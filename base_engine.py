from plotly.subplots import make_subplots

from technical.price import Price
from technical.volume import Volume
from technical.min_max import MinMax
from technical.wave import Wave
from technical.sr_level import SupportResistanceLevel
from technical.line import Line
from technical.box import Box

from statistical.ema import EMA
from statistical.ma import MA
from statistical.bband import BBand
from statistical.macd import MACD
from statistical.rsi import RSI

from trading.trading_record_display import TradingRecordDisplay
from trading.ratio_analysis_and_display import RatioForcastDisplay

from util import load_data, shrink_date_str, interval_to_label


class BaseEngine:
    def __init__(self, stock_name, from_date, to_date, interval='1d'):
        print(f"BaseEngine: {stock_name} {from_date}~{to_date} with interval {interval}")
        self.stock_name = stock_name
        self.interval = interval

        self.stock_df = None
        self.fig = None

        # load data
        stock_data = load_data(self.stock_name, self.interval)

        condition = (stock_data['Date'] > from_date) & (stock_data['Date'] < to_date)
        self.stock_df = stock_data.copy()[condition]

        # calculate
        self.price = Price(self.stock_df)

        self.ema = EMA(self.stock_df)
        self.ma = MA(self.stock_df)
        self.bband = BBand(self.stock_df)
        self.macd = MACD(self.stock_df)
        self.rsi = RSI(self.stock_df)

        self.min_max = MinMax(self.stock_df)
        self.wave = Wave(self.stock_df)
        self.sr_level = SupportResistanceLevel(self.stock_df, self.stock_name)
        self.line = Line(self.stock_df, self.stock_name)
        self.box = Box(self.stock_df, self.wave)

        self.volume = Volume(self.stock_df)

    def setup_graph(self, rows=2):
        if rows == 2:
            self.fig = make_subplots(rows=2, cols=1,
                                     row_heights=[0.5, 0.25],
                                     shared_xaxes=True,
                                     vertical_spacing=0.05,
                                     )
        elif rows == 3:
            self.fig = make_subplots(rows=3, cols=1,
                                     row_heights=[0.5, 0.25, 0.25],
                                     shared_xaxes=True,
                                     vertical_spacing=0.03,
                                     )
        elif rows == 4:
            self.fig = make_subplots(rows=4, cols=1,
                                     row_heights=[0.5, 0.25, 0.25, 0.25],
                                     shared_xaxes=True,
                                     vertical_spacing=0.01,
                                     )
        else:
            raise ValueError(f"Invalid rows: {rows}")

        rangebreaks = [
            dict(bounds=["sat", "mon"]),  # hide weekends
        ]

        if self.interval == '1h':
            rangebreaks.append(dict(bounds=[16, 9], pattern="hour"))  # hide hours outside 9am-4pm

        self.fig.update_xaxes(
            rangebreaks=rangebreaks
        )

        from_date = shrink_date_str(self.stock_df.iloc[0]['Date'])
        to_date = shrink_date_str(self.stock_df.iloc[-1]['Date'])

        title = (f"{self.stock_name}: {from_date} to {to_date}, "
                 f"{self.stock_df.shape[0]} {interval_to_label(self.interval)}")

        self.fig.update_layout(
            title=title,
            xaxis_rangeslider_visible=False,
            # xaxis_gridcolor='gray',
            hovermode="x unified",
            hoverlabel=dict(
                namelength=200
            ),
            height=1000,
        )

        # Apply xaxis_gridcolor to all rows
        for i in range(1, rows + 1):
            self.fig.update_xaxes(gridcolor='gray', row=i, col=1)

    def build_graph(self,
                    enable_candlestick=False,
                    enable_close_price=False,
                    # statistical
                    enable_ema=False,
                    enable_ma=False,
                    enable_bband=False,
                    enable_bband_pst=(False, 2),
                    enable_macd=(False, 2),
                    enable_rsi=(False, 2),
                    # technical
                    enable_min_max=False,
                    enable_wave=False,
                    enable_sr=False,
                    enable_line=False,
                    enable_box=False,
                    enable_ratio=False,
                    # volume
                    enable_volume_raw=(False, 2),
                    enable_volume_reg=(False, 2),
                    # misc
                    rows=2,
                    ):
        self.setup_graph(rows)

        self.price.build_graph(self.fig, enable_candlestick, enable_close_price)

        self.ema.build_graph(self.fig, enable_ema)
        self.ma.build_graph(self.fig, enable_ma)
        self.bband.build_graph(self.fig, enable_bband, enable_bband_pst)
        self.macd.build_graph(self.fig, enable_macd)
        self.rsi.build_graph(self.fig, enable_rsi)

        self.wave.build_graph(self.fig, enable_wave)
        self.sr_level.build_graph(self.fig, enable_sr)
        self.line.build_graph(self.fig, enable_line)
        self.box.build_graph(self.fig, self.interval, enable_box)
        self.min_max.build_graph(self.fig, self.interval, enable_min_max)

        self.volume.build_graph(self.fig, enable_volume_raw, enable_volume_reg)

        TradingRecordDisplay(self.fig, self.stock_name, self.interval).build_graph()
        RatioForcastDisplay(self.fig, self.stock_df, self.stock_name, enable_ratio).build_graph()

    def display(self):
        self.fig.show()
