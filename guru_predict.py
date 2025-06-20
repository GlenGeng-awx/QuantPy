from base_engine import BaseEngine
from conf import *
from preload_conf import *
import guru

spectrum = [
    (period_4y(), args_4y_guru()),
    (period_1y(), args_1y_guru()),
]

for stock_name in ALL:
    for (from_date, to_date, interval), args in spectrum:
        base_engine = BaseEngine(stock_name, from_date, to_date, interval)
        base_engine.build_graph(**args)

        stock_df, fig, context = base_engine.stock_df, base_engine.fig, base_engine.context

        if guru.predict.predict(stock_df, fig, stock_name, context):
            fig.show()
