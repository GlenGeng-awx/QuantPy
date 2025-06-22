import pandas as pd
import plotly.graph_objects as go

from util import get_idx_by_date, get_next_n_workday
from technical import get_date, get_price_key
from technical.line import Line


# date1, date2 is in format of '20210101' or ('20210101', 'open')
def _calculate_k(stock_df: pd.DataFrame, date1, date2) -> float:
    x1 = get_idx_by_date(stock_df, get_date(date1))
    y1 = stock_df.loc[x1][get_price_key(date1)]

    x2 = get_idx_by_date(stock_df, get_date(date2))
    y2 = stock_df.loc[x2][get_price_key(date2)]

    k = (y2 - y1) / (x2 - x1)
    return k


# date is in format of '20210101' or ('20210101', 'open')
def _calculate_point(stock_df: pd.DataFrame, date, delta, k) -> tuple:
    x = get_idx_by_date(stock_df, get_date(date))
    y = stock_df.loc[x][get_price_key(date)]

    target_x = x + delta
    target_y = y + k * delta

    if not stock_df.index[0] <= target_x <= stock_df.index[-1] + 10:
        return ()

    if target_x in stock_df.index:
        target_date = stock_df.loc[target_x]['Date']
    else:
        diff = target_x - stock_df.index[-1]
        last_date = stock_df['Date'].iloc[-1]
        target_date = get_next_n_workday(last_date, diff)

    return target_date, target_y


class LineLinear:
    def __init__(self, stock_df: pd.DataFrame, stock_name: str):
        self.line = Line(
            stock_df, stock_name,
            'lines',
            _calculate_k,
            _calculate_point
        )

    def build_graph(self, fig: go.Figure, enable=False):
        self.line.build_graph(fig, enable)
