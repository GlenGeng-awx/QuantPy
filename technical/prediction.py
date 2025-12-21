import pandas as pd
import plotly.graph_objects as go
import os
from guru_wizard import PREDICT_MODE
from util import touch_file, shrink_date_str


def dump_prediction(stock_name: str, date: str, predict_mode: str):
    touch_file(f'model/{predict_mode}/{stock_name}.{date}')


def load_prediction(stock_name: str, date: str) -> list:
    hits = []
    for predict_mode in PREDICT_MODE:
        if os.path.exists(f'model/{predict_mode}/{stock_name}.{date}'):
            hits.append(predict_mode)
    return hits


class Prediction:
    def __init__(self, stock_name: str, stock_df: pd.DataFrame):
        self.dates = []
        self.prices = []

        for idx in stock_df.index[-200:]:
            date = shrink_date_str(stock_df.loc[idx]['Date'])
            close = stock_df.loc[idx]['close']

            if load_prediction(stock_name, date):
                self.dates.append(date)
                self.prices.append(close)

        print(f'Prediction: loaded {len(self.dates)} points for {stock_name}')

    def build_graph(self, fig: go.Figure, enable=False):
        fig.add_trace(
            go.Scatter(
                name='prediction', x=self.dates, y=self.prices,
                mode='markers', marker=dict(color='blue', size=5),
                visible=None if enable else 'legendonly',
            )
        )
