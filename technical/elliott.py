import pandas as pd
import plotly.graph_objects as go

from technical.min_max import LOCAL_MAX_PRICE_1ST, LOCAL_MIN_PRICE_1ST
from trading.core_banking import CORE_BANKING
from util import get_idx_by_date, shrink_date_str


def get_diff(stock_df: pd.DataFrame):
    max_close = stock_df['close'].max()
    min_close = stock_df['close'].min()
    return (max_close - min_close) / 20


# return (x, y, text)
def calculate_elliott(stock_df: pd.DataFrame, stock_name: str) -> (list, list, list):
    diff = get_diff(stock_df)
    print(f'elliott diff {diff}')

    # date, close +/- diff, tags
    x, y, text = [], [], []

    for date, tags in CORE_BANKING.get(stock_name, {}).get('elliott', {}).items():
        if date not in stock_df['Date'].apply(shrink_date_str).values:
            print(f'elliott {stock_name} {date} is out of range')
            continue

        x.append(date)

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
            y.append(close + diff_ * 0.9)
            text.append('<br>'.join(reversed(tags)))
        elif stock_df.loc[idx][LOCAL_MIN_PRICE_1ST]:
            y.append(close - diff_)
            text.append('<br>'.join(tags))
        else:
            print(f'invalid elliott {stock_name} {date} {tags}')

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
        fig.add_trace(
            go.Scatter(
                name='elliott',
                x=self.x, y=self.y, text=self.text,
                mode='text', textfont=dict(color="black",),
                visible=None if enable else 'legendonly',
            )
        )
