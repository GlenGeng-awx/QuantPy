import pandas as pd
import plotly.graph_objects as go

from util import max_between, min_between
from conf import *


class WaveAnalysisImpl:
    def __init__(self, stock_df: pd.DataFrame, condition: pd.Series):
        self.stock_df = stock_df
        self.condition = condition

        self.wave_x = []
        self.wave_y = []

    def analyze(self):
        triggered = self.stock_df[self.condition].index.tolist()

        if len(triggered) <= 2:
            return

        wave_x = [self.stock_df.loc[triggered[0]]['Date']]
        wave_y = [self.stock_df.loc[triggered[0]]['close']]

        for i in range(1, len(triggered)):
            prev_idx, curr_idx = triggered[i - 1], triggered[i]

            highest_idx = max_between(self.stock_df, prev_idx, curr_idx)
            lowest_idx = min_between(self.stock_df, prev_idx, curr_idx)

            candidate = {prev_idx, curr_idx, highest_idx, lowest_idx}
            candidate.discard(prev_idx)  # already in wave_x

            candidate = list(candidate)
            candidate.sort()

            for idx in candidate:
                wave_x.append(self.stock_df.loc[idx]['Date'])
                wave_y.append(self.stock_df.loc[idx]['close'])

        self.wave_x = wave_x
        self.wave_y = wave_y


class WaveAnalysis:
    def __init__(self, stock_df: pd.DataFrame):
        self.stock_df = stock_df

        self.wave_1st = None
        self.wave_2nd = None
        self.wave_3rd = None
        self.wave_4th = None

    def analyze(self):
        condition_1st = self.stock_df[local_max_price_1st] | self.stock_df[local_min_price_1st]
        wave_1st = WaveAnalysisImpl(self.stock_df, condition_1st)
        wave_1st.analyze()

        condition_2nd = self.stock_df[local_max_price_2nd] | self.stock_df[local_min_price_2nd]
        wave_2nd = WaveAnalysisImpl(self.stock_df, condition_2nd)
        wave_2nd.analyze()

        condition_3rd = self.stock_df[local_max_price_3rd] | self.stock_df[local_min_price_3rd]
        wave_3rd = WaveAnalysisImpl(self.stock_df, condition_3rd)
        wave_3rd.analyze()

        condition_4th = self.stock_df[local_max_price_4th] | self.stock_df[local_min_price_4th]
        wave_4th = WaveAnalysisImpl(self.stock_df, condition_4th)
        wave_4th.analyze()

        self.wave_1st = wave_1st
        self.wave_2nd = wave_2nd
        self.wave_3rd = wave_3rd
        self.wave_4th = wave_4th


class WaveDisplay:
    def __init__(self, fig: go.Figure, wave_analysis: WaveAnalysis):
        self.fig = fig
        self.wave_analysis = wave_analysis

    def build_graph(self):
        wave_1st = self.wave_analysis.wave_1st

        self.fig.add_trace(
            go.Scatter(
                name="wave 1st",
                x=wave_1st.wave_x,
                y=wave_1st.wave_y,
                line=dict(width=1, color='black'),
                visible='legendonly',
            )
        )

        wave_2nd = self.wave_analysis.wave_2nd

        self.fig.add_trace(
            go.Scatter(
                name="wave 2nd",
                x=wave_2nd.wave_x,
                y=wave_2nd.wave_y,
                line=dict(width=1, color='black'),
                visible='legendonly',
            )
        )

        wave_3rd = self.wave_analysis.wave_3rd

        self.fig.add_trace(
            go.Scatter(
                name="wave 3rd",
                x=wave_3rd.wave_x,
                y=wave_3rd.wave_y,
                line=dict(width=1, color='black'),
                visible='legendonly',
            )
        )

        wave_4th = self.wave_analysis.wave_4th

        self.fig.add_trace(
            go.Scatter(
                name="wave 4th",
                x=wave_4th.wave_x,
                y=wave_4th.wave_y,
                line=dict(width=1, color='black'),
                visible='legendonly',
            )
        )
