from base_engine import BaseEngine
from preload_conf import period, FULL, FOUR_YEAR, TWO_YEAR, with_overrides
from transaction_book import get_current_position

drill_down_full = [
    (period(7), with_overrides(FULL, enable_elliott=False, enable_neck_line=False, enable_line=False)),
    (period(7), with_overrides(FULL, enable_elliott=False, enable_line=False)),
    (period(7), with_overrides(FULL, enable_elliott=False)),
    (period(7), FULL),
]

drill_down_4y = [
    (period(4), with_overrides(FOUR_YEAR, enable_elliott=False, enable_neck_line=False, enable_line=False,
                               enable_implied_neck_line=False, enable_implied_line=False)),
    (period(4), with_overrides(FOUR_YEAR, enable_implied_neck_line=False, enable_implied_line=False)),
    (period(4), FOUR_YEAR),
]

hologram = [
    (period(7), FULL),
    (period(4), FOUR_YEAR),
    (period(2), TWO_YEAR),
]

for stock_name in get_current_position():
    for (from_date, to_date, interval), args in hologram:
        base_engine = BaseEngine(stock_name, from_date, to_date, interval)
        base_engine.build_graph(**args)
        base_engine.fig.show()
