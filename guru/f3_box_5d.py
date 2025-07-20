import pandas as pd
from guru.f3_box import _calculate_hits

KEY = 'box 5d'


def calculate_hits(stock_df: pd.DataFrame) -> list:
    return _calculate_hits(stock_df, sz=5, key=KEY)
