from base_engine import BaseEngine
from preload_conf import period, FULL, FOUR_YEAR, TWO_YEAR, with_overrides
from transactions.book import get_current_position
from conf import *

drill_down_full = [
    (period(8), with_overrides(FULL, enable_elliott=False, enable_neck_line=False, enable_line=True)),
    (period(8), with_overrides(FULL, enable_elliott=True, enable_neck_line=False, enable_line=True)),
    (period(8), FULL),
]

drill_down_4y = [
    (period(4), with_overrides(FOUR_YEAR, enable_elliott=False, enable_neck_line=False, enable_line=False,
                               enable_implied_neck_line=False, enable_implied_line=False)),
    (period(4), with_overrides(FOUR_YEAR, enable_implied_neck_line=False, enable_implied_line=False)),
    (period(4), FOUR_YEAR),
]

hologram = [
    (period(8), FULL),
    (period(4), FOUR_YEAR),
    (period(2), TWO_YEAR),
]

Position = [
    ETF_SSE_DIVIDEND,
    ETF_CSI_300,
    ETF_STAR_50,
    ETF_CHI_NEXT,

    QQQ,
    SOX,
    GLD,
    BTC,
    COIN,

    KWEB,
    PDD,
    TME,
    TCOM,

    ADBE,
    TTD,
    PYPL,
    CPNG,

    #
    TENCENT,
    ORCL,
    CRM,
    NVO,
]

for stock_name in Position:
    for (from_date, to_date, interval), args in drill_down_full:
        base_engine = BaseEngine(stock_name, from_date, to_date, interval)
        base_engine.build_graph(**args)
        base_engine.fig.show()
