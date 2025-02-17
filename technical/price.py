import pandas as pd
import plotly.graph_objects as go


class Price:
    def __init__(self, stock_df: pd.DataFrame):
        self.stock_df = stock_df

    def build_graph(self, fig: go.Figure, enable_candlestick=False, enable_close_price=True):
        fig.add_trace(
            go.Candlestick(
                x=self.stock_df['Date'],
                close=self.stock_df['close'],
                open=self.stock_df['open'],
                high=self.stock_df['high'],
                low=self.stock_df['low'],
                name="Candlesticks",
                increasing_line_color='red',
                decreasing_line_color='green',
                line=dict(width=0.5),
                visible=None if enable_candlestick else 'legendonly',
            )
        )

        fig.add_trace(
            go.Scatter(
                name="close_price",
                x=self.stock_df['Date'],
                y=self.stock_df['close'],
                line=dict(width=0.5, color='blue'),
                visible=None if enable_close_price else 'legendonly',
            )
        )

        fig.add_trace(
            go.Scatter(
                name="close_price_spot",
                x=self.stock_df['Date'],
                y=self.stock_df['close'],
                mode="markers",
                marker=dict(size=2, color='blue'),
                visible='legendonly',
            )
        )

        fig.add_trace(
            go.Scatter(
                name="high_price_spot",
                x=self.stock_df['Date'],
                y=self.stock_df['high'],
                mode="markers",
                marker=dict(size=2, color='red'),
                visible='legendonly',
            )
        )

        fig.add_trace(
            go.Scatter(
                name="low_price_spot",
                x=self.stock_df['Date'],
                y=self.stock_df['low'],
                mode="markers",
                marker=dict(size=2, color='green'),
                visible='legendonly',
            )
        )

        last_close = self.stock_df['close'].iloc[-1]
        fig.add_hline(y=last_close,
                      line_dash='dot',
                      line_color='black',
                      line_width=1,
                      row=1, col=1)
