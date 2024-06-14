import plotly.graph_objects as go
from price_support_resistance_analysis import PriceSupportResistanceAnalysis


class PriceSupportResistanceDisplay:
    def __init__(self, fig: go.Figure, analysis: PriceSupportResistanceAnalysis):
        self.fig = fig
        self.support_resistance_level = analysis.support_resistance_level

    def build_graph(self):
        for level in self.support_resistance_level:
            self.fig.add_hline(
                y=level,
                line_width=0.5,
                line_dash="dash",
                line_color="grey",
                row=1, col=1
            )
