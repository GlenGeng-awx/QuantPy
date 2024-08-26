from datetime import datetime

from conf import *
from base_engine import BaseEngine

from gringotts.fake_runner import FakeRunner
from gringotts.giant_model import enumerate_switches, TinyModel
from gringotts.real_runner import RealRunner
from gringotts.trend import Trend

from gringotts.s1_9 import S1U9
from gringotts.s1_10 import S1U10
from gringotts.s1_11 import S1U11
from gringotts.s1_11_1 import S1U11V1
from gringotts.s1_12 import S1U12
from gringotts.s1_12_1 import S1U12V1

STOCK_NAMES_INDEX = [
    IXIC,
    SS_000300,
    SS_000001,
    GC_F,
]

STOCK_NAMES_TIER_0 = [
    # BA,
    # FUTU,
    # PLTR,
    # COIN,
    # TSLA,
    # BNTX,
    # AMD,
    # SNOW,
    # HK_0700,
]

STOCK_NAMES_TIER_1 = [
    # PDD,
    # JD,
    # BEKE,
    # HK_0700,
    # NVDA,
    # AMD,
    # BNTX,
    # CPNG,
    # TSM,
    # EBAY,
    # IXIC,
    # SS_000001,
    # TSLA,
    # COIN,
    # XPEV,
    # MRNA,
    # SNOW,
    IQ,
    # PLTR,
    # RIVN,
    # META,
    # MNSO,
    # ZM,
    # BABA,
    # EDU,
    # BA,
    # BILI,
    # LI,
    # SNAP,
    # FUTU,
]


def default_period():
    current_date = datetime.now()

    date_0y_ago = datetime(current_date.year, 1, 1).strftime('%Y-%m-%d')
    date_1y_ago = datetime(current_date.year - 1, 1, 1).strftime('%Y-%m-%d')
    date_5y_ago = datetime(current_date.year - 5, 1, 1).strftime('%Y-%m-%d')

    current_date = current_date.strftime('%Y-%m-%d')

    return [
        # (date_0y_ago, current_date, '1h'),
        (date_1y_ago, current_date, '1d'),
        # (date_5y_ago, current_date, '1wk'),
    ]


def get_period(_stock_name):
    return default_period()


for stock_name in STOCK_NAMES_TIER_1:
    for (start_date, end_date, interval) in get_period(stock_name):
        de = BaseEngine(stock_name, start_date, end_date, interval)
        de.build_graph(
                       enable_close_price=True,
                       enable_ma=True,
                       enable_min_max=True,
                       # enable_macd=True,
                       # enable_bband=True,
                       enable_bband_pst=(True, 2),
                       enable_rsi=(True, 3),
                       enable_volume_reg=(True, 4),
                       # enable_ema=True,
                       # enable_sr=True,
                       # enable_min_max=True
                       # enable_rsi=True,
                       rows=4,
                       )

        stock_df, fig = de.stock_df, de.fig
        Trend(stock_df).build_graph(fig)

        # step1: manual test
        for strategy in [S1U9, S1U10, S1U11, S1U11V1, S1U12, S1U12V1]:
            # for strategy in [S1U11V1]:
            # FakeRunner(stock_df, strategy).show(fig)
            RealRunner(strategy, stock_df).show(fig)

        # step2: automate test
        all_switches = enumerate_switches(10)
        results = []

        for switches in all_switches:
            runner = RealRunner(TinyModel, stock_df, switches)
            stat = runner.book.get_stat()
            revenue_pst, buy_cnt = stat['revenue_pst'], stat['buy_cnt']

            print(f'giant model: {switches} --> {revenue_pst:.2f}%, {buy_cnt} trades')
            results.append((switches, revenue_pst, buy_cnt))

        print(f'\n-----\n-----\n-----\n')

        results.sort(key=lambda x: (x[1], x[2]), reverse=True)

        for idx, (switches, revenue_pst, buy_cnt) in enumerate(results):
            print(f'giant model {idx}: {switches} --> {revenue_pst:.2f}%, {buy_cnt} trades')

        # step3: display top 5
        for switches, _, _ in results[:5]:
            RealRunner(TinyModel, stock_df, switches).show(fig)
