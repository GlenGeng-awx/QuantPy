import pandas as pd
import plotly.graph_objects as go

from technical.gap import Gap
from trading.core_banking import CORE_BANKING
from util import shrink_date_str, get_idx_by_date

VOLUME = 'volume'
VOLUME_REG = 'volume_reg'


class Volume:
    def __init__(self, stock_df: pd.DataFrame, stock_name: str):
        self.stock_df = stock_df
        self.stock_name = stock_name

        self.volume_avg = self.stock_df[VOLUME].mean()

        volume_peak = self.volume_avg * 4
        self.volume_reg = self.stock_df[VOLUME].apply(
            lambda vol: vol if vol < volume_peak else volume_peak + (vol - volume_peak) / 10)

        self.stock_df[VOLUME_REG] = self.volume_reg

    def add_tech(self, fig: go.Figure, row):
        # date, volume, tags
        x, y, text = [], [], []

        for date, tags in CORE_BANKING.get(self.stock_name, {}).get('tech', {}).items():
            if date not in self.stock_df['Date'].apply(shrink_date_str).values:
                continue

            x.append(date)

            idx = get_idx_by_date(self.stock_df, date)
            vol = self.volume_reg.loc[idx]
            y.append(vol)

            text.append('<br>'.join(tags))

        fig.add_trace(
            go.Scatter(
                name='vol tech',
                x=x, y=y, text=text,
                mode='text', textfont=dict(color="red", size=12),
                visible=None,
            ),
            row=row, col=1
        )

    def add_gap(self, fig: go.Figure, gap: Gap, row):
        up_x, up_y, up_text = [], [], []
        for idx, pst in gap.up_gaps:
            up_x.append(self.stock_df['Date'][idx])
            up_y.append(self.volume_reg[idx])
            up_text.append(f'{pst:.2%}')

        down_x, down_y, down_text = [], [], []
        for idx, pst in gap.down_gaps:
            down_x.append(self.stock_df['Date'][idx])
            down_y.append(self.volume_reg[idx])
            down_text.append(f'{pst:.2%}')

        fig.add_trace(
            go.Scatter(
                name='vol up gap',
                x=up_x, y=up_y, text=up_text,
                mode='text', textfont=dict(color="red", size=10),
                visible='legendonly',
            ),
            row=row, col=1
        )

        fig.add_trace(
            go.Scatter(
                name='vol down gap',
                x=down_x, y=down_y, text=down_text,
                mode='text', textfont=dict(color="green", size=10),
                visible='legendonly',
            ),
            row=row, col=1
        )

    def build_graph(self,
                    fig: go.Figure,
                    gap: Gap,
                    enable_volume=(False, 2),
                    ):
        enable, row = enable_volume

        fig.add_trace(
            go.Bar(
                name=VOLUME_REG,
                x=self.stock_df['Date'],
                y=self.volume_reg,
                marker_color='blue',
                opacity=0.5,
            ),
            row=row, col=1
        )

        fig.add_hline(
            y=self.volume_avg,
            line_dash='dot', line_color='black', line_width=0.5,
            row=row, col=1
        )

        if self.volume_reg.max() >= self.volume_avg * 4:
            fig.add_hline(
                y=self.volume_avg * 4,
                line_dash='dot', line_color='black', line_width=0.75,
                row=row, col=1
            )

        self.add_tech(fig, row)
        self.add_gap(fig, gap, row)
