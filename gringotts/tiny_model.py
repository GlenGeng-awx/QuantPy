import pandas as pd
from features import FEATURE_BUF
from gringotts import FORECAST_STEP, MARGIN, HIT_THRESHOLD, SUCCESSFUL_RATE


# one filter for each switch
# during train, input_indices is the output_indices of previous step
# during predict, input_indices is specified by caller
class _Filter:
    def __init__(self, stock_df: pd.DataFrame, switch: list[bool],
                 input_indices: list[int], train_position: int = None, train_ctx: dict = None):
        self.stock_df = stock_df

        self.switch = switch
        self.input_indices = input_indices

        self.train_position = train_position
        self.train_ctx = train_ctx

        self.output_indices = []  # #

    def _filter_in_train(self, idx):
        if self.switch[self.train_position]:
            feature = FEATURE_BUF[self.train_position]
            return self.train_ctx[idx][feature.KEY]
        return True

    def _filter_in_predict(self, idx):
        for i, feature in enumerate(FEATURE_BUF):
            if self.switch[i] and \
                    not self.stock_df[feature.KEY].loc[idx - feature.RECALL_DAYS + 1:idx].any():
                return False
        return True

    def _dispatch(self, idx) -> bool:
        if self.train_position is not None:
            return self._filter_in_train(idx)
        else:
            return self._filter_in_predict(idx)

    def filter(self):
        for idx in self.input_indices:
            if self._dispatch(idx):
                self.output_indices.append(idx)

    def abbr(self):
        return ','.join([str(i) for i in range(len(self.switch)) if self.switch[i]])

    def name(self):
        return ', '.join([feature.KEY for i, feature in enumerate(FEATURE_BUF) if self.switch[i]])


# given a filter, evaluate the performance of the model
# during train, just do a coarse evaluation
class _EvaluatorInTrain:
    def __init__(self, stock_df: pd.DataFrame, train_ctx: dict,
                 forecast_step: int, margin: float, hit_threshold: int, successful_rate: float):
        self.stock_df = stock_df
        self.train_ctx = train_ctx

        self.forecast_step = forecast_step
        self.margin = margin
        self.hit_threshold = hit_threshold
        self.successful_rate = successful_rate

        self.valid_trade_num = None

        self.successful_long_rate = 0
        self.successful_short_rate = 0

        self.pass_long = False
        self.pass_short = False

    def evaluate(self, output_indices: list[int]):
        # prune is important in train
        if len(output_indices) < self.hit_threshold:
            return

        # span is important
        if output_indices[-1] - output_indices[0] < 10:
            return

        valid_trade_num = 0

        successful_long_trades = 0
        successful_short_trades = 0

        close = self.stock_df['close']

        for idx in output_indices:
            if idx + self.forecast_step not in close:
                break
            valid_trade_num += 1

            # if close[idx] * (1 + self.margin) < close[idx + self.forecast_step]:
            if self.train_ctx[idx][self.forecast_step][self.margin]['long']:
                successful_long_trades += 1

            # if close[idx] * (1 - self.margin) > close[idx + self.forecast_step]:
            if self.train_ctx[idx][self.forecast_step][self.margin]['short']:
                successful_short_trades += 1

        if valid_trade_num < self.hit_threshold:
            return

        self.valid_trade_num = valid_trade_num

        self.successful_long_rate = successful_long_trades / valid_trade_num * 100
        self.successful_short_rate = successful_short_trades / valid_trade_num * 100

        self.pass_long = self.successful_long_rate >= self.successful_rate
        self.pass_short = self.successful_short_rate >= self.successful_rate

    def _long_name(self):
        name = f'L {self.forecast_step}d {self.margin * 100:.1f}% {self.hit_threshold}'
        name += f'|{self.valid_trade_num:02} {int(self.successful_long_rate)}%'
        return name

    def _short_name(self):
        name = f'S {self.forecast_step}d {self.margin * 100:.1f}% {self.hit_threshold}'
        name += f'|{self.valid_trade_num:02} {int(self.successful_short_rate)}%'
        return name

    def name(self):
        if self.pass_long:
            return self._long_name()
        elif self.pass_short:
            return self._short_name()
        else:
            return ''


