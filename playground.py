from datetime import datetime
from multiprocessing import Process

from conf import *
from base_engine import BaseEngine

from gringotts.giant_model import GiantModel
import features

STOCK_NAMES_INDEX = [
    IXIC,
    # SS_000300,
    # SS_000001,
    # GC_F,
]

STOCK_NAMES_TIER_0 = [
    # TSLA,
    # BILI,
    # HK_0700,
    # IXIC,
    # BABA,
    # PDD,
    # COIN,
    # BA,
    # FUTU,
    # CPNG,
    # PLTR,
    # BNTX,
    # AMD,
    # SNOW,
    # SS_000300,
    # JD,
    # BEKE,
    # NVDA,
    # IQ,
    # SS_000001,
    # RIVN,
    # MRNA,
    # MNSO,
    # EDU,
    # XPEV,
    # TSM,
    # EBAYri,
    # META,
    # ZM,
    LI,
    # SNAP,
]

STOCK_NAMES_TIER_1 = [

]


def default_period():
    current_date = datetime.now()

    date_1y_ago = datetime(current_date.year - 1, 1, 1).strftime('%Y-%m-%d')
    current_date = current_date.strftime('%Y-%m-%d')

    return date_1y_ago, current_date, '1d'


def handle_task(stock_name, start_date, end_date, interval):
    be = BaseEngine(stock_name, start_date, end_date, interval)

    be.build_graph(
        enable_close_price=False,
        # enable_ma=True,
        # enable_ema=True,
        # enable_bband=True,
        enable_min_max=True,
        enable_wave=True,
        enable_sr=True,
        enable_line=True,
        enable_volume_reg=(True, 3),
        enable_bband_pst=(True, 4),
        enable_rsi=(True, 5),
        enable_macd=(True, 6),
        rows=6,
    )

    stock_df, fig = be.stock_df, be.fig

    features.calculate_feature(stock_df)
    features.plot_feature(stock_df, fig)

    # giant_model = GiantModel(stock_df, stock_name)
    # giant_model.run()
    # giant_model.build_graph(fig)

    fig.show()


if __name__ == '__main__':
    start_date, end_date, interval = default_period()

    for stock_name in STOCK_NAMES_TIER_0:
        handle_task(stock_name, start_date, end_date, interval)
