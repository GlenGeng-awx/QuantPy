import pandas as pd
import plotly.graph_objects as go

from technical.min_max import LOCAL_MAX_PRICE_1ST, LOCAL_MIN_PRICE_1ST
from trading.core_banking import CORE_BANKING
from util import get_idx_by_date, shrink_date_str


# return (x, y, text)
# text: Brk
def plot_brk(stock_df: pd.DataFrame, date, text) -> (str, float, str):
    idx = get_idx_by_date(stock_df, date)
    close = stock_df['close']
    return date, close[idx], text


# return (x, y, text)
# text: G, EG, RG, BG
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


def get_diff(stock_df: pd.DataFrame):
    max_close = stock_df['close'].max()
    min_close = stock_df['close'].min()
    return (max_close - min_close) / 20


# return (x, y, text)
def plot_others(stock_df: pd.DataFrame, stock_name,
                date, tags: list, diff: float) -> (str, float, str):
    idx = get_idx_by_date(stock_df, date)
    close = stock_df.loc[idx]['close']

    diff_ = diff
    if len(tags) == 2:
        diff_ = diff * 1.5
    elif len(tags) == 3:
        diff_ = diff * 1.75
    elif len(tags) == 4:
        diff_ = diff * 2

    if stock_df.loc[idx][LOCAL_MAX_PRICE_1ST]:
        y = close + diff_ * 0.9
        text = '<br>'.join(reversed(tags))
    elif stock_df.loc[idx][LOCAL_MIN_PRICE_1ST]:
        y = close - diff_
        text = '<br>'.join(tags)
    else:
        print(f'invalid elliott {stock_name} {date} {tags}')
        raise ValueError

    return date, y, text


# return (x, y, text)
def calculate_elliott(stock_df: pd.DataFrame, stock_name: str) -> (list, list, list):
    diff = get_diff(stock_df)
    print(f'elliott diff {diff}')

    # date, price, text
    x, y, text = [], [], []

    for date, tags in CORE_BANKING.get(stock_name, {}).get('elliott', {}).items():
        if date not in stock_df['Date'].apply(shrink_date_str).values:
            print(f'elliott {stock_name} {date} is out of range')
            continue

        tags = list(tags)

        if 'Brk' in tags:
            tags.remove('Brk')
            x_, y_, text_ = plot_brk(stock_df, date, 'Brk')

            x.append(x_)
            y.append(y_)
            text.append(text_)

        for tag in ['G', 'EG', 'RG', 'BG']:
            if tag in tags:
                tags.remove(tag)
                x_, y_, text_ = plot_gap(stock_df, date, tag)

                x.append(x_)
                y.append(y_)
                text.append(text_)

        if tags:
            x_, y_, text_ = plot_others(stock_df, stock_name, date, tags, diff)

            x.append(x_)
            y.append(y_)
            text.append(text_)

    return x, y, text


class Elliott:
    def __init__(self, stock_df: pd.DataFrame, stock_name: str):
        self.stock_df = stock_df
        self.stock_name = stock_name

        self.x = []
        self.y = []
        self.text = []

        self.x, self.y, self.text = calculate_elliott(self.stock_df, self.stock_name)

    def build_graph(self, fig: go.Figure, enable=False):
        size = 13 if self.stock_df.shape[0] <= 550 else 14

        fig.add_trace(
            go.Scatter(
                name='elliott',
                x=self.x, y=self.y, text=self.text,
                mode='text', textfont=dict(color="black", size=size),
                visible=None if enable else 'legendonly',
            )
        )
