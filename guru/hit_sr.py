import pandas as pd
import plotly.graph_objects as go

from technical.sr_level import SupportResistanceLevel

MARGIN = 0.005


def _hit(target_price, price):
    return target_price * (1 - MARGIN) <= price <= target_price * (1 + MARGIN)


def calculate_hits(stock_df: pd.DataFrame, indices: list) -> list:
    hits = []

    for base_idx in indices:
        price = stock_df.loc[base_idx]['close']

        for idx in range(base_idx + 10, min(base_idx + 120, stock_df.index[-1] + 1)):
            date = stock_df.loc[idx]['Date']

            high = stock_df.loc[idx]['high']
            low = stock_df.loc[idx]['low']
            close = stock_df.loc[idx]['close']

            if _hit(price, high):
                hits.append((date, high))
            if _hit(price, low):
                hits.append((date, low))
            if _hit(price, close):
                hits.append((date, close))

    return sorted(list(set(hits)), key=lambda x: x[0])


class HitSR:
    def __init__(self, stock_df: pd.DataFrame, sr_level: SupportResistanceLevel):
        self.hits = calculate_hits(stock_df, sr_level.min_indices + sr_level.max_indices)

    def build_graph(self, fig: go.Figure, enable=False,
                    guru_start_date='2000-01-01', guru_end_date='2099-12-31'):
        self.hits = [
            (date, price) for date, price in self.hits if guru_start_date <= date <= guru_end_date
        ]
        fig.add_trace(
            go.Scatter(
                name=f'hit sr',
                x=[date for date, _ in self.hits],
                y=[price for _, price in self.hits],
                mode='markers', marker=dict(color='Sienna', size=3),
                visible=None if enable else 'legendonly',
            )
        )
