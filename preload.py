from datetime import datetime

import pandas as pd
from dateutil.relativedelta import relativedelta
from base_engine import BaseEngine
from demo import pick


def default_periods() -> list[tuple]:
    current_date = datetime.now()

    start_date_4y = (current_date - relativedelta(months=48)).strftime('%Y-%m-%d')
    start_date_1y = (current_date - relativedelta(months=12)).strftime('%Y-%m-%d')
    current_date = current_date.strftime('%Y-%m-%d')

    return [
        (start_date_4y, current_date, '1d'),
        (start_date_1y, current_date, '1d'),
    ]


def preload(stock_name: str, from_date: str, to_date: str, interval: str, **kwargs) -> BaseEngine:
    base_engine = BaseEngine(stock_name, from_date, to_date, interval)

    default_args = {
        'enable_candlestick': True,
        'enable_close_price': False,

        'enable_min_max': False,

        'enable_sr': False,             #
        'enable_elliott': False,        #
        'enable_neck_line': False,      #

        'enable_line_expo': False,      #
        'enable_line': False,           #

        'enable_tech': False,
        'enable_rd': False,
        'enable_gap': False,

        'enable_ma20': False,
        'enable_ma60': False,
        'enable_ma120': False,

        'enable_volume': (True, 2),
        'enable_bband_pst': (True, 3),
        'enable_rsi': (True, 4),
        'enable_macd': (True, 5),

        'guru_start_date': '2000-01-01',
        'guru_end_date': '2099-12-31',

        'enable_hit_elliott': False,
        'enable_hit_line': False,
        'enable_hit_line_expo': False,
        'enable_hit_neck_line': False,
        'enable_hit_sr': False,
        'enable_hit_ma20': False,
        'enable_hit_ma60': False,
        'enable_hit_ma120': False,
        'enable_hit_low_vol': (False, 2),
        'enable_hit_high_vol': (False, 2),

        'rows': 2,
    }

    common_args = {
        'enable_sr': True,
        'enable_elliott': True,
        'enable_neck_line': False,
    }

    linear_args = {
        'enable_line': True,
    }

    log_args = {
        'enable_line_expo': True,
    }

    default_args.update(common_args)

    if base_engine.yaxis_type == 'linear':
        default_args.update(linear_args)
    else:
        default_args.update(log_args)

    default_args.update(kwargs)
    base_engine.build_graph(**default_args)

    return base_engine


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

    for _stock_name in ALL:
        for _from_date, _to_date, _interval in default_periods():
            _base_engine = preload(_stock_name, _from_date, _to_date, _interval)
            _stock_df, _fig = _base_engine.stock_df, _base_engine.fig

            _fig.show()
