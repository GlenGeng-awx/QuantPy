import plotly.graph_objects as go
import pandas as pd
from conf import *


class PriceMountainViewDisplay:
    def __init__(self, fig: go.Figure, stock_df: pd.DataFrame):
        self.fig = fig
        self.stock_df = stock_df

    def build_graph(self):
        x, y = [], []

        for idx, row in self.stock_df.iterrows():
            local_max_1st, local_min_1st = row[local_max_price_1st], row[local_min_price_1st]
            local_max_2nd, local_min_2nd = row[local_max_price_2nd], row[local_min_price_2nd]
            high, low, date = row['high'], row['low'], row['Date'],

            # if local_max_2nd or local_min_2nd:
            #     x.append(date)
            #     y.append(high if local_max_2nd else low)

            if local_max_2nd:
                x.append(date)
                y.append(high)

            if local_min_2nd:
                x.append(date)
                y.append(low)

        self.fig.add_trace(
            go.Scatter(
                name='price mountain view',
                x=x,
                y=y,
                mode='lines',
                line=dict(width=1, color='black'),
            )
        )