# given a filter, evaluate the performance of the model
# during predict, do a fine evaluation
class _EvaluatorInPredict:
    def __init__(self, stock_df: pd.DataFrame,
                 forecast_step: int, margin: float, hit_threshold: int, successful_rate: float):
        self.stock_df = stock_df

        self.forecast_step = forecast_step
        self.margin = margin
        self.hit_threshold = hit_threshold
        self.successful_rate = successful_rate

        self.valid_trade_num = 0

        self.successful_long_rate = 0
        self.expect_long_margin = 0
        self.pass_long = False

        self.successful_short_rate = 0
        self.expect_short_margin = 0
        self.pass_short = False

    def evaluate(self, output_indices: list[int]):
        valid_trade_num = 0

        successful_long_trades = 0
        successful_short_trades = 0

        total_long_margin = 0
        total_short_margin = 0

        close = self.stock_df['close']

        for idx in output_indices:
            if idx + self.forecast_step not in close:
                break
            valid_trade_num += 1

            if close[idx] * (1 + self.margin) < close[idx + self.forecast_step]:
                successful_long_trades += 1

            if close[idx] * (1 - self.margin) > close[idx + self.forecast_step]:
                successful_short_trades += 1

            max_close = close.loc[idx:idx + self.forecast_step].max()
            min_close = close.loc[idx:idx + self.forecast_step].min()

            total_long_margin += (max_close - close[idx]) / close[idx] * 100
            total_short_margin += (close[idx] - min_close) / close[idx] * 100

        if valid_trade_num == 0:
            return

        self.valid_trade_num = valid_trade_num

        self.successful_long_rate = successful_long_trades / valid_trade_num * 100
        self.successful_short_rate = successful_short_trades / valid_trade_num * 100

        self.expect_long_margin = total_long_margin / valid_trade_num
        self.expect_short_margin = total_short_margin / valid_trade_num

        self.pass_long = self.successful_long_rate >= self.successful_rate
        self.pass_short = self.successful_short_rate >= self.successful_rate

    def name(self):
        name = 'N '
        if self.pass_long:
            name = 'L '
        elif self.pass_short:
            name = 'S '

        name += f'{self.forecast_step}d {self.margin * 100:.1f}% {self.hit_threshold}<br>'
        name += f'{self.valid_trade_num:02} L {int(self.successful_long_rate)}% S {int(self.successful_short_rate)}%<br>'
        name += f'EXP +{self.expect_long_margin:.1f}% -{self.expect_short_margin:.1f}%'
        return name


# during train, one switch has multiple evaluators, each do a coarse evaluation
# during predict, one switch has only one evaluator, do a fine evaluation
class TinyModel:
    def __init__(self, stock_df: pd.DataFrame, conf: dict, switch: list[bool],
                 input_indices: list[int], train_position: int = None, train_ctx: dict = None):
        self.filter = _Filter(stock_df, switch, input_indices, train_position, train_ctx)

        if train_position is not None:
            self.evaluators = [
                _EvaluatorInTrain(stock_df, train_ctx, conf[FORECAST_STEP], **eval_conf)
                for eval_conf in conf['evaluators']
            ]
        else:
            self.evaluators = [
                _EvaluatorInPredict(stock_df,
                                    conf[FORECAST_STEP],
                                    conf[MARGIN],
                                    conf[HIT_THRESHOLD],
                                    conf[SUCCESSFUL_RATE],
                                    )
            ]

    def phase1(self):
        self.filter.filter()

    def phase2(self):
        for evaluator in self.evaluators:
            evaluator.evaluate(self.filter.output_indices)

    def pass_long(self):
        return any(evaluator.pass_long for evaluator in self.evaluators)

    def pass_short(self):
        return any(evaluator.pass_short for evaluator in self.evaluators)

    def name(self):
        filter_name = f'{self.filter.name()}'
        eval_names = [evaluator.name() for evaluator in self.evaluators if evaluator.name()]
        return ';'.join(eval_names) + '\t' + filter_name

    def label(self):
        filter_label = f'{self.filter.abbr()}'
        eval_names = [evaluator.name() for evaluator in self.evaluators if evaluator.name()]
        return '<br>'.join([filter_label] + eval_names)


if __name__ == '__main__':
    for j in range(len(FEATURE_BUF)):
        print(f'{j} {FEATURE_BUF[j].KEY}')

    abbrs = [
        [10, 29],
    ]

    for abbr in abbrs:
        print(abbr, ' / '.join([FEATURE_BUF[i].KEY for i in abbr]))
