import pandas as pd
import plotly.graph_objects as go

from technical.core_banking import CORE_BANKING
from util import get_idx_by_date


def calculate_sr_level(stock_df: pd.DataFrame, date, prev_len, post_len) -> tuple:
    x = get_idx_by_date(stock_df, date)
    y = stock_df.loc[x]['close']

    x1 = x - prev_len
    date1 = stock_df.loc[x1]['Date']

    x2 = x + post_len
    date2 = stock_df.loc[x2]['Date']

    return date1, date2, y


class SupportResistanceLevel:
    def __init__(self, stock_df: pd.DataFrame, stock_name: str):
        self.stock_df = stock_df
        self.stock_name = stock_name

        self.sr_levels = []

        for sr_level in CORE_BANKING.get(stock_name, {}).get('sr_levels', []):
            date1, date2, y = calculate_sr_level(stock_df, *sr_level)
            self.sr_levels.append((date1, date2, y))

    def build_graph(self, fig: go.Figure, enable=False):
        for i, (date1, date2, y) in enumerate(self.sr_levels):
            fig.add_trace(
                go.Scatter(
                    name=f'sr level-{i}',
                    x=[date1, date2],
                    y=[y, y],
                    mode='lines',
                    line=dict(width=1, color='blue', dash='dash'),
                    visible=None if enable else 'legendonly',
                )
            )
