from period_util import *
from period_conf import *


class PeriodAnalysis:
    def __init__(self, stock_name: str, stock_df: pd.DataFrame):
        self.stock_name = stock_name
        self.stock_df = stock_df.copy()  # copy to avoid warning

        from_date = stock_df.iloc[0]['Date']
        to_date = stock_df.iloc[-1]['Date']
        print(f"{self.stock_name} period_analysis -> range: {from_date} ~ {to_date}, shape: {self.stock_df.shape}")

        self.volume_std_div_volume_mean = 0

        # [(from_idx, from_date, from_low, to_idx, to_date, to_high, length, delta, pst, mid), ...]
        self.up_box = []
        # [(from_idx, from_date, from_high, to_idx, to_date, to_low, length, delta, pst, mid), ...]
        self.down_box = []

    def pick_up_box(self, from_idx, to_idx):
        from_date = self.stock_df.loc[from_idx]['Date']
        from_low = self.stock_df.loc[from_idx]['low']

        to_date = self.stock_df.loc[to_idx]['Date']
        to_high = self.stock_df.loc[to_idx]['high']

        length = to_idx - from_idx
        delta = to_high - from_low
        pst = 100 * delta / from_low
        mid = (from_low + to_high) / 2

        up_conf = {
            '000001.SS': 10,
            '000300.SS': 10,
        }
        target_pst = up_conf.get(self.stock_name, 20)

        if length <= 9 and pst < target_pst:
            print(f'drop up box, {from_date} ~ {to_date}, {length} days, {pst:.2f}%')
            return

        print(f'pick up box, {from_date} ~ {to_date}, {length} days, {delta:.2f}$, {pst:.2f}%, mid {mid}')
        self.up_box.append((from_idx, from_date, from_low, to_idx, to_date, to_high, length, delta, pst, mid))

    def up_analysis(self):
        triggered_idx = []
        for idx, row in self.stock_df.iterrows():
            if hit_up(row):
                triggered_idx.append(idx)

        triggered_idx.append(self.stock_df.index[-1] + 1)
        print(f"triggered up -> {triggered_idx}")

        for i in range(len(triggered_idx) - 1):
            start_idx, end_idx = triggered_idx[i], triggered_idx[i + 1]

            highest_idx = start_idx
            for idx in range(start_idx + 1, end_idx):
                if self.stock_df.loc[idx]['high'] > self.stock_df.loc[highest_idx]['high']:
                    highest_idx = idx

            self.pick_up_box(start_idx, highest_idx)

    def pick_down_box(self, from_idx, to_idx):
        from_date = self.stock_df.loc[from_idx]['Date']
        from_high = self.stock_df.loc[from_idx]['high']

        to_date = self.stock_df.loc[to_idx]['Date']
        to_low = self.stock_df.loc[to_idx]['low']

        length = to_idx - from_idx
        delta = from_high - to_low
        pst = 100 * delta / from_high
        mid = (from_high + to_low) / 2

        down_conf = {
            '000001.SS': 8,
            '000300.SS': 8,
        }
        target_pst = down_conf.get(self.stock_name, 15)

        if length <= 9 and pst < target_pst:
            print(f'drop down box, {from_date} ~ {to_date}, {length} days, {pst:.2f}%')
            return

        print(f'pick down box, {from_date} ~ {to_date}, {length} days, {delta:.2f}$, {pst:.2f}%, mid {mid}')
        self.down_box.append((from_idx, from_date, from_high, to_idx, to_date, to_low, length, delta, pst, mid))

    def down_analysis(self):
        triggered_idx = []
        for idx, row in self.stock_df.iterrows():
            if hit_down(row):
                triggered_idx.append(idx)

        triggered_idx.append(self.stock_df.index[-1] + 1)
        print(f"triggered down -> {triggered_idx}")

        for i in range(len(triggered_idx) - 1):
            start_idx, end_idx = triggered_idx[i], triggered_idx[i + 1]

            lowest_idx = start_idx
            for idx in range(start_idx + 1, end_idx):
                if self.stock_df.loc[idx]['low'] < self.stock_df.loc[lowest_idx]['low']:
                    lowest_idx = idx

            self.pick_down_box(start_idx, lowest_idx)

    def add_column(self, column, dates: set):
        self.stock_df[column] = self.stock_df['Date'].apply(lambda date: date in dates)

    def analyze_price(self):
        # local max price analysis
        local_max_price_1st_dates = local_max(self.stock_df)

        condition = self.stock_df['Date'].isin(local_max_price_1st_dates)
        local_max_price_2nd_dates = local_max(self.stock_df[condition])

        condition = self.stock_df['Date'].isin(local_max_price_2nd_dates)
        local_max_price_3rd_dates = local_max(self.stock_df[condition])

        condition = self.stock_df['Date'].isin(local_max_price_3rd_dates)
        local_max_price_4th_dates = local_max(self.stock_df[condition])

        # local min price analysis
        local_min_price_1st_dates = local_min(self.stock_df)

        condition = self.stock_df['Date'].isin(local_min_price_1st_dates)
        local_min_price_2nd_dates = local_min(self.stock_df[condition])

        condition = self.stock_df['Date'].isin(local_min_price_2nd_dates)
        local_min_price_3rd_dates = local_min(self.stock_df[condition])

        condition = self.stock_df['Date'].isin(local_min_price_3rd_dates)
        local_min_price_4th_dates = local_min(self.stock_df[condition])

        # range max price analysis
        range_max_price_15_dates = range_max(self.stock_df, 15)
        range_max_price_30_dates = range_max(self.stock_df, 30)

        # range min price analysis
        range_min_price_15_dates = range_min(self.stock_df, 15)
        range_min_price_30_dates = range_min(self.stock_df, 30)

        # merge
        self.add_column(local_max_price_1st, local_max_price_1st_dates)
        self.add_column(local_max_price_2nd, local_max_price_2nd_dates)
        self.add_column(local_max_price_3rd, local_max_price_3rd_dates)
        self.add_column(local_max_price_4th, local_max_price_4th_dates)

        self.add_column(local_min_price_1st, local_min_price_1st_dates)
        self.add_column(local_min_price_2nd, local_min_price_2nd_dates)
        self.add_column(local_min_price_3rd, local_min_price_3rd_dates)
        self.add_column(local_min_price_4th, local_min_price_4th_dates)

        self.add_column(range_max_price_15, range_max_price_15_dates)
        self.add_column(range_max_price_30, range_max_price_30_dates)

        self.add_column(range_min_price_15, range_min_price_15_dates)
        self.add_column(range_min_price_30, range_min_price_30_dates)

    def regularize_volume(self):
        volume = self.stock_df['volume']

        print(f'volume mean: {volume.mean()}, volume std: {volume.std()}')
        self.volume_std_div_volume_mean = volume.std() / volume.mean()

        self.stock_df[volume_reg] = (volume - volume.mean()) / volume.std()

        self.stock_df[volume_ma_15] = self.stock_df[volume_reg].rolling(window=15).mean()
        self.stock_df[volume_ma_30] = self.stock_df[volume_reg].rolling(window=30).mean()
        self.stock_df[volume_ma_60] = self.stock_df[volume_reg].rolling(window=60).mean()

        self.stock_df[volume_reg] = self.stock_df[volume_reg].apply(lambda v: 4 + (v - 4) / 6 if v > 4 else v)

    def analyze_volume(self):
        self.regularize_volume()

        # local max volume analysis
        local_max_volume_1st_dates = local_max(self.stock_df, volume_reg)

        condition = self.stock_df['Date'].isin(local_max_volume_1st_dates)
        local_max_volume_2nd_dates = local_max(self.stock_df[condition], volume_reg)

        condition = self.stock_df['Date'].isin(local_max_volume_2nd_dates)
        local_max_volume_3rd_dates = local_max(self.stock_df[condition], volume_reg)

        condition = self.stock_df['Date'].isin(local_max_volume_3rd_dates)
        local_max_volume_4th_dates = local_max(self.stock_df[condition], volume_reg)

        # local min volume analysis
        local_min_volume_1st_dates = local_min(self.stock_df, volume_reg)

        condition = self.stock_df['Date'].isin(local_min_volume_1st_dates)
        local_min_volume_2nd_dates = local_min(self.stock_df[condition], volume_reg)

        condition = self.stock_df['Date'].isin(local_min_volume_2nd_dates)
        local_min_volume_3rd_dates = local_min(self.stock_df[condition], volume_reg)

        condition = self.stock_df['Date'].isin(local_min_volume_3rd_dates)
        local_min_volume_4th_dates = local_min(self.stock_df[condition], volume_reg)

        # merge
        self.add_column(local_max_volume_1st, local_max_volume_1st_dates)
        self.add_column(local_max_volume_2nd, local_max_volume_2nd_dates)
        self.add_column(local_max_volume_3rd, local_max_volume_3rd_dates)
        self.add_column(local_max_volume_4th, local_max_volume_4th_dates)

        self.add_column(local_min_volume_1st, local_min_volume_1st_dates)
        self.add_column(local_min_volume_2nd, local_min_volume_2nd_dates)
        self.add_column(local_min_volume_3rd, local_min_volume_3rd_dates)
        self.add_column(local_min_volume_4th, local_min_volume_4th_dates)

    def analyze(self):
        self.analyze_price()
        self.analyze_volume()

        # box analysis
        self.up_analysis()
        self.down_analysis()

        print(self.stock_df.head(100))
