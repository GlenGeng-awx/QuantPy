import pandas as pd
import plotly.graph_objects as go

from .wave import Wave
from util import interval_to_label


class BoxImpl:
    def __init__(self, stock_df: pd.DataFrame, wave_idx: list, interval: str, label: str):
        self.stock_df = stock_df
        self.wave_idx = wave_idx

        self.interval = interval
        self.label = label

        # [(from_idx, from_date, from_low, to_idx, to_date, to_high, length, delta, pst, mid), ...]
        self.up_box = []
        # [(from_idx, from_date, from_high, to_idx, to_date, to_low, length, delta, pst, mid), ...]
        self.down_box = []

        self.x_of_up_box = []
        self.y_of_up_box = []

        self.x_of_up_text = []
        self.y_of_up_text = []
        self.up_text = []

        self.x_of_down_box = []
        self.y_of_down_box = []

        self.x_of_down_text = []
        self.y_of_down_text = []
        self.down_text = []

        for idx in range(len(self.wave_idx) - 1):
            from_idx, to_idx = self.wave_idx[idx], self.wave_idx[idx + 1]
            self.fill_box(from_idx, to_idx)

        for item in self.up_box:
            self.add_up_box(*item)

        for item in self.down_box:
            self.add_down_box(*item)

    def fill_box(self, from_idx, to_idx):
        from_date = self.stock_df.loc[from_idx]['Date']
        from_price = self.stock_df.loc[from_idx]['close']

        to_date = self.stock_df.loc[to_idx]['Date']
        to_price = self.stock_df.loc[to_idx]['close']

        length = to_idx - from_idx
        mid = (from_price + to_price) / 2

        if from_price < to_price:
            delta = to_price - from_price
            pst = 100 * delta / from_price
            self.up_box.append((from_idx, from_date, from_price, to_idx, to_date, to_price, length, delta, pst, mid))
        else:
            delta = from_price - to_price
            pst = 100 * delta / from_price
            self.down_box.append((from_idx, from_date, from_price, to_idx, to_date, to_price, length, delta, pst, mid))

    def add_up_box(self, from_idx, from_date, from_low, to_idx, to_date, to_high, length, delta, pst, mid):
        # box
        self.x_of_up_box.extend([from_date, from_date, to_date, to_date, from_date, None])
        self.y_of_up_box.extend([from_low, to_high, to_high, from_low, from_low, None])

        # middle line
        self.x_of_up_box.extend([from_date, to_date, None])
        self.y_of_up_box.extend([mid, mid, None])

        # trend line
        self.x_of_up_box.extend([from_date, to_date, None])
        self.y_of_up_box.extend([from_low, to_high, None])

        # label
        x = self.stock_df.loc[(from_idx + to_idx) // 2]['Date']
        y = from_low
        text = f'{length}{interval_to_label(self.interval, abbr=True)} <br> {delta:.2f}$ <br> +{pst:.2f}%'

        self.x_of_up_text.append(x)
        self.y_of_up_text.append(y)
        self.up_text.append(text)

    def add_down_box(self, from_idx, from_date, from_high, to_idx, to_date, to_low, length, delta, pst, mid):
        # box
        self.x_of_down_box.extend([from_date, to_date, to_date, from_date, from_date, None])
        self.y_of_down_box.extend([from_high, from_high, to_low, to_low, from_high, None])

        # middle line
        self.x_of_down_box.extend([from_date, to_date, None])
        self.y_of_down_box.extend([mid, mid, None])

        # trend line
        self.x_of_down_box.extend([from_date, to_date, None])
        self.y_of_down_box.extend([from_high, to_low, None])

        # label
        x = self.stock_df.loc[(from_idx + to_idx) // 2]['Date']
        y = from_high
        text = f'-{pst:.2f}% <br> {delta:.2f}$ <br> {length}{interval_to_label(self.interval, abbr=True)}'

        self.x_of_down_text.append(x)
        self.y_of_down_text.append(y)
        self.down_text.append(text)

    def build_graph(self, fig: go.Figure, enable=False):
        fig.add_trace(
            go.Scatter(
                name=f'up box - {self.label}',
                x=self.x_of_up_box,
                y=self.y_of_up_box,
                mode='lines',
                line=dict(width=1, color='red', dash="dot",),
                visible=None if enable else 'legendonly',
            )
        )

        fig.add_trace(
            go.Scatter(
                name=f'up text - {self.label}',
                x=self.x_of_up_text,
                y=self.y_of_up_text,
                text=self.up_text,
                mode="text",
                textfont=dict(
                    color="red",
                ),
                visible='legendonly',
            )
        )

        fig.add_trace(
            go.Scatter(
                name=f'down box - {self.label}',
                x=self.x_of_down_box,
                y=self.y_of_down_box,
                mode='lines',
                line=dict(width=1, color='green', dash="dot",),
                visible=None if enable else 'legendonly',
            )
        )

        fig.add_trace(
            go.Scatter(
                name=f'down text - {self.label}',
                x=self.x_of_down_text,
                y=self.y_of_down_text,
                text=self.down_text,
                mode="text",
                textfont=dict(
                    color="green",
                ),
                visible='legendonly',
            )
        )


class Box:
    def __init__(self, stock_df: pd.DataFrame, wave: Wave):
        self.stock_df = stock_df
        self.wave = wave

    def build_graph(self, fig: go.Figure, interval: str, enable=False):
        # BoxImpl(self.stock_df, self.wave.wave_2nd[0], interval, 'wave_2nd').build_graph(fig)
        BoxImpl(self.stock_df, self.wave.wave_3rd[0], interval, 'wave_3rd').build_graph(fig)
        BoxImpl(self.stock_df, self.wave.wave_4th[0], interval, 'wave_4th').build_graph(fig, enable)
