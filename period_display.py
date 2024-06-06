import pandas as pd
import plotly.graph_objects as go
from pandas import Series
from plotly.subplots import make_subplots

from period_analysis import *


class PeriodDisplay:
    def __init__(self, period_analysis: PeriodAnalysis):
        self.stock_name = period_analysis.stock_name
        self.stock_df = period_analysis.stock_df.copy()

        self.volume_std_div_volume_mean = period_analysis.volume_std_div_volume_mean

        self.up_box = period_analysis.up_box
        self.down_box = period_analysis.down_box

        self.fig = None

    def add_price_scatter(self, filter_column: str, display_column: str, color: str, size: int):
        self.fig.add_trace(
            go.Scatter(
                name=filter_column,
                x=self.stock_df[self.stock_df[filter_column]]['Date'],
                y=self.stock_df[self.stock_df[filter_column]][display_column],
                mode='markers',
                marker=dict(
                    color=color,
                    size=size
                )
            ),
            row=1, col=1,
        )

    def add_price_mountain_view(self):
        x, y = [], []

        for idx, row in self.stock_df.iterrows():
            local_max_1st, local_min_1st = row[local_max_price_1st], row[local_min_price_1st]
            high, low, date = row['high'], row['low'], row['Date'],

            if local_max_1st or local_min_1st:
                x.append(date)
                y.append(high if local_max_1st else low)

        self.fig.add_trace(
            go.Scatter(
                name='price mountain view',
                x=x,
                y=y,
                mode='lines',
                line=dict(width=0.5, color='grey'),
            )
        )

    def build_candlestick(self):
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

        self.add_price_mountain_view()

        self.add_price_scatter(local_max_price_1st, 'high', 'red', 2)
        self.add_price_scatter(local_max_price_2nd, 'high', 'red', 4)
        self.add_price_scatter(local_max_price_3rd, 'high', 'red', 6)
        self.add_price_scatter(local_max_price_4th, 'high', 'red', 8)

        self.add_price_scatter(local_min_price_1st, 'low', 'green', 2)
        self.add_price_scatter(local_min_price_2nd, 'low', 'green', 4)
        self.add_price_scatter(local_min_price_3rd, 'low', 'green', 6)
        self.add_price_scatter(local_min_price_4th, 'low', 'green', 8)

        self.add_price_scatter(range_max_price_15, 'high', 'black', 2)
        self.add_price_scatter(range_max_price_30, 'high', 'black', 4)

        self.add_price_scatter(range_min_price_15, 'low', 'black', 2)
        self.add_price_scatter(range_min_price_30, 'low', 'black', 4)

    def in_precise_view(self):
        return self.stock_df.shape[0] < 400
        # return True

    def add_volume_ma(self, column, color: str, size: float):
        self.fig.add_trace(
            go.Scatter(
                name=column,
                x=self.stock_df['Date'],
                y=self.stock_df[column],
                mode='lines',
                line=dict(width=size, color=color),
            ),
            row=2, col=1
        )

    def add_volume_scatter(self, condition: Series, color: str, size: int):
        self.fig.add_trace(
            go.Scatter(
                x=self.stock_df[condition]['Date'],
                y=self.stock_df[condition][volume_reg],
                mode='markers',
                marker_size=size,
                marker_color=color,
            ),
            row=2, col=1
        )

    def build_volume_graph(self):
        # step A
        condition = (
                self.stock_df[local_max_volume_1st]
                | self.stock_df[local_min_volume_1st]
                | (self.stock_df[volume_reg] > 2)
        )
        self.fig.add_trace(
            go.Scatter(
                name='volume mountain view',
                x=self.stock_df[condition]['Date'],
                y=self.stock_df[condition][volume_reg],
                mode='lines',
                line=dict(width=0.5, color='grey'),
            ),
            row=2, col=1
        )

        self.add_volume_ma(volume_ma_15, 'red', 0.5)
        self.add_volume_ma(volume_ma_30, 'grey', 0.5)
        self.add_volume_ma(volume_ma_60, 'green', 0.5)

        condition = (self.stock_df['Date'] == self.stock_df['Date'])
        self.add_volume_scatter(condition, 'blue', 2)

        # step B
        condition = self.stock_df[local_min_volume_2nd]
        self.add_volume_scatter(condition, 'black', 2)

        condition = self.stock_df[local_min_volume_3rd]
        self.add_volume_scatter(condition, 'black', 4)

        condition = self.stock_df[local_min_volume_4th]
        self.add_volume_scatter(condition, 'black', 6)

        # step C
        condition1 = (
                self.stock_df[local_max_volume_2nd]
                & (self.stock_df['open'] < self.stock_df['close'])
        )
        self.add_volume_scatter(condition1, 'red', 2)

        condition2 = (
                self.stock_df[local_max_volume_3rd]
                & (self.stock_df['open'] < self.stock_df['close'])
        )
        self.add_volume_scatter(condition2, 'red', 4)

        condition3 = (
                self.stock_df[local_max_volume_4th]
                & (self.stock_df['open'] < self.stock_df['close'])
        )
        self.add_volume_scatter(condition3, 'red', 6)

        for date in self.stock_df[condition2 | condition3]['Date']:
            self.fig.add_vline(x=date, line_width=1, line_dash="dash", line_color='red', row=1, col=1)

        # step D
        condition1 = (
                self.stock_df[local_max_volume_2nd]
                & (self.stock_df['open'] > self.stock_df['close'])
        )
        self.add_volume_scatter(condition1, 'green', 2)

        condition2 = (
                self.stock_df[local_max_volume_3rd]
                & (self.stock_df['open'] > self.stock_df['close'])
        )
        self.add_volume_scatter(condition2, 'green', 4)

        condition3 = (
                self.stock_df[local_max_volume_4th]
                & (self.stock_df['open'] > self.stock_df['close'])
        )
        self.add_volume_scatter(condition3, 'green', 6)

        for date in self.stock_df[condition2 | condition3]['Date']:
            self.fig.add_vline(x=date, line_width=1, line_dash="dash", line_color='green', row=1, col=1)

    def add_hline(self):
        for idx, row in self.stock_df.iterrows():
            if hit_down(row):
                self.fig.add_hline(y=row['high'], line_width=0.5, line_dash="dash", line_color="grey", row=1, col=1)
            if hit_up(row):
                self.fig.add_hline(y=row['low'], line_width=0.5, line_dash="dash", line_color="grey", row=1, col=1)

    def add_up_box(self, _from_idx, from_date, from_low, _to_idx, to_date, to_high, length, delta, pst, mid):
        self.fig.add_shape(
            type="rect",
            x0=from_date, y0=from_low, x1=to_date, y1=to_high,
            line=dict(
                color="Red",
                width=0.5,
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

        self.fig.add_shape(
            type="line",
            x0=from_date, y0=from_low, x1=to_date, y1=to_high,
            line=dict(
                color="Red",
                width=0.5,
                # dash="dot"
            )
        )

    def add_down_box(self, _from_idx, from_date, from_high, _to_idx, to_date, to_low, length, delta, pst, mid):
        self.fig.add_shape(
            type="rect",
            x0=from_date, y0=from_high, x1=to_date, y1=to_low,
            line=dict(
                color="Green",
                width=0.5,
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

        self.fig.add_shape(
            type="line",
            x0=from_date, y0=from_high, x1=to_date, y1=to_low,
            line=dict(
                color="Green",
                width=0.5,
                # dash="dot",
            )
        )

    def build_graph(self):
        self.fig = make_subplots(rows=2, cols=1,
                                 subplot_titles=("candle stick", f"std/mean={self.volume_std_div_volume_mean:.2f}"),
                                 vertical_spacing=0.05,
                                 row_heights=[0.6, 0.4],
                                 shared_xaxes=True,
                                 )

        self.build_candlestick()
        self.build_volume_graph()

        if self.in_precise_view():
            self.add_hline()

        for item in self.up_box:
            self.add_up_box(*item)

        for item in self.down_box:
            self.add_down_box(*item)

        self.fig.update_xaxes(
            rangebreaks=[
                dict(bounds=["sat", "mon"]),  # hide weekends
            ]
        )

        # self.fig.update_xaxes(showspikes=True)
        # self.fig.update_yaxes(showspikes=True)

        from_date = self.stock_df.iloc[0]['Date']
        to_date = self.stock_df.iloc[-1]['Date']

        self.fig.update_layout(
            title=f'{self.stock_name} Period Analysis {from_date} ~ {to_date}',
            xaxis_rangeslider_visible=False,
            hovermode="x unified",
            hoverlabel=dict(
                namelength=200
            )
        )

