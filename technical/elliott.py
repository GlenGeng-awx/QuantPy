import pandas as pd
import plotly.graph_objects as go

from technical import plot_tags
from trading.core_banking import CORE_BANKING
from util import shrink_date_str


# return (x, y, text)
def calculate_elliott(stock_df: pd.DataFrame, stock_name: str, yaxis_type: str) -> (list, list, list):
    # date, price, text
    x, y, text = [], [], []

    for date, tags in CORE_BANKING.get(stock_name, {}).get('elliott', {}).items():
        if date not in stock_df['Date'].iloc[1:].apply(shrink_date_str).values:
            print(f'elliott {stock_name} {date} is out of range')
            continue

        x_, y_, text_ = plot_tags(stock_df, stock_name, yaxis_type, date, tags)

        x.append(x_)
        y.append(y_)
        text.append(text_)

    return x, y, text


class Elliott:
    def __init__(self, stock_df: pd.DataFrame, stock_name: str, yaxis_type: str):
        self.stock_df = stock_df
        self.stock_name = stock_name
        self.yaxis_type = yaxis_type

        self.x = []
        self.y = []
        self.text = []

        self.x, self.y, self.text = calculate_elliott(self.stock_df, self.stock_name, self.yaxis_type)

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
