import pandas as pd

from base_engine import BaseEngine


def _pick(stock_df: pd.DataFrame, dates: list) -> bool:
    return stock_df['Date'].iloc[-2] in dates \
        and stock_df['Date'].iloc[-1] in dates


def pick(base_engine: BaseEngine) -> bool:
    stock_df = base_engine.stock_df

    hit_line = base_engine.hit_line
    line_hits = hit_line.line_hits
    neckline_hits = hit_line.neckline_hits

    # hit_volume = base_engine.hit_volume
    # vol_hits = hit_volume.hits

    if _pick(stock_df, [date for date, _ in line_hits]) \
            or _pick(stock_df, [date for date, _ in neckline_hits]):
        return True

    return False
