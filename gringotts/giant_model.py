import copy
import pandas as pd
from features import FEATURE_BUF


def enumerate_switches(size: int) -> list[list]:
    if size == 0:
        return [[]]

    switches_part1 = enumerate_switches(size - 1)
    switches_part2 = copy.deepcopy(switches_part1)

    for switch in switches_part1:
        switch.append(False)

    for switch in switches_part2:
        switch.append(True)

    return switches_part1 + switches_part2


class TinyModel:
    def __init__(self, stock_df: pd.DataFrame, switch: list[bool]):
        self.stock_df = stock_df

        self.switch = switch
        self.name = ', '.join([feature.KEY for i, feature in enumerate(FEATURE_BUF) if switch[i]])

        self.indices = []

        self.successful_trades = 0
        self.successful_rate = 0

    def check_long(self, idx) -> bool:
        for i, feature in enumerate(FEATURE_BUF):
            if self.switch[i] and not self.stock_df[feature.KEY][idx]:
                return False
        return True

    def run(self):
        for idx in self.stock_df.index[:-5]:
            if self.check_long(idx):
                self.indices.append(idx)

        if not self.indices:
            return

        close = self.stock_df['close']

        for idx in self.indices:
            if close[idx] < close[idx + 5]:
                self.successful_trades += 1

        self.successful_rate = self.successful_trades / len(self.indices) * 100


class GiantModel:
    def __init__(self, stock_df: pd.DataFrame):
        self.stock_df = stock_df

    def run(self):
        switches = enumerate_switches(len(FEATURE_BUF))

        for i, switch in enumerate(switches):
            model = TinyModel(self.stock_df, switch)
            model.run()

            if model.successful_rate > 75 and len(model.indices) >= 2:
                print(f'{i + 1}/{len(switches)}: {model.successful_rate}% among {len(model.indices)}, {model.name}')


if __name__ == '__main__':
    print(FEATURE_BUF[6].KEY)
