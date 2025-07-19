import pandas as pd
from guru.f2_spike import _calculate_hits

KEY = 'spike 1d'


def calculate_hits(stock_df: pd.DataFrame) -> list:
    return _calculate_hits(stock_df, sz=1, key=KEY)
