from base_engine import BaseEngine
from preload_conf import *
from conf import *
from transaction_book import get_unexpired_stock_names

"""
Weekly SOP
    7y
    7y neckline

    7y elliott
    7y line

    4y elliott
    4y line

My View
    who is up / down ?
    who is too expensive / cheap ?
    why PE is so high / low ?
"""

drill_down_7 = [
    (period_ny(years=7), display_args()),
    (period_ny(years=7), display_args(enable_neck_line=True)),
    (period_ny(years=7), display_args(enable_neck_line=True, enable_elliott=True)),
    (period_ny(years=7), display_args(enable_neck_line=True, enable_elliott=True, enable_line=True)),
]

drill_down_4 = [
    (period_ny(years=4), display_args()),
    (period_ny(years=4), display_args(enable_neck_line=True, enable_elliott=True)),
    (period_ny(years=4), display_args(enable_neck_line=True, enable_elliott=True, enable_line=True)),
]


spectrum = [
    (period_ny(years=7), display_args(with_high=True)),
    (period_ny(years=4), display_args(with_high=True, with_mid=True, with_guru=True)),
    (period_1y(), display_args(with_high=True, with_mid=True, with_low=True, with_guru=True)),
]

# candidates = get_unexpired_stock_names()

for stock_name in ALL:
    for (from_date, to_date, interval), args in spectrum:  # drill_down
        base_engine = BaseEngine(stock_name, from_date, to_date, interval)
        base_engine.build_graph(**args)

        stock_df, fig = base_engine.stock_df, base_engine.fig
        fig.show()
