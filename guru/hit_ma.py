from technical.ma import MA_20, MA_60, MA_120, MA_200
from guru.factor import Factor

MARGIN = 0.005


def _hit(target_price, price, margin):
    return target_price * (1 - margin) <= price <= target_price * (1 + margin)


def _calculate_hits(stock_df, ma_col):
    prices = stock_df[ma_col].dropna()
    hits = []

    for idx in prices.index:
        date = stock_df.loc[idx]['Date']
        high, low, close = stock_df.loc[idx]['high'], stock_df.loc[idx]['low'], stock_df.loc[idx]['close']
        price = prices[idx]

        if _hit(price, high, MARGIN) or _hit(price, low, MARGIN) or _hit(price, close, MARGIN):
            hits.append(date)

    return hits


factors = [
    Factor('hit ma20', 'black', lambda df: _calculate_hits(df, MA_20)),
    Factor('hit ma60', 'black', lambda df: _calculate_hits(df, MA_60)),
    Factor('hit ma120', 'black', lambda df: _calculate_hits(df, MA_120)),
    Factor('hit ma200', 'black', lambda df: _calculate_hits(df, MA_200)),
]
