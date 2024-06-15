import plotly.graph_objects as go
from plotly.subplots import make_subplots

from analysis_engine import AnalysisEngine

from util import *

from price_min_max_display import PriceMinMaxDisplay
from price_min_max_forest_display import PriceMinMaxForestDisplay
from price_mountain_view_display import PriceMountainViewDisplay
from price_trend_display import PriceTrendDisplay
from price_box_display import PriceBoxDisplay
from price_support_resistance_display import PriceSupportResistanceDisplay

from volume_min_max_display import VolumeMinMaxDisplay
from volume_mountain_view_display import VolumeMountainViewDisplay
from volume_trend_display import VolumeTrendDisplay


class DisplayEngine:
    def __init__(self, analysis_engine: AnalysisEngine, display_conf: dict):
        self.stock_name = analysis_engine.stock_name
        self.stock_df = analysis_engine.stock_df
        self.analysis_engine = analysis_engine

        self.display_conf = display_conf

        from_date = shrink_date_str(self.stock_df.iloc[0]['Date'])
        to_date = shrink_date_str(self.stock_df.iloc[-1]['Date'])
        self.title = f"{self.stock_name}: {from_date} to {to_date}, {self.stock_df.shape[0]} days"

        self.fig = None

    def setup(self):
        self.fig = make_subplots(rows=2, cols=1,
                                 subplot_titles=("candle stick", "volume"),
                                 vertical_spacing=0.05,
                                 row_heights=[0.6, 0.4],
                                 shared_xaxes=True,
                                 )

        self.fig.update_xaxes(
            rangebreaks=[
                dict(bounds=["sat", "mon"]),  # hide weekends
            ]
        )

        # self.fig.update_xaxes(showspikes=True)
        # self.fig.update_yaxes(showspikes=True)

        self.fig.update_layout(
            title=self.title,
            xaxis_rangeslider_visible=False,
            # plot_bgcolor='white',
            xaxis_gridcolor='gray',
            # yaxis_gridcolor='gray',
            hovermode="x unified",
            hoverlabel=dict(
                namelength=200
            )
        )

    def add_candlestick(self):
        self.fig.add_trace(
            go.Candlestick(
                x=self.stock_df['Date'],
                close=self.stock_df['close'],
                open=self.stock_df['open'],
                high=self.stock_df[high_k],
                low=self.stock_df[low_k],
                name="Candlesticks",
                increasing_line_color='red',
                decreasing_line_color='green',
                line=dict(width=0.5)
            )
        )

    def build_graph(self):
        self.setup()

        self.add_candlestick()
        PriceMinMaxDisplay(self.fig, self.stock_df).build_graph()
        PriceMinMaxForestDisplay(self.fig, self.analysis_engine.price_min_max_forest_analysis).build_graph()
        PriceMountainViewDisplay(self.fig, self.stock_df).build_graph()
        # PriceTrendDisplay(self.fig, self.stock_df).build_graph()
        PriceBoxDisplay(self.fig, self.analysis_engine.price_box_analysis, False).build_graph()
        # PriceBoxDisplay(self.fig, self.analysis_engine.price_box_analysis, True).build_graph()
        PriceSupportResistanceDisplay(self.fig, self.analysis_engine.price_support_resistance_analysis).build_graph()

        VolumeMinMaxDisplay(self.fig, self.stock_df).build_graph()
        # VolumeMountainViewDisplay(self.fig, self.stock_df).build_graph()
        VolumeTrendDisplay(self.fig, self.stock_df).build_graph()

    def display(self):
        self.fig.show()
