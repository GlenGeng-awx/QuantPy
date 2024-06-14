from util import *
from price_support_resistance_analysis import is_support_level, is_resistance_level


class PriceBoxAnalysis:
    def __init__(self, stock_df: pd.DataFrame):
        self.stock_df = stock_df

        # [(from_idx, from_date, from_low, to_idx, to_date, to_high, length, delta, pst, mid), ...]
        self.up_box = []
        # [(from_idx, from_date, from_high, to_idx, to_date, to_low, length, delta, pst, mid), ...]
        self.down_box = []

    def build_up_box(self, from_idx, to_idx):
        from_date = self.stock_df.loc[from_idx]['Date']
        from_low = self.stock_df.loc[from_idx]['low']

        to_date = self.stock_df.loc[to_idx]['Date']
        to_high = self.stock_df.loc[to_idx]['high']

        length = to_idx - from_idx
        delta = to_high - from_low
        pst = 100 * delta / from_low
        mid = (from_low + to_high) / 2

        print(f'build up box, {from_date} ~ {to_date}, {length} days, {delta:.2f}$, {pst:.2f}%, mid {mid}')
        self.up_box.append((from_idx, from_date, from_low, to_idx, to_date, to_high, length, delta, pst, mid))

    def build_down_box(self, from_idx, to_idx):
        from_date = self.stock_df.loc[from_idx]['Date']
        from_high = self.stock_df.loc[from_idx]['high']

        to_date = self.stock_df.loc[to_idx]['Date']
        to_low = self.stock_df.loc[to_idx]['low']

        length = to_idx - from_idx
        delta = from_high - to_low
        pst = 100 * delta / from_high
        mid = (from_high + to_low) / 2

        print(f'build down box, {from_date} ~ {to_date}, {length} days, {delta:.2f}$, {pst:.2f}%, mid {mid}')
        self.down_box.append((from_idx, from_date, from_high, to_idx, to_date, to_low, length, delta, pst, mid))

    def analyze_middle(self, start_idx, end_idx):
        start_row = self.stock_df.loc[start_idx]
        end_row = self.stock_df.loc[end_idx]

        if is_support_level(start_row) and is_resistance_level(end_row):
            self.build_up_box(start_idx, end_idx)

        if is_resistance_level(start_row) and is_support_level(end_row):
            self.build_down_box(start_idx, end_idx)

        if is_support_level(start_row) and is_support_level(end_row):
            highest_idx = max_between(self.stock_df, start_idx + 1, end_idx - 1)
            self.build_up_box(start_idx, highest_idx)
            self.build_down_box(highest_idx, end_idx)

        if is_resistance_level(start_row) and is_resistance_level(end_row):
            lowest_idx = min_between(self.stock_df, start_idx + 1, end_idx - 1)
            self.build_down_box(start_idx, lowest_idx)
            self.build_up_box(lowest_idx, end_idx)

    def analyze_head(self, head_idx):
        head_row = self.stock_df.loc[head_idx]

        if is_support_level(head_row):
            start_idx = max_between(self.stock_df, self.stock_df.index[0], head_idx - 1)
            self.build_down_box(start_idx, head_idx)

        if is_resistance_level(head_row):
            start_idx = min_between(self.stock_df, self.stock_df.index[0], head_idx - 1)
            self.build_up_box(start_idx, head_idx)

    def analyze_tail(self, tail_idx):
        tail_row = self.stock_df.loc[tail_idx]

        if is_support_level(tail_row):
            end_idx = max_between(self.stock_df, tail_idx + 1, self.stock_df.index[-1])
            self.build_up_box(tail_idx, end_idx)

        if is_resistance_level(tail_row):
            end_idx = min_between(self.stock_df, tail_idx + 1, self.stock_df.index[-1])
            self.build_down_box(tail_idx, end_idx)

    def analyze(self):
        triggered_idx = []
        for idx, row in self.stock_df.iterrows():
            if is_support_level(row) or is_resistance_level(row):
                triggered_idx.append(idx)

        print(f"triggered up down -> {triggered_idx}")
        if len(triggered_idx) < 2:
            return

        for i in range(1, len(triggered_idx)):
            start_idx, end_idx = triggered_idx[i - 1], triggered_idx[i]
            self.analyze_middle(start_idx, end_idx)

        self.analyze_head(triggered_idx[0])
        self.analyze_tail(triggered_idx[-1])
