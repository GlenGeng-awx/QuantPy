from plotly.subplots import make_subplots

from technical.price import Price
from technical.volume import Volume
from technical.min_max import MinMax
from technical.sr_level import SupportResistanceLevel
from technical.line import Line
from technical.line_expo import LineExpo
from technical.neck_line import NeckLine
from technical.elliott import Elliott
from technical.tech import Tech
from technical.rd import RD
from technical.gap import Gap

from statistical.ema import EMA
from statistical.ma import MA
from statistical.trend import Trend
from statistical.bband import BBand
from statistical.macd import MACD
from statistical.rsi import RSI

from guru.hit_line import HitLine
from guru.hit_line_expo import HitLineExpo
from guru.hit_neck_line import HitNeckLine
from guru.hit_sr import HitSR
from guru.hit_volume import HitVolume

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

        condition = (stock_data['Date'] >= from_date) & (stock_data['Date'] <= to_date)
        self.stock_df = stock_data.copy()[condition]

        # calculate
        self.price = Price(self.stock_df)

        self.ema = EMA(self.stock_df)
        self.ma = MA(self.stock_df)
        self.trend = Trend(self.stock_df)
        self.bband = BBand(self.stock_df)
        self.macd = MACD(self.stock_df)
        self.rsi = RSI(self.stock_df)

        self.min_max = MinMax(self.stock_df)
        self.sr_level = SupportResistanceLevel(self.stock_df)

        self.line = Line(self.stock_df, self.stock_name)
        self.line_expo = LineExpo(self.stock_df, self.stock_name)
        self.neck_line = NeckLine(self.stock_df, self.stock_name)

        self.elliott = Elliott(self.stock_df, self.stock_name)
        self.tech = Tech(self.stock_df, self.stock_name)
        self.rd = RD(self.stock_df, self.stock_name)
        self.gap = Gap(self.stock_df, self.stock_name)

        self.volume = Volume(self.stock_df, self.stock_name)

        # guru
        self.hit_line = HitLine(self.stock_df, self.line)
        self.hit_line_expo = HitLineExpo(self.stock_df, self.line_expo)
        self.hit_neck_line = HitNeckLine(self.stock_df, self.neck_line)
        self.hit_sr = HitSR(self.stock_df, self.sr_level)
        self.hit_volume = HitVolume(self.stock_df)

    def setup_graph(self, rows=2):
        self.fig = make_subplots(rows=rows, cols=1,
                                 row_heights=[0.5] + [0.25] * (rows - 1),
                                 shared_xaxes=True,
                                 vertical_spacing=0.02,
                                 )

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
            yaxis_type='log',
            hovermode="x unified",
            hoverdistance=1,  # Only show hoverlabel for the current day
            hoverlabel=dict(
                namelength=200
            ),
            height=500 + 250 * (rows - 1)
        )

        # # Apply xaxis_gridcolor to all rows
        # for i in range(1, rows + 1):
        #     self.fig.update_xaxes(gridcolor='gray', row=i, col=1)

    def build_graph(self,
                    enable_candlestick=False,
                    enable_close_price=False,
                    # statistical
                    enable_ema=False,
                    enable_ma=False,
                    enable_trend=False,
                    enable_bband=False,
                    enable_bband_pst=(False, 2),
                    enable_macd=(False, 2),
                    enable_rsi=(False, 2),
                    # technical
                    enable_min_max=False,
                    enable_sr=False,
                    enable_line=False,
                    enable_line_expo=False,
                    enable_neck_line=False,
                    enable_elliott=True,
                    enable_tech=True,
                    enable_rd=True,
                    enable_gap=False,
                    # volume
                    enable_volume=(False, 2),
                    # misc
                    rows=2,
                    # guru
                    enable_hit_line=False,
                    enable_hit_line_expo=False,
                    enable_hit_neck_line=False,
                    enable_hit_sr=False,
                    enable_hit_low_vol=(False, 2),
                    enable_hit_high_vol=(False, 2),
                    ):
        self.setup_graph(rows)

        self.price.build_graph(self.fig, enable_candlestick, enable_close_price)

        self.elliott.build_graph(self.fig, enable_elliott)
        self.tech.build_graph(self.fig, enable_tech)
        self.rd.build_graph(self.fig, enable_rd)
        self.gap.build_graph(self.fig, enable_gap)

        self.volume.build_graph(self.fig, self.gap, enable_volume)

        self.min_max.build_graph(self.fig, self.interval, enable_min_max)
        self.sr_level.build_graph(self.fig, enable_sr)

        self.line.build_graph(self.fig, enable_line)
        self.line_expo.build_graph(self.fig, enable_line_expo)
        self.neck_line.build_graph(self.fig, enable_neck_line)

        # guru
        self.hit_line.build_graph(self.fig, enable_hit_line)
        self.hit_line_expo.build_graph(self.fig, enable_hit_line_expo)
        self.hit_neck_line.build_graph(self.fig, enable_hit_neck_line)
        self.hit_sr.build_graph(self.fig, enable_hit_sr)
        self.hit_volume.build_graph(self.fig, enable_hit_low_vol, enable_hit_high_vol)

        self.ma.build_graph(self.fig, enable_ma)
        self.ema.build_graph(self.fig, enable_ema)
        self.trend.build_graph(self.fig, enable_trend)
        self.bband.build_graph(self.fig, enable_bband, enable_bband_pst)
        self.macd.build_graph(self.fig, enable_macd)
        self.rsi.build_graph(self.fig, enable_rsi)
