import pandas as pd

from util import get_idx_by_date


def _hit(target_price, price, margin: float) -> bool:
    return target_price * (1 - margin) <= price <= target_price * (1 + margin)


# line: (dates, prices)
def _calculate_hits(stock_df: pd.DataFrame, line) -> list:
    dates, prices = line
    high, low, close = stock_df['high'], stock_df['low'], stock_df['close']

    hits = []

    for date, price in zip(dates[5:], prices[5:]):
        if date not in stock_df['Date'].values:
            continue

        idx = get_idx_by_date(stock_df, date)
        target_price = price * 1.03

        touch = _hit(target_price, high[idx], 0.0025) \
                or _hit(target_price, low[idx], 0.0025) \
                or _hit(target_price, close[idx], 0.0025)

        below = close[idx - 5] < prices[idx - 5] \
                or close[idx - 4] < prices[idx - 4] \
                or close[idx - 3] < prices[idx - 3] \
                or close[idx - 2] < prices[idx - 2] \
                or close[idx - 1] < prices[idx - 1]

        if touch and below:
            hits.append(date)

    return hits
