import plotly.graph_objects as go
from plotly.subplots import make_subplots

from util import *


class PeriodAnalysis:
    def __init__(self, stock_name: str, stock_df: pd.DataFrame):
        self.stock_name = stock_name

        self.stock_df = stock_df.copy()  # copy to avoid warning
        self.from_date = stock_df.iloc[0]['Date']
        self.to_date = stock_df.iloc[-1]['Date']
        print(f"{self.stock_name} period_analysis -> range: {self.from_date} ~ {self.to_date}, shape: {self.stock_df.shape}")

        # [(from_idx, from_date, from_low, to_idx, to_date, to_high, length, delta, pst, mid), ...]
        self.up_box = []
        # [(from_idx, from_date, from_high, to_idx, to_date, to_low, length, delta, pst, mid), ...]
        self.down_box = []

        self.volume_std_div_mean = 0
        self.fig = None

    def add_candlestick(self):
        self.fig.add_trace(
            go.Candlestick(
                x=self.stock_df['Date'],
                close=self.stock_df['close'],
                open=self.stock_df['open'],
                high=self.stock_df['high'],
                low=self.stock_df['low'],
                name="Candlesticks",
                increasing_line_color='red',
                decreasing_line_color='green',
                line=dict(width=0.5)
            )
        )

    def add_volume(self):
        self.fig.add_trace(
            go.Scatter(
                x=self.stock_df['Date'],
                y=self.stock_df['volume_reg'],
                mode='markers+lines',
                line=dict(width=0.5),
                marker_size=1,
                marker_color='blue',
            ),
            row=2, col=1
        )

        self.fig.add_trace(
            go.Scatter(
                x=self.stock_df['Date'],
                y=self.stock_df['volume_ma_n'],
                mode='lines',
                line=dict(width=0.5, color='black'),
            ),
            row=2, col=1
        )

    def add_scatter(self, filter_column: str, display_column: str, color: str, size: int, row=1, col=1):
        self.fig.add_trace(
            go.Scatter(
                x=self.stock_df[self.stock_df[filter_column]]['Date'],
                y=self.stock_df[self.stock_df[filter_column]][display_column],
                mode='markers',
                marker=dict(
                    color=color,
                    size=size
                )
            ),
            row=row, col=col,
        )

    def add_hline(self):
        for idx, row in self.stock_df.iterrows():
            if hit_down(row):
                self.fig.add_hline(y=row['high'], line_width=0.5, line_dash="dash", line_color="green", row=1, col=1)

            if hit_up(row):
                self.fig.add_hline(y=row['low'], line_width=0.5, line_dash="dash", line_color="red", row=1, col=1)

    def add_vline(self, dates):
        for date in dates:
            self.fig.add_vline(x=date, line_width=1, line_dash="dash", line_color="black")

    def add_up_box(self, _from_idx, from_date, from_low, _to_idx, to_date, to_high, length, delta, pst, mid):
        self.fig.add_shape(
            type="rect",
            x0=from_date, y0=from_low, x1=to_date, y1=to_high,
            line=dict(
                color="Red",
                width=1,
                dash="dot"
            ),
            label=dict(
                text=f'{length}D <br> {delta:.2f}$ <br> +{pst:.2f}%',
                textposition="bottom center"
            ),
        )

        self.fig.add_shape(
            type="line",
            x0=from_date, y0=mid, x1=to_date, y1=mid,
            line=dict(
                color="Red",
                width=0.5,
                dash="dot"
            )
        )

    def add_down_box(self, _from_idx, from_date, from_high, _to_idx, to_date, to_low, length, delta, pst, mid):
        self.fig.add_shape(
            type="rect",
            x0=from_date, y0=from_high, x1=to_date, y1=to_low,
            line=dict(
                color="Green",
                width=1,
                dash="dot",
            ),
            label=dict(
                text=f'-{pst:.2f}% <br> {delta:.2f}$ <br> {length}D',
                textposition="top center"
            ),
        )

        self.fig.add_shape(
            type="line",
            x0=from_date, y0=mid, x1=to_date, y1=mid,
            line=dict(
                color="Green",
                width=0.5,
                dash="dot",
            )
        )

    def build_graph(self):
        self.fig = make_subplots(rows=2, cols=1,
                                 subplot_titles=("candle stick", f"std/mean={self.volume_std_div_mean:.2f}"),
                                 vertical_spacing=0.05,
                                 row_heights=[0.7, 0.3],
                                 shared_xaxes=True,
                                 )

        self.add_candlestick()

        self.add_scatter('local_max_1st', 'high', 'red', 2)
        self.add_scatter('local_max_2nd', 'high', 'red', 6)
        self.add_scatter('local_max_3rd', 'high', 'red', 10)
        self.add_scatter('range_max_n', 'high', 'black', 4)

        self.add_scatter('local_min_1st', 'low', 'green', 2)
        self.add_scatter('local_min_2nd', 'low', 'green', 6)
        self.add_scatter('local_min_3rd', 'low', 'green', 10)
        self.add_scatter('range_min_n', 'low', 'blue', 4)

        for item in self.up_box:
            self.add_up_box(*item)

        for item in self.down_box:
            self.add_down_box(*item)

        if self.stock_df.shape[0] < 300:
            self.add_hline()

        self.add_volume()

        self.add_scatter('local_max_volume_1st', 'volume_reg', 'red', 2, row=2, col=1)
        self.add_scatter('local_max_volume_2nd', 'volume_reg', 'red', 4, row=2, col=1)
        self.add_scatter('local_max_volume_3rd', 'volume_reg', 'red', 8, row=2, col=1)

        self.add_scatter('local_min_volume_1st', 'volume_reg', 'green', 2, row=2, col=1)
        self.add_scatter('local_min_volume_2nd', 'volume_reg', 'green', 4, row=2, col=1)
        self.add_scatter('local_min_volume_3rd', 'volume_reg', 'green', 8, row=2, col=1)

        self.fig.update_xaxes(
            rangebreaks=[
                dict(bounds=["sat", "mon"]),  # hide weekends
            ]
        )

        self.fig.update_layout(
            title=f'{self.stock_name} Period Analysis {self.from_date} ~ {self.to_date}',
            xaxis_rangeslider_visible=False,
            hovermode='x unified',
        )

    def pick_up_box(self, from_idx, to_idx):
        from_date = self.stock_df.loc[from_idx]['Date']
        from_low = self.stock_df.loc[from_idx]['low']

        to_date = self.stock_df.loc[to_idx]['Date']
        to_high = self.stock_df.loc[to_idx]['high']

        length = to_idx - from_idx
        delta = to_high - from_low
        pst = 100 * delta / from_low
        mid = (from_low + to_high) / 2

        if length <= 9 and pst < 20:
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

        if length <= 9 and pst < 15:
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

    def regularize_volume(self):
        volume = self.stock_df['volume']
        print(f'volume mean: {volume.mean()}, volume std: {volume.std()}')
        self.volume_std_div_mean = volume.std() / volume.mean()
        self.stock_df['volume_reg'] = (volume - volume.mean()) / volume.std()
        self.stock_df['volume_ma_n'] = self.stock_df['volume_reg'].rolling(window=15).mean()

    def add_column(self, column, dates: set):
        self.stock_df[column] = self.stock_df['Date'].apply(lambda date: date in dates)

    def analyze(self):
        # calculate candle stick
        local_max_1st_dates = local_max(self.stock_df)
        local_max_2nd_dates = local_max(self.stock_df[self.stock_df['Date'].isin(local_max_1st_dates)])
        local_max_3rd_dates = local_max(self.stock_df[self.stock_df['Date'].isin(local_max_2nd_dates)])

        range_max_n_dates = range_max(self.stock_df, 15)

        local_min_1st_dates = local_min(self.stock_df)
        local_min_2nd_dates = local_min(self.stock_df[self.stock_df['Date'].isin(local_min_1st_dates)])
        local_min_3rd_dates = local_min(self.stock_df[self.stock_df['Date'].isin(local_min_2nd_dates)])

        range_min_n_dates = range_min(self.stock_df, 15)

        # merge
        self.add_column('local_max_1st', local_max_1st_dates)
        self.add_column('local_max_2nd', local_max_2nd_dates)
        self.add_column('local_max_3rd', local_max_3rd_dates)
        self.add_column('range_max_n', range_max_n_dates)

        self.add_column('local_min_1st', local_min_1st_dates)
        self.add_column('local_min_2nd', local_min_2nd_dates)
        self.add_column('local_min_3rd', local_min_3rd_dates)
        self.add_column('range_min_n', range_min_n_dates)

        self.up_analysis()
        self.down_analysis()

        # calculate volume
        self.regularize_volume()

        local_max_volume_1st_dates = local_max(self.stock_df, 'volume_reg')
        local_max_volume_2nd_dates = local_max(
            self.stock_df[self.stock_df['Date'].isin(local_max_volume_1st_dates)], 'volume_reg')
        local_max_volume_3rd_dates = local_max(
            self.stock_df[self.stock_df['Date'].isin(local_max_volume_2nd_dates)], 'volume_reg')

        local_min_volume_1st_dates = local_min(self.stock_df, 'volume_reg')
        local_min_volume_2nd_dates = local_min(
            self.stock_df[self.stock_df['Date'].isin(local_min_volume_1st_dates)], 'volume_reg')
        local_min_volume_3rd_dates = local_min(
            self.stock_df[self.stock_df['Date'].isin(local_min_volume_2nd_dates)], 'volume_reg')

        # merge
        self.add_column('local_max_volume_1st', local_max_volume_1st_dates)
        self.add_column('local_max_volume_2nd', local_max_volume_2nd_dates)
        self.add_column('local_max_volume_3rd', local_max_volume_3rd_dates)

        self.add_column('local_min_volume_1st', local_min_volume_1st_dates)
        self.add_column('local_min_volume_2nd', local_min_volume_2nd_dates)
        self.add_column('local_min_volume_3rd', local_min_volume_3rd_dates)

        # print(self.stock_df)
