import plotly.graph_objects as go
from price_min_max_forest_analysis import PriceMinMaxForestAnalysis


class PriceMinMaxForestDisplay:
    def __init__(self, fig: go.Figure, analysis: PriceMinMaxForestAnalysis):
        self.fig = fig

        self.stock_df = analysis.stock_df
        self.max_forest = analysis.max_forest
        self.min_forest = analysis.min_forest

    def build_graph(self):
        # max forest
        x = []
        y = []
        for (from_date, from_idx, to_date, to_idx) in self.max_forest:
            from_high = self.stock_df.loc[from_idx]['high']
            to_high = self.stock_df.loc[to_idx]['high']

            x.extend([from_date, to_date, None])
            y.extend([from_high, to_high, None])

        self.fig.add_trace(
            go.Scatter(
                name='max forest',
                x=x,
                y=y,
                mode='lines',
                line=dict(width=1, color='red', dash='dot'),
            )
        )

        # min forest
        x = []
        y = []
        for (from_date, from_idx, to_date, to_idx) in self.min_forest:
            from_low = self.stock_df.loc[from_idx]['low']
            to_low = self.stock_df.loc[to_idx]['low']

            x.extend([from_date, to_date, None])
            y.extend([from_low, to_low, None])

        self.fig.add_trace(
            go.Scatter(
                name='min forest',
                x=x,
                y=y,
                mode='lines',
                line=dict(width=1, color='green', dash='dot'),
            )
        )
