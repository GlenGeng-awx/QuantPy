import pandas as pd
import plotly.graph_objects as go
from technical.neck_line import calculate_neck_line
from technical.min_max import LOCAL_MIN_PRICE_3RD, LOCAL_MAX_PRICE_3RD


class ImpliedNeckLine:
    def __init__(self, stock_df: pd.DataFrame):
        # list of (dates, prices)
        self.implied_neck_lines = []

        condition = stock_df[LOCAL_MIN_PRICE_3RD] | stock_df[LOCAL_MAX_PRICE_3RD]
        dates = stock_df.tail(250)[condition]['Date']
        if dates.empty:
            return

        for date in dates:
            self.implied_neck_lines.append(calculate_neck_line(stock_df, date, 5, 250))

        # sort by price
        self.implied_neck_lines.sort(key=lambda x: x[1][0], reverse=True)

    def build_graph(self, fig: go.Figure, enable=True):
        for i, (dates, prices) in enumerate(self.implied_neck_lines):
            fig.add_trace(
                go.Scatter(
                    name=f'implied neck line-{i + 1}',
                    x=dates, y=prices,
                    mode='lines', line=dict(width=0.75, color='brown', dash='dot'),
                    visible=None if enable else 'legendonly',
                )
            )
