from datetime import datetime
from dateutil.relativedelta import relativedelta
from base_engine import BaseEngine
import features


def default_periods() -> list[tuple]:
    current_date = datetime.now()

    start_date_3y = (current_date - relativedelta(months=36)).strftime('%Y-%m-%d')
    start_date_2y = (current_date - relativedelta(months=24)).strftime('%Y-%m-%d')
    start_date_1y = (current_date - relativedelta(months=12)).strftime('%Y-%m-%d')
    current_date = current_date.strftime('%Y-%m-%d')

    return [
        # (start_date_3y, start_date_1y, '1d'),
        (start_date_3y, current_date, '1d'),
        (start_date_2y, current_date, '1d'),
        (start_date_1y, current_date, '1d'),
    ]


def preload(stock_name: str, from_date: str, to_date: str, interval: str, **kwargs) -> BaseEngine:
    base_engine = BaseEngine(stock_name, from_date, to_date, interval)

    default_args = {
        'enable_candlestick': False,
        'enable_close_price': True,
        'enable_wave': False,
        'enable_box': False,
        'enable_min_max': True,
        'enable_sr': True,
        'enable_line': True,
        'enable_position': False,
        'enable_volume': (True, 2),
        'enable_bband_pst': (True, 4),
        'enable_rsi': (True, 5),
        'enable_macd': (True, 6),
        'rows': 6,
    }
    default_args.update(kwargs)
    base_engine.build_graph(**default_args)

    return base_engine


if __name__ == '__main__':
    from conf import *

    targets = [NU, AAPL, IQ, BIDU, ZM, DELL, AMD, JPM, META, WMT, MRK, ADBE, CVX, DIS]

    for _stock_name in targets:
        for _from_date, _to_date, _interval in default_periods():
            _base_engine = preload(_stock_name, _from_date, _to_date, _interval, enable_position=False)
            _stock_df, _fig = _base_engine.stock_df, _base_engine.fig

            _stock_df = features.calculate_feature(_stock_df, _stock_name, True)
            _stock_df = features.calculate_feature(_stock_df, _stock_name, False)
            features.plot_feature(_stock_df, _fig)

            _fig.show()
