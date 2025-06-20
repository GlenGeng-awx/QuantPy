from base_engine import BaseEngine
from conf import *
from preload_conf import *
import guru

spectrum = [
    (period_4y(), args_4y_guru()),
]

for stock_name in ALL:
    for (from_date, to_date, interval), args in spectrum:
        base_engine = BaseEngine(stock_name, from_date, to_date, interval)
        base_engine.build_graph(**args)

        stock_df, context = base_engine.stock_df, base_engine.context
        guru.train.train(stock_df, stock_name, context)
