import pandas as pd
import plotly.graph_objects as go

from util import max_between, min_between
from .min_max import (LOCAL_MAX_PRICE_1ST, LOCAL_MIN_PRICE_1ST, LOCAL_MAX_PRICE_2ND, LOCAL_MIN_PRICE_2ND,
                      LOCAL_MAX_PRICE_3RD, LOCAL_MIN_PRICE_3RD, LOCAL_MAX_PRICE_4TH, LOCAL_MIN_PRICE_4TH)


def calculate_wave(stock_df: pd.DataFrame, condition: pd.Series):
    triggered = stock_df[condition].index.tolist()

    if len(triggered) == 0:
        return [], [], []

    # handle tail
    highest_idx = max_between(stock_df, triggered[-1], stock_df.index[-1])
    lowest_idx = min_between(stock_df, triggered[-1], stock_df.index[-1])

    triggered = list(set(triggered) | {highest_idx, lowest_idx})
    triggered.sort()

    wave_idx = set()

    for i in range(1, len(triggered)):
        prev_idx, curr_idx = triggered[i - 1], triggered[i]

        highest_idx = max_between(stock_df, prev_idx, curr_idx)
        lowest_idx = min_between(stock_df, prev_idx, curr_idx)

        wave_idx.update({prev_idx, curr_idx, highest_idx, lowest_idx})

    wave_idx = list(wave_idx)
    wave_idx.sort()

    wave_x = stock_df.loc[wave_idx]['Date'].tolist()
    wave_y = stock_df.loc[wave_idx]['close'].tolist()

    return wave_idx, wave_x, wave_y


class Wave:
    def __init__(self, stock_df: pd.DataFrame):
        self.stock_df = stock_df

        condition_1st = self.stock_df[LOCAL_MAX_PRICE_1ST] | self.stock_df[LOCAL_MIN_PRICE_1ST]
        self.wave_1st = calculate_wave(self.stock_df, condition_1st)

        condition_2nd = self.stock_df[LOCAL_MAX_PRICE_2ND] | self.stock_df[LOCAL_MIN_PRICE_2ND]
        self.wave_2nd = calculate_wave(self.stock_df, condition_2nd)

        condition_3rd = self.stock_df[LOCAL_MAX_PRICE_3RD] | self.stock_df[LOCAL_MIN_PRICE_3RD]
        self.wave_3rd = calculate_wave(self.stock_df, condition_3rd)

        condition_4th = self.stock_df[LOCAL_MAX_PRICE_4TH] | self.stock_df[LOCAL_MIN_PRICE_4TH]
        self.wave_4th = calculate_wave(self.stock_df, condition_4th)

    def build_graph(self, fig: go.Figure, enable=False):
        fig.add_trace(
            go.Scatter(
                name="wave 1st",
                x=self.wave_1st[1],
                y=self.wave_1st[2],
                line=dict(width=1, color='black'),
                visible=None if enable else 'legendonly',
                # visible='legendonly',
            )
        )

        fig.add_trace(
            go.Scatter(
                name="wave 2nd",
                x=self.wave_2nd[1],
                y=self.wave_2nd[2],
                line=dict(width=1, color='black'),
                # visible=None if enable else 'legendonly',
                visible='legendonly',
            )
        )

        fig.add_trace(
            go.Scatter(
                name="wave 3rd",
                x=self.wave_3rd[1],
                y=self.wave_3rd[2],
                line=dict(width=1, color='black'),
                # visible=None if enable else 'legendonly',
                visible='legendonly',
            )
        )

        fig.add_trace(
            go.Scatter(
                name="wave 4th",
                x=self.wave_4th[1],
                y=self.wave_4th[2],
                line=dict(width=1, color='black'),
                # visible=None if enable else 'legendonly',
                visible='legendonly',
            )
        )
