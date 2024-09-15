import pandas as pd
from features import FEATURE_BUF
from gringotts import RECALL_STEP, FORECAST_STEP, MARGIN, HIT_THRESHOLD, SUCCESSFUL_RATE


class TinyModel:
    def __init__(self, stock_df: pd.DataFrame, conf: dict, switch: list[bool],
                 input_indices: list[int], train_position: int = None):
        self.stock_df = stock_df

        self.recall_step = conf[RECALL_STEP]
        self.forecast_step = conf[FORECAST_STEP]
        self.margin = conf[MARGIN]
        self.hit_threshold = conf[HIT_THRESHOLD]
        self.successful_rate = conf[SUCCESSFUL_RATE]

        self.switch = switch
        self.abbr = ','.join([str(i) for i in range(len(switch)) if switch[i]])
        self.name = ', '.join([feature.KEY for i, feature in enumerate(FEATURE_BUF) if switch[i]])

        self.input_indices = input_indices
        self.train_position = train_position

        self.output_indices = []
        self.valid_trade_num = 0

        self.successful_long_rate = 0
        self.successful_short_rate = 0

        self.expect_long_margin = 0
        self.expect_short_margin = 0

    def _train(self, idx):
        if self.switch[self.train_position]:
            feature = FEATURE_BUF[self.train_position]
            return self.stock_df[feature.KEY].loc[idx - self.recall_step + 1:idx].any()
        return True

    def _predict(self, idx):
        for i, feature in enumerate(FEATURE_BUF):
            if self.switch[i] and \
                    not self.stock_df[feature.KEY].loc[idx - self.recall_step + 1:idx].any():
                return False
        return True

    def _check(self, idx) -> bool:
        if self.train_position is not None:
            return self._train(idx)
        else:
            return self._predict(idx)

    def _filter(self):
        for idx in self.input_indices:
            if self._check(idx):
                self.output_indices.append(idx)

    def _evaluate(self):
        valid_trade_num = 0

        successful_long_trades = 0
        successful_short_trades = 0

        total_long_margin = 0
        total_short_margin = 0

        close = self.stock_df['close']

        for idx in self.output_indices:
            if idx + self.forecast_step in close:
                valid_trade_num += 1
            else:
                continue

            if close[idx] * (1 + self.margin) < close[idx + self.forecast_step]:
                successful_long_trades += 1

            if close[idx] * (1 - self.margin) > close[idx + self.forecast_step]:
                successful_short_trades += 1

            max_close = close.loc[idx + 1:idx + self.forecast_step].max()
            min_close = close.loc[idx + 1:idx + self.forecast_step].min()

            if max_close > close[idx]:
                total_long_margin += (max_close - close[idx]) / close[idx] * 100

            if min_close < close[idx]:
                total_short_margin += (close[idx] - min_close) / close[idx] * 100

        if valid_trade_num == 0:
            return

        self.valid_trade_num = valid_trade_num

        self.successful_long_rate = successful_long_trades / valid_trade_num * 100
        self.successful_short_rate = successful_short_trades / valid_trade_num * 100

        self.expect_long_margin = total_long_margin / valid_trade_num
        self.expect_short_margin = total_short_margin / valid_trade_num

    def run(self):
        self._filter()
        self._evaluate()

    def pass_long(self):
        return self.successful_long_rate >= self.successful_rate \
            and self.valid_trade_num >= self.hit_threshold

    def pass_short(self):
        return self.successful_short_rate >= self.successful_rate \
            and self.valid_trade_num >= self.hit_threshold


if __name__ == '__main__':
    for j in range(len(FEATURE_BUF)):
        print(f'{j} {FEATURE_BUF[j].KEY}')

    abbrs = [
        [10, 29],
    ]

    for abbr in abbrs:
        print(abbr, ' / '.join([FEATURE_BUF[i].KEY for i in abbr]))
