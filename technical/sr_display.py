import pandas as pd
import plotly.graph_objects as go
from conf import local_min_price_3rd, local_max_price_3rd, local_min_price_4th, local_max_price_4th


class SupportResistanceDisplay:
    def __init__(self, fig: go.Figure, interval, stock_df: pd.DataFrame):
        self.fig = fig
        self.interval = interval
        self.stock_df = stock_df

        self.start_date = stock_df['Date'].iloc[0]
        self.end_date = stock_df['Date'].iloc[-1]

    def build_graph_impl(self, condition: pd.Series, name: str, color: str, enable=False):
        x = []
        y = []

        for _, row in self.stock_df[condition].iterrows():
            x.extend([self.start_date, self.end_date, None])
            y.extend([row['close'], row['close'], None])

        self.fig.add_trace(
            go.Scatter(
                name=name,
                x=x,
                y=y,
                mode='lines',
                line=dict(width=0.75, color=color),
                visible=None if enable else 'legendonly',
            )
        )

    def build_graph(self, enable=False):
        self.build_graph_impl(self.stock_df[local_min_price_3rd], 'support levels - 3rd', 'green',
                              True if enable and self.interval == '1d' else False)
        self.build_graph_impl(self.stock_df[local_max_price_3rd], 'resistance levels - 3rd', 'red',
                              True if enable and self.interval == '1d' else False)

        self.build_graph_impl(self.stock_df[local_min_price_4th], 'support levels - 4th', 'green',
                              True if enable and self.interval == '1h' else False)
        self.build_graph_impl(self.stock_df[local_max_price_4th], 'resistance levels - 4th', 'red',
                              True if enable and self.interval == '1h' else False)