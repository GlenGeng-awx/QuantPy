import plotly.graph_objects as go
from plotly.subplots import make_subplots

from analysis_engine import AnalysisEngine

from util import *

from min_max_analysis import PriceMinMaxDisplay
from wave_analysis import WaveDisplay
# from price_box_display import PriceBoxDisplay

from volume_min_max_display import VolumeMinMaxDisplay
# from volume_mountain_view_display import VolumeMountainViewDisplay
# from volume_trend_display import VolumeTrendDisplay

# from trading_record_display import TradingRecordDisplay


class DisplayEngine:
    def __init__(self, analysis_engine: AnalysisEngine):
        self.stock_name = analysis_engine.stock_name
        self.interval = analysis_engine.interval

        self.stock_df = analysis_engine.stock_df
        self.analysis_engine = analysis_engine

        from_date = shrink_date_str(self.stock_df.iloc[0]['Date'])
        to_date = shrink_date_str(self.stock_df.iloc[-1]['Date'])
        self.title = (f"{self.stock_name}: {from_date} to {to_date}, "
                      f"{self.stock_df.shape[0]} {'days' if self.interval == '1d' else 'hours'}")

        self.fig = None

    def setup_graph(self):
        self.fig = make_subplots(rows=2, cols=1,
                                 subplot_titles=("candle stick", "volume"),
                                 vertical_spacing=0.05,
                                 row_heights=[0.6, 0.4],
                                 shared_xaxes=True,
                                 )

        rangebreaks = [
            dict(bounds=["sat", "mon"]),  # hide weekends
        ]

        if self.interval == '1h':
            rangebreaks.append(dict(bounds=[16, 9], pattern="hour"))  # hide hours outside 9am-4pm

        self.fig.update_xaxes(
            rangebreaks=rangebreaks
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
                high=self.stock_df['high'],
                low=self.stock_df['low'],
                name="Candlesticks",
                increasing_line_color='red',
                decreasing_line_color='green',
                line=dict(width=0.5),
                visible='legendonly',
            )
        )

        self.fig.add_trace(
            go.Scatter(
                name="close_price",
                x=self.stock_df['Date'],
                y=self.stock_df['close'],
                line=dict(width=0.5, color='blue'),
                # visible='legendonly',
            )
        )

    def build_graph(self):
        self.setup_graph()

        self.add_candlestick()
        WaveDisplay(self.fig, self.analysis_engine.wave_analysis).build_graph()
        PriceMinMaxDisplay(self.fig, self.stock_df).build_graph()
        # PriceBoxDisplay(self.fig, self.analysis_engine.price_box_analysis).build_graph()

        VolumeMinMaxDisplay(self.fig, self.stock_df).build_graph()
        # VolumeMountainViewDisplay(self.fig, self.stock_df).build_graph()
        # VolumeTrendDisplay(self.fig, self.stock_df).build_graph()

        # TradingRecordDisplay(self.fig, self.stock_name).build_graph()

    def display(self):
        self.fig.show()
