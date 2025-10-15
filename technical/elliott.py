import pandas as pd
import plotly.graph_objects as go

from technical import get_diff
from technical.min_max import LOCAL_MAX_PRICE_1ST, LOCAL_MIN_PRICE_1ST
from util import shrink_date_str, get_idx_by_date
from core_banking import CORE_BANKING


# return (x, y, text)
def plot_tags(stock_df: pd.DataFrame,
              stock_name,
              date: str,
              tags: list) -> (str, float, str):
    idx = get_idx_by_date(stock_df, date)
    close = stock_df.loc[idx]['close']

    diff = get_diff(stock_df, date)

    diff_ = diff
    if len(tags) == 2:
        diff_ = diff * 1.25
    if len(tags) == 3:
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
    # date, price, text
    x, y, text = [], [], []

    for date, tags in CORE_BANKING.get(stock_name, {}).get('elliott', {}).items():
        if date not in stock_df['Date'].iloc[1:-1].apply(shrink_date_str).values:
            print(f'elliott {stock_name} {date} is out of range')
            continue

        x_, y_, text_ = plot_tags(stock_df, stock_name, date, tags)

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
