import pandas as pd
from guru.f7_weekday import _calculate_hits

KEY = 'tuesday'


def calculate_hits(stock_df: pd.DataFrame) -> list:
    return _calculate_hits(stock_df, 1)
