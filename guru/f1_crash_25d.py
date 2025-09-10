import pandas as pd
from guru.f1_crash import _calculate_hits

KEY = 'crash 25d'


def calculate_hits(stock_df: pd.DataFrame) -> list:
    return _calculate_hits(stock_df, sz=25, key=KEY)
