from plotly.subplots import make_subplots

from technical.price import Price
from technical.volume import Volume
from technical.min_max import MinMax
from technical.sr_level import SupportResistanceLevel
from technical.primary_line import PrimaryLine
from technical.secondary_line import SecondaryLine
from technical.neck_line import NeckLine
from technical.elliott import Elliott
from technical.ec import EC
from technical.transaction import Transaction
from technical.implied_neck_line import ImpliedNeckLine
from technical.implied_line import ImpliedLine

from statistical.ema import EMA
from statistical.ma import MA
from util import load_data, shrink_date_str, interval_to_label, get_next_n_workday
import guru


class BaseEngine:
    def __init__(self, stock_name, from_date, to_date, interval='1d'):
        self.stock_name = stock_name
        self.interval = interval
        print(f"BaseEngine: {stock_name} {from_date}~{to_date} with interval {interval}")

        self.stock_df = None
        self.fig = None

        # load data
        stock_data = load_data(self.stock_name, self.interval)

        dates = stock_data['Date'].apply(shrink_date_str)
        condition = (dates >= from_date) & (dates <= to_date)
        self.stock_df = stock_data.copy()[condition]

        # calculate
        self.price = Price(self.stock_df)

        self.ema = EMA(self.stock_df)
        self.ma = MA(self.stock_df)

        self.min_max = MinMax(self.stock_df)
        self.sr_level = SupportResistanceLevel(self.stock_df)

        self.primary_line = PrimaryLine(self.stock_df, self.stock_name)
        self.secondary_line = SecondaryLine(self.stock_df, self.stock_name)
        self.neck_line = NeckLine(self.stock_df, self.stock_name)

        self.elliott = Elliott(self.stock_df, self.stock_name)
        self.ec = EC(self.stock_df, self.stock_name)
        self.transaction = Transaction(self.stock_name)

        self.volume = Volume(self.stock_df, self.stock_name)

        # implied
        self.implied_neck_line = ImpliedNeckLine(self.stock_df)
        self.implied_line = ImpliedLine(self.stock_df, self.stock_name)

        # guru
        self.context = {}

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
            height=800 + 250 * (rows - 1)
        )

        # add range selector 1Y/2Y to row 1
        self.fig.update_xaxes(
            rangeselector=dict(
                buttons=list([
                    dict(count=6, label="6M", step="month", stepmode="backward"),
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
            row=rows, col=1,
        )

        # # Apply xaxis_gridcolor to all rows
        # for i in range(1, rows + 1):
        #     self.fig.update_xaxes(gridcolor='gray', row=i, col=1)

    def build_graph(self,
                    enable_candlestick=False,
                    enable_close_price=False,
                    # statistical
                    enable_ema=False,
                    enable_ma=(False, False, False, False, False, False, False),
                    # technical
                    enable_min_max=False,
                    enable_sr=False,
                    enable_line=False,
                    enable_neck_line=False,
                    enable_elliott=True,
                    enable_ec=True,
                    enable_transaction=False,
                    # implied
                    enable_implied_neck_line=True,
                    enable_implied_line=True,
                    # other
                    enable_volume=(True, 2),
                    enable_guru=(False, 2, None),
                    rows=2,
                    ):
        self.setup_graph(rows)

        self.price.build_graph(self.fig, enable_candlestick, enable_close_price)

        self.elliott.build_graph(self.fig, enable_elliott)
        self.ec.build_graph(self.fig, enable_ec)
        self.transaction.build_graph(self.fig, enable_transaction)

        self.volume.build_graph(self.fig, enable_volume)

        self.min_max.build_graph(self.fig, self.interval, enable_min_max)
        self.sr_level.build_graph(self.fig, enable_sr)

        self.primary_line.build_graph(self.fig, enable_line)
        self.secondary_line.build_graph(self.fig, enable_line)
        self.neck_line.build_graph(self.fig, enable_neck_line)

        self.ma.build_graph(self.fig, enable_ma)
        # self.ema.build_graph(self.fig, enable_ema)

        self.implied_neck_line.build_graph(self.fig, enable_implied_neck_line)
        self.implied_line.build_graph(self.fig, enable_implied_line)

        if enable_guru[0]:
            self.context = guru.calculate(self.stock_df)

            _, row, last_n_days = enable_guru
            guru.plot.plot(self.stock_df, self.fig, self.context, row, last_n_days)
