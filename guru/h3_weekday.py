import pandas as pd


# 0/1/2/3/4 -> Monday/Tuesday/Wednesday/Thursday/Friday
def _calculate_hits(stock_df: pd.DataFrame, i: int) -> list:
    dates = []

    for date, ts in zip(stock_df['Date'], pd.to_datetime(stock_df['Date'], utc=True)):
        if ts.weekday() == i:
            dates.append(date)

    return dates
