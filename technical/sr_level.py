import pandas as pd
import plotly.graph_objects as go

from .min_max import LOCAL_MIN_PRICE_3RD, LOCAL_MAX_PRICE_3RD, LOCAL_MIN_PRICE_4TH, LOCAL_MAX_PRICE_4TH


def get_close_price(stock_df: pd.DataFrame, condition: pd.Series) -> list:
    return stock_df[condition]['close'].tolist()


class SupportResistanceLevel:
    def __init__(self, stock_df: pd.DataFrame):
        self.stock_df = stock_df

        self.start_date = stock_df['Date'].iloc[0]
        self.end_date = stock_df['Date'].iloc[-1]

        self.support_levels_3rd = get_close_price(stock_df, stock_df[LOCAL_MIN_PRICE_3RD])
        self.resistance_levels_3rd = get_close_price(stock_df, stock_df[LOCAL_MAX_PRICE_3RD])

        self.support_levels_4th = get_close_price(stock_df, stock_df[LOCAL_MIN_PRICE_4TH])
        self.resistance_levels_4th = get_close_price(stock_df, stock_df[LOCAL_MAX_PRICE_4TH])

    def _build_graph(self, fig: go.Figure, prices: list, name: str, color: str, enable=False):
        x = []
        y = []

        for price in prices:
            x.extend([self.start_date, self.end_date, None])
            y.extend([price, price, None])

        fig.add_trace(
            go.Scatter(
                name=name,
                x=x,
                y=y,
                mode='lines',
                line=dict(width=0.75, color=color),
                visible=None if enable else 'legendonly',
            )
        )

    def build_graph(self, fig: go.Figure, interval: str, enable=False):
        self._build_graph(fig, self.support_levels_3rd, 'support levels - 3rd', 'green',
                          True if enable and interval != '1h' else False)
        self._build_graph(fig, self.resistance_levels_3rd, 'resistance levels - 3rd', 'red',
                          True if enable and interval != '1h' else False)

        self._build_graph(fig, self.support_levels_4th, 'support levels - 4th', 'green',
                          True if enable and interval == '1h' else False)
        self._build_graph(fig, self.resistance_levels_4th, 'resistance levels - 4th', 'red',
                          True if enable and interval == '1h' else False)
