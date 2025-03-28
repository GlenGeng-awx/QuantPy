import pandas as pd
import plotly.graph_objects as go
from trading.core_banking import CORE_BANKING
from util import shrink_date_str, get_idx_by_date

VOLUME = 'volume'
VOLUME_REG = 'volume_reg'

VOLUME_MA_5 = 'volume_ma_5'
VOLUME_MA_15 = 'volume_ma_15'
VOLUME_MA_30 = 'volume_ma_30'
VOLUME_MA_60 = 'volume_ma_60'


# return (x, y, text)
def calculate_tech_annot(stock_df: pd.DataFrame, stock_name: str, volume_reg: pd.Series) -> (list, list, list):
    # date, volume, tags
    x, y, text = [], [], []

    for date, tags in CORE_BANKING.get(stock_name, {}).get('elliott', {}).items():
        if date not in stock_df['Date'].apply(shrink_date_str).values:
            print(f'volume {stock_name} {date} is out of range')
            continue
        x.append(date)

        idx = get_idx_by_date(stock_df, date)
        vol = volume_reg.loc[idx]
        y.append(vol)

        tags = [tag for tag in tags if tag in ['S', 'H']]
        if not tags:
            continue
        text.append('<br>'.join(reversed(tags)))

    return x, y, text


class Volume:
    def __init__(self, stock_df: pd.DataFrame, stock_name: str):
        self.stock_df = stock_df

        volume = stock_df[VOLUME]

        stock_df[VOLUME_MA_5] = volume.rolling(window=5).mean()
        stock_df[VOLUME_MA_15] = volume.rolling(window=15).mean()
        stock_df[VOLUME_MA_30] = volume.rolling(window=30).mean()
        stock_df[VOLUME_MA_60] = volume.rolling(window=60).mean()

        volume_peak = self.stock_df[VOLUME].mean() * 4
        self.volume_reg = self.stock_df[VOLUME].apply(lambda x: x if x < volume_peak else volume_peak)

        self.x, self.y, self.text = calculate_tech_annot(stock_df, stock_name, self.volume_reg)

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

    def build_graph(self,
                    fig: go.Figure,
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

        fig.add_trace(
            go.Scatter(
                name='elliott',
                x=self.x, y=self.y, text=self.text,
                mode='text', textfont=dict(color="red", ),
                visible=None if enable else 'legendonly',
            ),
            row=row, col=1
        )

        self.add_volume_ma(fig, VOLUME_MA_5, 'black', 1, (False, row))
        self.add_volume_ma(fig, VOLUME_MA_15, 'black', 1, (False, row))
        self.add_volume_ma(fig, VOLUME_MA_30, 'black', 1, (False, row))
        self.add_volume_ma(fig, VOLUME_MA_60, 'black', 1, (False, row))
