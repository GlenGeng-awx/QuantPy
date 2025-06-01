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
# from statistical.trend import Trend
# from statistical.bband import BBand
# from statistical.macd import MACD
# from statistical.rsi import RSI

from guru.hit_elliott import HitElliott
from guru.hit_line import HitLine
from guru.hit_line_expo import HitLineExpo
from guru.hit_neck_line import HitNeckLine
from guru.hit_sr import HitSR
from guru.hit_ma import HitMA
from guru.hit_volume import HitVolume
from trading.core_banking import CORE_BANKING

from util import load_data, shrink_date_str, interval_to_label, get_next_n_workday


class BaseEngine:
    def __init__(self, stock_name, from_date, to_date, interval='1d'):
        self.stock_name = stock_name
        self.interval = interval
        self.yaxis_type = CORE_BANKING.get(stock_name, {}).get('yaxis_type', 'log')

        print(f"BaseEngine: {stock_name} {from_date}~{to_date} with interval {interval} and yaxis_type {self.yaxis_type}")

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
        # self.trend = Trend(self.stock_df)
        # self.bband = BBand(self.stock_df)
        # self.macd = MACD(self.stock_df)
        # self.rsi = RSI(self.stock_df)

        self.min_max = MinMax(self.stock_df)
        self.sr_level = SupportResistanceLevel(self.stock_df)

        self.line = Line(self.stock_df, self.stock_name)
        self.line_expo = LineExpo(self.stock_df, self.stock_name)
        self.neck_line = NeckLine(self.stock_df, self.stock_name)

        self.elliott = Elliott(self.stock_df, self.stock_name, self.yaxis_type)
        self.tech = Tech(self.stock_df, self.stock_name, self.yaxis_type)
        self.rd = RD(self.stock_df, self.stock_name)
        self.gap = Gap(self.stock_df, self.stock_name)

        self.volume = Volume(self.stock_df, self.stock_name)

        # guru
        self.hit_elliott = HitElliott(self.stock_df, stock_name)
        self.hit_line = HitLine(self.stock_df, self.line)
        self.hit_line_expo = HitLineExpo(self.stock_df, self.line_expo)
        self.hit_neck_line = HitNeckLine(self.stock_df, self.neck_line)
        self.hit_sr = HitSR(self.stock_df, self.sr_level)
        self.hit_ma = HitMA(self.stock_df)
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
            yaxis_type=self.yaxis_type,
            hovermode="x unified",
            hoverdistance=1,  # Only show hoverlabel for the current day
            hoverlabel=dict(
                namelength=200
            ),
            height=800 + 250 * (rows - 1)
        )

        # add range selector 1Y/2Y to row 1
        self.fig.update_xaxes(
            rangeselector=dict(
                buttons=list([
                    dict(count=12, label="1Y", step="month", stepmode="backward"),
                    dict(count=24, label="2Y", step="month", stepmode="backward"),
                ])
            ),
            row=1, col=1
        )

        # add range slider to row 2
        from_date = self.stock_df['Date'].iloc[-min(750, self.stock_df.shape[0])]
        to_date = get_next_n_workday(self.stock_df['Date'].iloc[-1], 10)

        self.fig.update_xaxes(
            range=[from_date, to_date],  # 初始显示最后750天
            rangeslider_visible=True,
            row=2, col=1
        )

        # # Apply xaxis_gridcolor to all rows
        # for i in range(1, rows + 1):
        #     self.fig.update_xaxes(gridcolor='gray', row=i, col=1)

    def build_graph(self,
                    enable_candlestick=False,
                    enable_close_price=False,
                    # statistical
                    enable_ema=False,
                    enable_ma20=False,
                    enable_ma60=False,
                    enable_ma120=False,
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
                    guru_start_date='2000-01-01',
                    guru_end_date='2099-12-31',
                    enable_hit_elliott=False,
                    enable_hit_line=False,
                    enable_hit_line_expo=False,
                    enable_hit_neck_line=False,
                    enable_hit_sr=False,
                    enable_hit_ma20=False,
                    enable_hit_ma60=False,
                    enable_hit_ma120=False,
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

        self.line_expo.build_graph(self.fig, enable_line_expo)
        self.neck_line.build_graph(self.fig, enable_neck_line)
        self.line.build_graph(self.fig, enable_line)

        # guru
        self.hit_elliott.build_graph(self.fig, enable_hit_elliott, guru_start_date, guru_end_date)
        self.hit_line.build_graph(self.fig, enable_hit_line, guru_start_date, guru_end_date)
        self.hit_line_expo.build_graph(self.fig, enable_hit_line_expo, guru_start_date, guru_end_date)
        self.hit_neck_line.build_graph(self.fig, enable_hit_neck_line, guru_start_date, guru_end_date)
        self.hit_sr.build_graph(self.fig, enable_hit_sr, guru_start_date, guru_end_date)
        self.hit_ma.build_graph(self.fig, enable_hit_ma20, enable_hit_ma60, enable_hit_ma120, guru_start_date,
                                guru_end_date)
        self.hit_volume.build_graph(self.fig, enable_hit_low_vol, enable_hit_high_vol, guru_start_date, guru_end_date)

        self.ma.build_graph(self.fig, enable_ma20, enable_ma60, enable_ma120)
        self.ema.build_graph(self.fig, enable_ema)
        # self.trend.build_graph(self.fig, enable_trend)
        # self.bband.build_graph(self.fig, enable_bband, enable_bband_pst)
        # self.macd.build_graph(self.fig, enable_macd)
        # self.rsi.build_graph(self.fig, enable_rsi)
