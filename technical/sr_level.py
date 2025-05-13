import pandas as pd
import plotly.graph_objects as go

SR_LEVEL_MIN = 'sr level min'
SR_LEVEL_MAX = 'sr level max'
SIZE = 10


def calculate_sr_level(stock_df: pd.DataFrame) -> (list, list):
    min_indices, max_indices = [], []
    close = stock_df['close']

    for idx in close.index[SIZE:-SIZE]:
        if close.loc[idx - SIZE:idx + SIZE].idxmax() == idx:
            max_indices.append(idx)

        if close.loc[idx - SIZE:idx + SIZE].idxmin() == idx:
            min_indices.append(idx)

    return min_indices, max_indices


class SupportResistanceLevel:
    def __init__(self, stock_df: pd.DataFrame):
        self.stock_df = stock_df
        self.min_indices, self.max_indices = calculate_sr_level(stock_df)

    def build_graph_impl(self, fig: go.Figure, indices: list, name: str, color: str, enable=False):
        dates, prices = [], []

        for idx in indices:
            date = self.stock_df.loc[idx]['Date']
            date0 = self.stock_df.loc[idx - SIZE]['Date']
            date1 = self.stock_df.loc[idx + SIZE]['Date']

            price = self.stock_df.loc[idx]['close']

            dates.extend([date0, date, date1, None])
            prices.extend([price, price, price, None])

        fig.add_trace(
            go.Scatter(
                name=name, x=dates, y=prices,
                mode='lines', line=dict(width=1.5, color=color, dash='dot'),
                visible=None if enable else 'legendonly',
            )
        )

    def build_graph(self, fig: go.Figure, enable=False):
        self.build_graph_impl(fig, self.min_indices, SR_LEVEL_MIN, 'green', enable)
        self.build_graph_impl(fig, self.max_indices, SR_LEVEL_MAX, 'red', enable)
