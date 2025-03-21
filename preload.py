from datetime import datetime
from base_engine import BaseEngine
import features


def _default_period() -> tuple:
    current_date = datetime.now()

    date_2y_ago = datetime(current_date.year - 3, 10, 1).strftime('%Y-%m-%d')
    current_date = current_date.strftime('%Y-%m-%d')

    return date_2y_ago, current_date, '1d'


def preload(stock_name: str, **kwargs) -> BaseEngine:
    base_engine = BaseEngine(stock_name, *_default_period())

    default_args = {
        'enable_candlestick': False,
        'enable_close_price': True,
        'enable_wave': False,
        'enable_box': False,
        'enable_min_max': True,
        'enable_sr': True,
        'enable_line': True,
        'enable_position': False,
        'enable_volume': (True, 3),
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

    targets = [META, MSFT, COIN, MRK, JPM, BABA, LI, TCOM, OKTA, VISA, MS, NVO, GS]

    for _stock_name in ALL:
        _base_engine = preload(_stock_name, enable_position=True)
        _stock_df, _fig = _base_engine.stock_df, _base_engine.fig

        _stock_df = features.calculate_feature(_stock_df, _stock_name, True)
        _stock_df = features.calculate_feature(_stock_df, _stock_name, False)
        features.plot_feature(_stock_df, _fig)

        _fig.show()
