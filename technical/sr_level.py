import pandas as pd
import plotly.graph_objects as go

SR_LEVEL = 'sr_level'
SIZE = 20


def calculate_sr_level(stock_df: pd.DataFrame):
    indices = []

    close = stock_df['close']

    for idx in close.index[SIZE:-SIZE]:
        if close.loc[idx - SIZE:idx + SIZE].idxmax() == idx:
            indices.append(idx)

        if close.loc[idx - SIZE:idx + SIZE].idxmin() == idx:
            indices.append(idx)

    return pd.Series([True] * len(indices), index=indices)


class SupportResistanceLevel:
    def __init__(self, stock_df: pd.DataFrame):
        self.stock_df = stock_df

        stock_df[SR_LEVEL] = calculate_sr_level(stock_df).reindex(stock_df.index, fill_value=False)

    def build_graph(self, fig: go.Figure, enable=False):
        sr_level = self.stock_df[self.stock_df[SR_LEVEL]]

        dates = []
        prices = []

        for idx in sr_level.index:
            date0 = self.stock_df.loc[idx - 10]['Date']
            date1 = self.stock_df.loc[idx + 10]['Date']
            price = self.stock_df.loc[idx]['close']

            dates.extend([date0, date1, None])
            prices.extend([price, price, None])

        fig.add_trace(
            go.Scatter(
                name='sr level',
                x=dates,
                y=prices,
                mode='lines',
                line=dict(width=1, color='blue', dash='dot'),
                visible=None if enable else 'legendonly',
            )
        )
