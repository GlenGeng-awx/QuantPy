import pandas as pd

from base_engine import BaseEngine
from demo import pick
from preload_impl import *


def select_dates(stock_df: pd.DataFrame) -> list:
    offset = 0
    dates = [
        stock_df['Date'].iloc[-5 - offset],
        stock_df['Date'].iloc[-4 - offset],
        stock_df['Date'].iloc[-3 - offset],
        stock_df['Date'].iloc[-2 - offset],
        stock_df['Date'].iloc[-1 - offset],
    ]
    print(dates)
    return dates


if __name__ == '__main__':
    from conf import *

    # candidates = []
    #
    # for _stock_name in ALL:
    #     _from_date, _to_date, _interval = default_periods()[0]
    #     _base_engine = preload(_stock_name, _from_date, _to_date, _interval)
    #
    #     selected_dates = select_dates(_base_engine.stock_df)
    #     var_p, var_v = pick(_base_engine, selected_dates)
    #     # if var_p and var_v:
    #     if var_p:
    #         print(_stock_name, var_p, var_v)
    #         candidates.append(_stock_name)
    #
    #         _base_engine = preload(_stock_name, _from_date, _to_date, _interval,
    #                                **dict(var_p + var_v),
    #                                guru_start_date=selected_dates[0], guru_end_date=selected_dates[-1])
    #         _stock_df, _fig = _base_engine.stock_df, _base_engine.fig
    #         _fig.show()
    #
    # print(candidates)
    # candidates = ['QQQ', '^IXIC', 'KWEB', '000300.SS', '000001.SS', 'AAPL', 'GOOG', 'JPM', 'MA', 'V', 'NFLX', 'NVO', 'XOM', 'PG', 'KO', 'BAC', 'GS', 'MS', 'ADBE', 'PLTR', 'AMD', 'QCOM', 'GILD', 'UBER', 'PDD', 'SPOT', 'PYPL', 'NU', 'EBAY', 'CPNG', 'HPQ', 'LI', 'BNTX', 'ZM', 'FUTU', 'GTLB']
    #

    put = [DELL, AVGO, PLTR, TSM, COIN, BA]
    call = [EDU, AMD, GOOG, INTC]
    position = [QQQ, COIN, TSM, BA, DELL, AMD, PLTR, INTC, GOOG, AVGO, EDU]

    spectrum = [
        (period_4y(), args_4y()),
        (period_1y(), args_1y()),
    ]

    for stock_name in ALL[10:20]:
        for (from_date, to_date, interval), args in spectrum:
            base_engine = BaseEngine(stock_name, from_date, to_date, interval)
            base_engine.build_graph(**args)

            stock_df, fig = base_engine.stock_df, base_engine.fig
            fig.show()
