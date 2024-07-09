import plotly.graph_objects as go
from plotly.subplots import make_subplots

from analysis_engine import AnalysisEngine
from min_max_analysis import PriceMinMaxDisplay
from wave_analysis import WaveDisplay
from box_display import BoxDisplay
from trading_record_display import TradingRecordDisplay

from util import *
from conf import *


class DisplayEngine:
    def __init__(self, analysis_engine: AnalysisEngine):
        self.stock_name = analysis_engine.stock_name
        self.interval = analysis_engine.interval

        self.stock_df = analysis_engine.stock_df
        self.analysis_engine = analysis_engine

        from_date = shrink_date_str(self.stock_df.iloc[0]['Date'])
        to_date = shrink_date_str(self.stock_df.iloc[-1]['Date'])
        self.title = (f"{self.stock_name}: {from_date} to {to_date}, "
                      f"{self.stock_df.shape[0]} {interval_to_label(self.interval)}")

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
            ),
            # barmode='overlay'
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

    def add_volume_ma(self, column, color: str, size: float):
        self.fig.add_trace(
            go.Scatter(
                name=column,
                x=self.stock_df['Date'],
                y=self.stock_df[column],
                mode='lines',
                line=dict(width=size, color=color),
                visible='legendonly',
            ),
            row=2, col=1
        )

    def add_volume(self):
        self.fig.add_trace(
            go.Bar(
                name="volume",
                x=self.stock_df['Date'],
                y=self.stock_df['volume_reg'],
                marker_color='blue',
                opacity=0.5,
            ),
            row=2, col=1
        )

        self.add_volume_ma(volume_ma_5, 'black', 1)
        self.add_volume_ma(volume_ma_15, 'black', 1)
        self.add_volume_ma(volume_ma_30, 'black', 1)
        self.add_volume_ma(volume_ma_60, 'black', 1)

    def build_graph(self):
        self.setup_graph()

        self.add_candlestick()

        WaveDisplay(self.fig, self.analysis_engine.wave_analysis).build_graph()
        BoxDisplay(self.fig, self.interval, self.analysis_engine.wave_analysis).build_graph()
        PriceMinMaxDisplay(self.fig, self.stock_df).build_graph()

        self.add_volume()

        TradingRecordDisplay(self.fig, self.stock_name, self.interval).build_graph()

    def display(self):
        self.fig.show()
