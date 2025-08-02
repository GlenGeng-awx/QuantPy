import pandas as pd
from guru.e4_vol_box import _calculate_hits

KEY = 'vol box 20d'


def calculate_hits(stock_df: pd.DataFrame) -> list:
    return _calculate_hits(stock_df, sz=20, key=KEY)
