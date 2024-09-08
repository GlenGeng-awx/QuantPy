import pandas as pd
from features import FEATURE_BUF


class TinyModel:
    def __init__(self, stock_df: pd.DataFrame, switch: list[bool]):
        self.stock_df = stock_df

        self.switch = switch
        self.abbr = ','.join([str(i) for i in range(len(switch)) if switch[i]])
        self.name = ', '.join([feature.KEY for i, feature in enumerate(FEATURE_BUF) if switch[i]])

        self.indices = []

        self.successful_long_trades = 0
        self.successful_long_rate = 0

        self.successful_short_trades = 0
        self.successful_short_rate = 0

    def check(self, idx) -> bool:
        for i, feature in enumerate(FEATURE_BUF):
            if self.switch[i] and not self.stock_df[feature.KEY][idx]:
                return False
        return True

    def run(self):
        for idx in self.stock_df.index:
            if self.check(idx):
                self.indices.append(idx)

        # evaluate the model
        valid_trade_num = 0
        step = 5
        margin = 0.03

        close = self.stock_df['close']

        for idx in self.indices:
            if idx + step in close:
                valid_trade_num += 1
            else:
                continue

            if close[idx] * (1 + margin) < close[idx + step]:
                self.successful_long_trades += 1

            if close[idx] * (1 - margin) > close[idx + step]:
                self.successful_short_trades += 1

        if valid_trade_num == 0:
            return

        self.successful_long_rate = self.successful_long_trades / valid_trade_num * 100
        self.successful_short_rate = self.successful_short_trades / valid_trade_num * 100


if __name__ == '__main__':
    abbrs = [
        [0, 7],
        [13],
        [2, 17],
    ]

    for abbr in abbrs:
        print(abbr, ' / '.join([FEATURE_BUF[i].KEY for i in abbr]))
