import pandas as pd
import plotly.graph_objects as go

from technical.min_max import LOCAL_MAX_PRICE_1ST, LOCAL_MIN_PRICE_1ST
from trading.core_banking import CORE_BANKING
from util import get_idx_by_date, shrink_date_str


# for linear
def _get_diff(stock_df: pd.DataFrame, _date):
    max_close = stock_df['close'].max()
    min_close = stock_df['close'].min()
    return (max_close - min_close) / 20


# for log
def get_diff(stock_df: pd.DataFrame, date):
    max_close = stock_df['close'].max()
    min_close = stock_df['close'].min()
    ratio = min(max_close / min_close / 40, 0.15)

    idx = get_idx_by_date(stock_df, date)
    close = stock_df.loc[idx]['close']
    return close * ratio


# return (x, y, text)
def plot_tags(stock_df: pd.DataFrame, stock_name,
              date, tags: list, diff: float) -> (str, float, str):
    idx = get_idx_by_date(stock_df, date)
    close = stock_df.loc[idx]['close']

    diff_ = diff
    if len(tags) == 2:
        diff_ = diff * 1.25
    elif len(tags) == 3:
        diff_ = diff * 1.5
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
def calculate_elliott(stock_df: pd.DataFrame, stock_name: str) -> ((list, list, list), (list, list, list)):
    # date, price, text
    x, y, text = [], [], []
    x1, y1, text1 = [], [], []

    for date, tags in CORE_BANKING.get(stock_name, {}).get('elliott', {}).items():
        if date not in stock_df['Date'].apply(shrink_date_str).values:
            print(f'elliott {stock_name} {date} is out of range')
            continue

        diff = get_diff(stock_df, date)
        x_, y_, text_ = plot_tags(stock_df, stock_name, date, tags, diff)

        x.append(x_)
        y.append(y_)
        text.append(text_)

        x1_, y1_, text1_ = plot_tags(stock_df, stock_name, date, [tags[0]], diff)

        x1.append(x1_)
        y1.append(y1_)
        text1.append(text1_)

    return (x, y, text), (x1, y1, text1)


class Elliott:
    def __init__(self, stock_df: pd.DataFrame, stock_name: str):
        self.stock_df = stock_df
        self.stock_name = stock_name

        self.x = []
        self.y = []
        self.text = []

        self.x1 = []
        self.y1 = []
        self.text1 = []

        (self.x, self.y, self.text), (self.x1, self.y1, self.text1) = calculate_elliott(self.stock_df, self.stock_name)

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

        fig.add_trace(
            go.Scatter(
                name='elliott 1',
                x=self.x1, y=self.y1, text=self.text1,
                mode='text', textfont=dict(color="black", size=size),
                visible='legendonly',
            )
        )
