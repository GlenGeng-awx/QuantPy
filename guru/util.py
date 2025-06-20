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
def _pick_rolling_10pst(stock_df: pd.DataFrame, candidates: list, tag: str, rolling_size: int = 200) -> list:
    hits = []

    for i in range(rolling_size, len(candidates)):
        value, idx = candidates[i]

        rolling_window = candidates[i - rolling_size:i]
        rolling_window.sort(key=lambda x: x[0], reverse=True)

        threshold_pos = int(len(rolling_window) * 0.1) - 1
        threshold_value = rolling_window[threshold_pos][0]

        if value >= threshold_value:
            date = stock_df['Date'][idx]
            hits.append(date)
            # print(f'tag = {tag}, date = {date}, value = {value}, threshold_value = {threshold_value}')

    return hits
