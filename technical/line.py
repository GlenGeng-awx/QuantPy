import pandas as pd
import plotly.graph_objects as go

from technical.core_banking import CORE_BANKING
from util import get_idx_by_date


def calculate_k(stock_df: pd.DataFrame, date1, date2) -> float:
    x1 = get_idx_by_date(stock_df, date1)
    y1 = stock_df.loc[x1]['close']

    x2 = get_idx_by_date(stock_df, date2)
    y2 = stock_df.loc[x2]['close']

    k = (y2 - y1) / (x2 - x1)
    return k


def calculate_primary_line(stock_df: pd.DataFrame, date1, date2, prev_len, post_len) -> tuple:
    k = calculate_k(stock_df, date1, date2)

    x1 = get_idx_by_date(stock_df, date1)
    y1 = stock_df.loc[x1]['close']

    start_x = x1 - prev_len
    start_date = stock_df.loc[start_x]['Date']
    start_y = y1 - k * prev_len

    x2 = get_idx_by_date(stock_df, date2)
    y2 = stock_df.loc[x2]['close']

    end_x = x2 + post_len
    end_date = stock_df.loc[end_x]['Date']
    end_y = y2 + k * post_len

    return start_date, start_y, end_date, end_y


def calculate_secondary_line(stock_df: pd.DataFrame, date, prev_len, post_len, date1, date2) -> tuple:
    k = calculate_k(stock_df, date1, date2)

    x = get_idx_by_date(stock_df, date)
    y = stock_df.loc[x]['close']

    start_x = x - prev_len
    start_date = stock_df.loc[start_x]['Date']
    start_y = y - k * prev_len

    end_x = x + post_len
    end_date = stock_df.loc[end_x]['Date']
    end_y = y + k * post_len

    return start_date, start_y, end_date, end_y


class Line:
    def __init__(self, stock_df: pd.DataFrame, stock_name: str):
        self.stock_df = stock_df
        self.stock_name = stock_name

        self.primary_lines = []
        self.secondary_lines = []

        for line in CORE_BANKING.get(stock_name, {}).get('lines', []):
            if len(line) == 4:
                self.primary_lines.append(calculate_primary_line(stock_df, *line))
            else:
                self.secondary_lines.append(calculate_secondary_line(stock_df, *line))

    def build_graph(self, fig: go.Figure, enable=False):
        for i, (start_date, start_y, end_date, end_y) in enumerate(self.primary_lines):
            fig.add_trace(
                go.Scatter(
                    name=f'primary line-{i}',
                    x=[start_date, end_date],
                    y=[start_y, end_y],
                    mode='lines',
                    line=dict(width=1, color='red', dash='dash'),
                    visible=None if enable else 'legendonly',
                )
            )

        for i, (start_date, start_y, end_date, end_y) in enumerate(self.secondary_lines):
            fig.add_trace(
                go.Scatter(
                    name=f'secondary line-{i}',
                    x=[start_date, end_date],
                    y=[start_y, end_y],
                    mode='lines',
                    line=dict(width=1, color='green', dash='dash'),
                    visible=None if enable else 'legendonly',
                )
            )
