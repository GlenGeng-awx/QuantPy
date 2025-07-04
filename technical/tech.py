import pandas as pd
import plotly.graph_objects as go

from technical import plot_tags
from core_banking import CORE_BANKING
from util import get_idx_by_date, shrink_date_str


# return (x, y, text)
# text: B, B3, A, M
def plot_close(stock_df: pd.DataFrame, date, text) -> (str, float, str):
    idx = get_idx_by_date(stock_df, date)
    close = stock_df['close']
    return date, close[idx], text


# return (x, y, text)
# text: G, BG, RG, EG
def plot_gap(stock_df: pd.DataFrame, date, text) -> (str, float, str):
    idx = get_idx_by_date(stock_df, date)

    high = stock_df['high']
    low = stock_df['low']
    close = stock_df['close']

    if close[idx] > close[idx - 1]:
        y = (low[idx] + high[idx - 1]) / 2
    else:
        y = (high[idx] + low[idx - 1]) / 2

    return date, y, text


# return (x, y, text)
def calculate_tech(stock_df: pd.DataFrame, stock_name: str, yaxis_type: str) -> (list, list, list):
    # date, price, text
    x, y, text = [], [], []

    for date, tags in CORE_BANKING.get(stock_name, {}).get('tech', {}).items():
        if date not in stock_df['Date'].apply(shrink_date_str).values:
            print(f'tech {stock_name} {date} is out of range')
            continue

        tags = list(tags)

        for tag in ['A', 'B', 'B3', 'M']:
            if tag in tags:
                tags.remove(tag)
                x_, y_, text_ = plot_close(stock_df, date, tag)

                x.append(x_)
                y.append(y_)
                text.append(text_)

        for tag in ['G', 'BG', 'RG', 'EG']:
            if tag in tags:
                tags.remove(tag)
                x_, y_, text_ = plot_gap(stock_df, date, tag)

                x.append(x_)
                y.append(y_)
                text.append(text_)

        if tags:
            x_, y_, text_ = plot_tags(stock_df, stock_name, yaxis_type, date, tags)

            x.append(x_)
            y.append(y_)
            text.append(text_)

    return x, y, text


class Tech:
    def __init__(self, stock_df: pd.DataFrame, stock_name: str, yaxis_type: str):
        self.stock_df = stock_df
        self.stock_name = stock_name
        self.yaxis_type = yaxis_type

        self.x = []
        self.y = []
        self.text = []

        self.x, self.y, self.text = calculate_tech(self.stock_df, self.stock_name, self.yaxis_type)

    def build_graph(self, fig: go.Figure, enable=False):
        size = 13 if self.stock_df.shape[0] <= 550 else 12

        fig.add_trace(
            go.Scatter(
                name='tech',
                x=self.x, y=self.y, text=self.text,
                mode='text', textfont=dict(color="BLue", size=size),
                visible=None if enable else 'legendonly',
            )
        )
