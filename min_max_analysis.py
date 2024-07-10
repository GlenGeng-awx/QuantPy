import plotly.graph_objects as go
import time

from util import *
from conf import *


class MinMaxAnalysis:
    def __init__(self, stock_name: str, interval: str, stock_df: pd.DataFrame):
        self.stock_name = stock_name
        self.stock_df = stock_df.copy()  # copy to avoid warning

        from_date = shrink_date_str(stock_df.iloc[0]['Date'])
        to_date = shrink_date_str(stock_df.iloc[-1]['Date'])
        self.csv_file = f'./repo/{self.stock_name}_{from_date}_{to_date}_{interval}.csv'

    def add_column(self, column, dates: set):
        self.stock_df[column] = self.stock_df['Date'].isin(dates)

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

        # merge
        self.add_column(local_max_price_1st, local_max_price_1st_dates)
        self.add_column(local_max_price_2nd, local_max_price_2nd_dates)
        self.add_column(local_max_price_3rd, local_max_price_3rd_dates)
        self.add_column(local_max_price_4th, local_max_price_4th_dates)

        self.add_column(local_min_price_1st, local_min_price_1st_dates)
        self.add_column(local_min_price_2nd, local_min_price_2nd_dates)
        self.add_column(local_min_price_3rd, local_min_price_3rd_dates)
        self.add_column(local_min_price_4th, local_min_price_4th_dates)

    def regularize_volume(self):
        volume = self.stock_df['volume']

        print(f'volume mean: {volume.mean()}, volume std: {volume.std()}')

        self.stock_df[volume_reg] = (volume - volume.mean()) / volume.std()

        self.stock_df[volume_ma_5] = self.stock_df[volume_reg].rolling(window=5).mean()
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
        start_time = time.time()

        if os.path.exists(self.csv_file):
            self.from_csv()
        else:
            self.analyze_price()
            self.analyze_volume()
            # self.to_csv()

        end_time = time.time()
        print(f'MinMaxAnalysis on {self.stock_name} cost {(end_time - start_time) * 1000}ms')

    def to_csv(self):
        self.stock_df.to_csv(self.csv_file)

    def from_csv(self):
        self.stock_df = pd.read_csv(self.csv_file)


class PriceMinMaxDisplay:
    def __init__(self, fig: go.Figure, stock_df: pd.DataFrame):
        self.fig = fig
        self.stock_df = stock_df

    def add_scatter(self, filter_column: str, display_column: str, color: str, size: int):
        condition = self.stock_df[filter_column]
        x = self.stock_df[condition]['Date']
        y = self.stock_df[condition][display_column]

        self.fig.add_trace(
            go.Scatter(
                name=filter_column,
                x=x,
                y=y,
                mode='markers',
                marker=dict(
                    color=color,
                    size=size
                ),
                visible='legendonly',
            ),
            row=1, col=1,
        )

    def build_graph(self):
        self.add_scatter(local_max_price_1st, 'close', 'red', 4)
        self.add_scatter(local_min_price_1st, 'close', 'green', 4)

        self.add_scatter(local_max_price_2nd, 'close', 'red', 4)
        self.add_scatter(local_min_price_2nd, 'close', 'green', 4)

        self.add_scatter(local_max_price_3rd, 'close', 'red', 4)
        self.add_scatter(local_min_price_3rd, 'close', 'green', 4)

        self.add_scatter(local_max_price_4th, 'close', 'red', 4)
        self.add_scatter(local_min_price_4th, 'close', 'green', 4)

