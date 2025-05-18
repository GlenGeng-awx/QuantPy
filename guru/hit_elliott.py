import pandas as pd
import plotly.graph_objects as go

from trading.core_banking import CORE_BANKING
from util import get_idx_by_date


def _hit(target_price, price, margin: float):
    return target_price * (1 - margin) <= price <= target_price * (1 + margin)


# lines: list of (dates, prices)
def calculate_hits(stock_df: pd.DataFrame, stock_name: str, margin) -> list:
    hits = []

    for elliott_date, _ in CORE_BANKING.get(stock_name, {}).get('elliott', {}).items():
        idx = get_idx_by_date(stock_df, elliott_date)
        price = stock_df.loc[idx]['close']

        for i in stock_df.index:
            if i < idx + 20:
                continue

            date = stock_df.loc[i]['Date']
            high, low, close = stock_df.loc[i]['high'], stock_df.loc[i]['low'], stock_df.loc[i]['close']

            if _hit(price, high, margin):
                hits.append((date, high))
            if _hit(price, low, margin):
                hits.append((date, low))
            if _hit(price, close, margin):
                hits.append((date, close))

    return sorted(list(set(hits)), key=lambda x: x[0])


class HitElliott:
    def __init__(self, stock_df: pd.DataFrame, stock_name: str):
        self.hits = calculate_hits(stock_df, stock_name, 0.01)

    def build_graph(self, fig: go.Figure, enable=False,
                    guru_start_date='2000-01-01', guru_end_date='2099-12-31'):
        self.hits = [
            (date, price) for date, price in self.hits if guru_start_date <= date <= guru_end_date
        ]
        fig.add_trace(
            go.Scatter(
                name=f'hit elliott',
                x=[date for date, _ in self.hits],
                y=[price for _, price in self.hits],
                mode='markers', marker=dict(color='Chocolate', size=4),
                visible=None if enable else 'legendonly',
            )
        )
