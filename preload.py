from base_engine import BaseEngine
from preload_conf import *
from conf import *
from transaction_book import get_unexpired_stock_names

spectrum = [
    (period_4y(), display_args()),
    (period_4y(), display_args(with_high=True)),
    (period_4y(), display_args(with_high=True, with_mid=True)),
    (period_1y(), display_args(with_high=True, with_mid=True, with_low=True, with_guru=True)),
]

for stock_name in V_INDEX + ALL:
    for (from_date, to_date, interval), args in spectrum:
        base_engine = BaseEngine(stock_name, from_date, to_date, interval)
        base_engine.build_graph(**args)

        stock_df, fig = base_engine.stock_df, base_engine.fig
        fig.show()
