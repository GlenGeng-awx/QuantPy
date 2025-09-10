import pandas as pd
from guru.f3_box import _calculate_hits

KEY = 'box 30d'


def calculate_hits(stock_df: pd.DataFrame) -> list:
    return _calculate_hits(stock_df, sz=30, key=KEY)
