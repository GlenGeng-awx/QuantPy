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


# calculates: list of (value, idx)
def _pick_10pst(stock_df: pd.DataFrame, candidates: list) -> list:
    candidates.sort(key=lambda x: x[0], reverse=True)
    reserved = int(len(candidates) * 0.1)

    hits = []
    for i in range(reserved):
        idx = candidates[i][1]
        hits.append(stock_df['Date'][idx])
    return hits
