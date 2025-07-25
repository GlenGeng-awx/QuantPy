import pandas as pd
from guru.e4_vol_box import _calculate_hits

KEY = 'vol box 10d'


def calculate_hits(stock_df: pd.DataFrame) -> list:
    return _calculate_hits(stock_df, sz=10, key=KEY)
