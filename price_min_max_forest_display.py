import plotly.graph_objects as go
from price_min_max_forest_analysis import PriceMinMaxForestAnalysis
from util import *


class PriceMinMaxForestDisplay:
    def __init__(self, fig: go.Figure, analysis: PriceMinMaxForestAnalysis):
        self.fig = fig

        self.stock_df = analysis.stock_df

        self.max_forest_3rd = analysis.max_forest_3rd
        self.min_forest_3rd = analysis.min_forest_3rd

        self.max_forest_2nd = analysis.max_forest_2nd
        self.min_forest_2nd = analysis.min_forest_2nd

    def add_scatter(self, edges, column: str, name: str, color: str, width: int):
        x = []
        y = []

        for (from_date, from_idx, to_date, to_idx) in edges:
            from_price = self.stock_df.loc[from_idx][column]
            to_price = self.stock_df.loc[to_idx][column]

            x.extend([from_date, to_date, None])
            y.extend([from_price, to_price, None])

        self.fig.add_trace(
            go.Scatter(
                name=name,
                x=x,
                y=y,
                mode='lines',
                line=dict(width=width, color=color, dash='dot'),
            )
        )

    def build_graph(self):
        # max forest 3rd
        # self.add_scatter(self.max_forest_3rd, high_k, 'max forest 3rd', 'red', 1)

        # min forest 3rd
        # self.add_scatter(self.min_forest_3rd, low_k, 'min forest 3rd', 'green', 1)

        # max forest 2nd
        self.add_scatter(self.max_forest_2nd, high_k, 'max forest 2nd', 'red', 1)

        # min forest 2nd
        self.add_scatter(self.min_forest_2nd, low_k, 'min forest 2nd', 'green', 1)