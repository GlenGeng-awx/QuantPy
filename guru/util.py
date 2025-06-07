import pandas as pd

from util import get_idx_by_date, shrink_date_str


def _hit(target_price, price, margin: float) -> bool:
    return target_price * (1 - margin) <= price <= target_price * (1 + margin)


# line: (dates, prices)
def _calculate_hits(stock_df: pd.DataFrame, line, margin) -> list:
    dates, prices = line
    hits = []

    for date, price in zip(dates, prices):
        if date not in stock_df['Date'].values:
            continue

        idx = get_idx_by_date(stock_df, shrink_date_str(date))
        high, low, close = stock_df.loc[idx]['high'], stock_df.loc[idx]['low'], stock_df.loc[idx]['close']

        if _hit(price, high, margin) \
                or _hit(price, low, margin) \
                or _hit(price, close, margin):
            hits.append(date)

    return hits
