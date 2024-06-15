import plotly.graph_objects as go
import pandas as pd
from conf import *
from util import max_between, min_between


class PriceMountainViewDisplay:
    def __init__(self, fig: go.Figure, stock_df: pd.DataFrame):
        self.fig = fig
        self.stock_df = stock_df

        self.x = []
        self.y = []

        self.indices = []

    def step1(self):
        for idx, row in self.stock_df.iterrows():
            local_max_2nd, local_min_2nd = row[local_max_price_2nd], row[local_min_price_2nd]
            high, low, date = row[high_k], row[low_k], row['Date'],

            if local_max_2nd or local_min_2nd:
                self.x.append(date)
                self.y.append(high if local_max_2nd else low)
                self.indices.append(idx)

            if len(self.indices) < 2:
                continue

            prev_idx = self.indices[-2]
            prev_row = self.stock_df.loc[prev_idx]

            if prev_row[local_max_price_2nd] and local_max_2nd:
                min_idx = min_between(self.stock_df, prev_idx + 1, idx - 1)

                min_date = self.stock_df.loc[min_idx]['Date']
                min_low = self.stock_df.loc[min_idx][low_k]

                print(f'insert: min_date={min_date} min_low={min_low}')
                self.x.insert(-1, min_date)
                self.y.insert(-1, min_low)

            elif prev_row[local_min_price_2nd] and local_min_2nd:
                max_idx = max_between(self.stock_df, prev_idx + 1, idx - 1)

                max_date = self.stock_df.loc[max_idx]['Date']
                max_high = self.stock_df.loc[max_idx][high_k]

                print(f'insert: max_date={max_date} max_high={max_high}')
                self.x.insert(-1, max_date)
                self.y.insert(-1, max_high)



    def step2(self):
        self.fig.add_trace(
            go.Scatter(
                name='price mountain view',
                x=self.x,
                y=self.y,
                mode='lines',
                line=dict(width=1, color='black'),
            )
        )

    def build_graph(self):
        self.step1()
        self.step2()
