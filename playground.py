import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

from conf import *
from base_engine import BaseEngine
from statistical.bband import BBAND_MID

STOCK_NAMES_INDEX = [
    IXIC,
    SS_000300,
    SS_000001,
    GC_F,
]

STOCK_NAMES_TIER_0 = [
    # IXIC,
    # SS_000001,
    # SS_000300,
    TSLA,
    # META,
    # HK_0700,
    MRNA,
    # BILI,
    XPEV,
    # CPNG,
    # SNOW,
    IQ,
    # JD,
    BEKE,
    # RIVN,
    # MNSO,
    # ZM,
    # BABA,
    # BA,
    # PDD,
    FUTU,
    COIN,
]

STOCK_NAMES_TIER_1 = [
    PDD,
    JD,
    BEKE,
    HK_0700,
    NVDA,
    AMD,
    BNTX,
    CPNG,
    TSM,
    EBAY,
    IXIC,
    SS_000001,
    TSLA,
    COIN,
    XPEV,
    MRNA,
    SNOW,
    IQ,
    PLTR,
    RIVN,
    META,
    MNSO,
    ZM,
    BABA,
    EDU,
    BA,
    BILI,
    LI,
    SNAP,
]


def default_period():
    current_date = datetime.now()

    date_0y_ago = datetime(current_date.year, 1, 1).strftime('%Y-%m-%d')
    date_1y_ago = datetime(current_date.year - 1, 1, 1).strftime('%Y-%m-%d')
    date_5y_ago = datetime(current_date.year - 5, 1, 1).strftime('%Y-%m-%d')

    current_date = current_date.strftime('%Y-%m-%d')

    return [
        # (date_0y_ago, current_date, '1h'),
        (date_1y_ago, current_date, '1d'),
        # (date_5y_ago, current_date, '1wk'),
    ]


def get_period(_stock_name):
    return default_period()


TREND = 'bband_trend'
LONG = 'long'
SHORT = 'short'


class Playground:
    def __init__(self, stock_df: pd.DataFrame):
        self.stock_df = stock_df
        self.initial_drop = 30

        self.stock_df[TREND] = self.analyze_trend()
        self.stock_df[LONG] = self.analyze_long()
        self.stock_df[SHORT] = self.analyze_short()

    def _is_up_trend(self, as_of_idx) -> bool:
        # [as_of_idx - retention + 1, as_of_idx]
        retention = 2
        s = self.stock_df[BBAND_MID].loc[as_of_idx - retention + 1:as_of_idx]
        print(f'{as_of_idx} {s}')
        return (s.diff().dropna() > 0).all()

    def _is_down_trend(self, as_of_idx) -> bool:
        # [as_of_idx - retention + 1, as_of_idx]
        retention = 2
        s = self.stock_df[BBAND_MID].loc[as_of_idx - retention + 1:as_of_idx]
        return (s.diff().dropna() < 0).all()

    def analyze_trend(self) -> pd.Series:
        trend = []
        indices = []

        for idx in self.stock_df.index[self.initial_drop:]:
            indices.append(idx)
            if self._is_up_trend(idx):
                trend.append('up')
            elif self._is_down_trend(idx):
                trend.append('down')
            else:
                trend.append('swing')

        return pd.Series(trend, index=indices)

    def analyze_long(self) -> pd.Series:
        indices = []
        prices = []

        for idx in self.stock_df.index[self.initial_drop:]:
            row = self.stock_df.loc[idx]
            prev_row = self.stock_df.loc[idx - 1]
            prev_2nd_row = self.stock_df.loc[idx - 2]
            pass

        return pd.Series(prices, index=indices)

    def analyze_short(self) -> pd.Series:
        indices = []
        prices = []

        for idx in self.stock_df.index[self.initial_drop:]:
            row = self.stock_df.loc[idx]
            prev_row = self.stock_df.loc[idx - 1]
            prev_2nd_row = self.stock_df.loc[idx - 2]
            pass

        return pd.Series(prices, index=indices)

    def _build_graph_for_trend(self, fig: go.Figure):
        index = self.stock_df[stock_df[TREND] == 'up'].index
        x = self.stock_df.loc[index]['Date']
        y = self.stock_df.loc[index][BBAND_MID]

        fig.add_trace(
            go.Scatter(
                name=f'up trend',
                x=x,
                y=y,
                mode="markers",
                marker=dict(size=2, color='red'),
            )
        )

        index = self.stock_df[stock_df[TREND] == 'down'].index
        x = self.stock_df.loc[index]['Date']
        y = self.stock_df.loc[index][BBAND_MID]

        fig.add_trace(
            go.Scatter(
                name=f'down trend',
                x=x,
                y=y,
                mode="markers",
                marker=dict(size=2, color='green'),
            )
        )

        index = self.stock_df[stock_df[TREND] == 'swing'].index
        x = self.stock_df.loc[index]['Date']
        y = self.stock_df.loc[index][BBAND_MID]

        fig.add_trace(
            go.Scatter(
                name=f'swing trend',
                x=x,
                y=y,
                mode="markers",
                marker=dict(size=2, color='blue'),
            )
        )

    def _build_graph_for_long(self, fig: go.Figure):
        index = self.stock_df[stock_df[LONG] > 0].index
        x = self.stock_df.loc[index]['Date']
        y = self.stock_df.loc[index][LONG]

        fig.add_trace(
            go.Scatter(
                name=f'long',
                x=x,
                y=y,
                mode="markers",
                marker=dict(size=6, color='orange'),
            )
        )

    def _build_graph_for_short(self, fig: go.Figure):
        index = self.stock_df[stock_df[SHORT] > 0].index
        x = self.stock_df.loc[index]['Date']
        y = self.stock_df.loc[index][SHORT]

        fig.add_trace(
            go.Scatter(
                name=f'short',
                x=x,
                y=y,
                mode="markers",
                marker=dict(size=6, color='purple'),
            )
        )

    def build_graph(self, fig: go.Figure):
        self._build_graph_for_trend(fig)
        # self._build_graph_for_long(fig)
        # self._build_graph_for_short(fig)


for stock_name in STOCK_NAMES_TIER_0:
    for (start_date, end_date, interval) in get_period(stock_name):
        de = BaseEngine(stock_name, start_date, end_date, interval)
        de.build_graph(
                       # enable_close_price=True,
                       enable_volume_reg=True,
                       # enable_macd=True,
                       # enable_macd=True,
                       # enable_bband=True,
                       # enable_ema=True,
                       # enable_sr=True,
                       # enable_min_max=True
                       )

        stock_df, fig = de.stock_df, de.fig
        Playground(stock_df).build_graph(fig)

        de.display()
