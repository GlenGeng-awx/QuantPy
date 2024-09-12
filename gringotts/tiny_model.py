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

        self.successful_long_trades = 0
        self.successful_long_rate = 0

        self.successful_short_trades = 0
        self.successful_short_rate = 0

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
        close = self.stock_df['close']
        valid_trade_num = 0

        for idx in self.output_indices:
            if idx + self.forecast_step in close:
                valid_trade_num += 1
            else:
                continue

            if close[idx] * (1 + self.margin) < close[idx + self.forecast_step]:
                self.successful_long_trades += 1

            if close[idx] * (1 - self.margin) > close[idx + self.forecast_step]:
                self.successful_short_trades += 1

        if valid_trade_num == 0:
            return

        self.successful_long_rate = self.successful_long_trades / valid_trade_num * 100
        self.successful_short_rate = self.successful_short_trades / valid_trade_num * 100

    def run(self):
        self._filter()
        self._evaluate()

    def pass_long(self):
        return self.successful_long_rate >= self.successful_rate \
            and len(self.output_indices) >= self.hit_threshold

    def pass_short(self):
        return self.successful_short_rate >= self.successful_rate \
            and len(self.output_indices) >= self.hit_threshold


if __name__ == '__main__':
    for j in range(len(FEATURE_BUF)):
        print(f'{j} {FEATURE_BUF[j].KEY}')

    abbrs = [
        [6, 21, 27],
    ]

    for abbr in abbrs:
        print(abbr, ' / '.join([FEATURE_BUF[i].KEY for i in abbr]))
