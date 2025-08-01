import pandas as pd
from guru.h3_weekday import _calculate_hits

KEY = 'friday'


def calculate_hits(stock_df: pd.DataFrame) -> list:
    return _calculate_hits(stock_df, 4)
