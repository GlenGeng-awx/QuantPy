from base_engine import BaseEngine
from preload_conf import *
from x_position import *

spectrum = [
    (period_4y(), args_4y()),
    # (period_1y(), args_1y()),
    # (period_4y(), args_4y_guru()),
    (period_1y(), args_1y_guru()),
]

for stock_name in ALL:
    for (from_date, to_date, interval), args in spectrum:
        base_engine = BaseEngine(stock_name, from_date, to_date, interval)
        base_engine.build_graph(**args)

        stock_df, fig = base_engine.stock_df, base_engine.fig
        fig.show()
