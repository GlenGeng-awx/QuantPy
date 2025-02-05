from datetime import datetime
from base_engine import BaseEngine
import features


def _default_period() -> tuple:
    current_date = datetime.now()

    date_2y_ago = datetime(current_date.year - 2, 1, 1).strftime('%Y-%m-%d')
    current_date = current_date.strftime('%Y-%m-%d')

    return date_2y_ago, current_date, '1d'


def preload(stock_name: str) -> BaseEngine:
    base_engine = BaseEngine(stock_name, *_default_period())

    base_engine.build_graph(
        # enable_candlestick=True,
        enable_wave=True,
        enable_box=False,
        enable_min_max=True,
        enable_sr=True,
        enable_line=True,
        enable_close_price=False,
        # enable_position=False,
        enable_volume_reg=(True, 3),
        enable_bband_pst=(True, 4),
        enable_rsi=(True, 5),
        enable_macd=(True, 6),
        rows=6,
    )

    stock_df, fig = base_engine.stock_df, base_engine.fig

    stock_df = features.calculate_feature(stock_df)
    features.plot_feature(stock_df, fig)

    base_engine.stock_df = stock_df
    return base_engine


if __name__ == '__main__':
    from conf import *
    from trading.position import POSITION
    from technical.core_banking import CORE_BANKING

    candidates = [INTC, LI]

    # for _stock_name in POSITION.keys():
    # for _stock_name in [k for k, v in CORE_BANKING.items() if 'elliott' in v]:
    for _stock_name in ALL:
        _base_engine = preload(_stock_name)
        _fig = _base_engine.fig
        _fig.show()
