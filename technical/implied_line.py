import pandas as pd
import plotly.graph_objects as go

from util import shrink_date_str
from technical import Anchor
from technical.min_max import LOCAL_MIN_PRICE_3RD, LOCAL_MAX_PRICE_3RD
from technical.secondary_line import calculate_secondary_line
from core_banking import CORE_BANKING, MID_TERM


class ImpliedLine:
    def __init__(self, stock_df: pd.DataFrame, stock_name: str):
        self.stock_df = stock_df
        self.stock_name = stock_name

        # list of (dates, prices, k)
        self.implied_lines = []

        anchor1, anchor2 = self.get_mid_term_line()
        if anchor1 is None or anchor2 is None:
            return

        condition = stock_df[LOCAL_MIN_PRICE_3RD] | stock_df[LOCAL_MAX_PRICE_3RD]
        dates = stock_df.tail(250)[condition]['Date']
        if dates.empty:
            return

        for date in dates:
            implied_line = calculate_secondary_line(stock_df, Anchor(date), 5, 250, anchor1, anchor2)
            self.implied_lines.append(implied_line)

    def get_mid_term_line(self):
        dates = self.stock_df['Date'].apply(shrink_date_str).values

        for line in CORE_BANKING.get(self.stock_name, {}).get('lines', []):
            if len(line) == 5 and line[4] == MID_TERM:
                anchor1, anchor2 = Anchor.of(line[0]), Anchor.of(line[1])
                if anchor1.date in dates and anchor2.date in dates:
                    return anchor1, anchor2

        return None, None

    def build_graph(self, fig: go.Figure, enable=False):
        for i, (dates, prices, k) in enumerate(self.implied_lines):
            fig.add_trace(
                go.Scatter(
                    name=f'implied line-{i + 1}',
                    x=dates, y=prices,
                    mode='lines', line=dict(width=0.75, color='blue', dash='dot'),
                    visible=None if enable else 'legendonly',
                )
            )
