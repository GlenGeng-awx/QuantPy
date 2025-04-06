import pandas as pd
import plotly.graph_objects as go

from technical.gap import Gap
from trading.core_banking import CORE_BANKING
from util import shrink_date_str, get_idx_by_date

VOLUME = 'volume'
VOLUME_REG = 'volume_reg'

VOLUME_MA_5 = 'volume_ma_5'
VOLUME_MA_15 = 'volume_ma_15'
VOLUME_MA_30 = 'volume_ma_30'
VOLUME_MA_60 = 'volume_ma_60'


# Only display S, H, H 3%, Brk, Top, Bottom
# return (x, y, text)
def calculate_tech_annot(stock_df: pd.DataFrame, stock_name: str, volume_reg: pd.Series) -> (list, list, list):
    # date, volume, tags
    x, y, text = [], [], []

    for date, tags in CORE_BANKING.get(stock_name, {}).get('elliott', {}).items():
        if date not in stock_df['Date'].apply(shrink_date_str).values:
            print(f'volume {stock_name} {date} is out of range')
            continue

        tags = [tag for tag in tags if tag in ['S', 'H', 'H 3%', 'Brk', 'Top', 'Bottom']]
        if not tags:
            continue

        x.append(date)

        idx = get_idx_by_date(stock_df, date)
        vol = volume_reg.loc[idx]
        y.append(vol)

        text.append('<br>'.join(reversed(tags)))
    return x, y, text


class Volume:
    def __init__(self, stock_df: pd.DataFrame, stock_name: str):
        self.stock_df = stock_df
        self.stock_name = stock_name

        volume = stock_df[VOLUME]

        stock_df[VOLUME_MA_5] = volume.rolling(window=5).mean()
        stock_df[VOLUME_MA_15] = volume.rolling(window=15).mean()
        stock_df[VOLUME_MA_30] = volume.rolling(window=30).mean()
        stock_df[VOLUME_MA_60] = volume.rolling(window=60).mean()

        volume_peak = self.stock_df[VOLUME].mean() * 4
        self.volume_reg = self.stock_df[VOLUME].apply(lambda x: x if x < volume_peak else volume_peak)

    def add_volume_ma(self, fig: go.Figure, ma_type: str,
                      color: str, size: float, enable_ma=(False, 2)):
        enable, row = enable_ma
        fig.add_trace(
            go.Scatter(
                name=ma_type,
                x=self.stock_df['Date'],
                y=self.stock_df[ma_type],
                mode='lines',
                line=dict(width=size, color=color),
                visible=None if enable else 'legendonly',
            ),
            row=row, col=1
        )

    def add_elliott(self, fig: go.Figure, row):
        x, y, text = calculate_tech_annot(self.stock_df, self.stock_name, self.volume_reg)

        fig.add_trace(
            go.Scatter(
                name='vol elliott',
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
                name=VOLUME,
                x=self.stock_df['Date'],
                y=self.volume_reg,
                marker_color='blue',
                opacity=0.5,
            ),
            row=row, col=1
        )

        self.add_elliott(fig, row)
        self.add_gap(fig, gap, row)

        self.add_volume_ma(fig, VOLUME_MA_5, 'black', 1, (False, row))
        self.add_volume_ma(fig, VOLUME_MA_15, 'black', 1, (False, row))
        self.add_volume_ma(fig, VOLUME_MA_30, 'black', 1, (False, row))
        self.add_volume_ma(fig, VOLUME_MA_60, 'black', 1, (False, row))
