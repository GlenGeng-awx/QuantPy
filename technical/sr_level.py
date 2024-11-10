import pandas as pd
import plotly.graph_objects as go

SR_LEVEL = 'sr_level'
SR_LEVEL_MIN = 'sr_level_min'
SR_LEVEL_MAX = 'sr_level_max'
SIZE = 20


def calculate_sr_level(stock_df: pd.DataFrame):
    indices = []
    min_indices = []
    max_indices = []

    close = stock_df['close']

    for idx in close.index[SIZE:-SIZE]:
        if close.loc[idx - SIZE:idx + SIZE].idxmax() == idx:
            indices.append(idx)
            max_indices.append(idx)

        if close.loc[idx - SIZE:idx + SIZE].idxmin() == idx:
            indices.append(idx)
            min_indices.append(idx)

    stock_df[SR_LEVEL] = pd.Series([True] * len(indices),
                                   index=indices).reindex(stock_df.index, fill_value=False)

    stock_df[SR_LEVEL_MIN] = pd.Series([True] * len(min_indices),
                                       index=min_indices).reindex(stock_df.index, fill_value=False)
    stock_df[SR_LEVEL_MAX] = pd.Series([True] * len(max_indices),
                                       index=max_indices).reindex(stock_df.index, fill_value=False)


class SupportResistanceLevel:
    def __init__(self, stock_df: pd.DataFrame):
        self.stock_df = stock_df
        calculate_sr_level(stock_df)

    def build_graph_impl(self, fig: go.Figure, s: pd.Series, name: str, color: str, enable=False):
        sr_level = self.stock_df[s]

        dates = []
        prices = []

        for idx in sr_level.index:
            date0 = self.stock_df.loc[idx - SIZE]['Date']
            date1 = self.stock_df.loc[idx + SIZE]['Date']
            price = self.stock_df.loc[idx]['close']

            dates.extend([date0, date1, None])
            prices.extend([price, price, None])

        fig.add_trace(
            go.Scatter(
                name=name,
                x=dates,
                y=prices,
                mode='lines',
                line=dict(width=1, color=color, dash='dot'),
                visible=None if enable else 'legendonly',
            )
        )

    def build_graph(self, fig: go.Figure, enable=False):
        self.build_graph_impl(fig, self.stock_df[SR_LEVEL_MIN], 'sr level min', 'green', enable)
        self.build_graph_impl(fig, self.stock_df[SR_LEVEL_MAX], 'sr level max', 'red', enable)
