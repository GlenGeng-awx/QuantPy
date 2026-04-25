from technical.ma import MA_20, MA_60, MA_120, MA_200
from guru.factor import Factor

MARGIN = 0.0025
OFFSET = 0.03


def _hit(target_price, price, margin):
    return target_price * (1 - margin) <= price <= target_price * (1 + margin)


def _calculate_hits(stock_df, ma_col, up):
    prices = stock_df[ma_col].dropna()
    high, low, close = stock_df['high'], stock_df['low'], stock_df['close']
    multiplier = 1 + OFFSET if up else 1 - OFFSET
    hits = []
    for idx in prices.index[5:]:
        date = stock_df.loc[idx]['Date']
        target_price = prices[idx] * multiplier

        touch = _hit(target_price, high[idx], MARGIN) \
                or _hit(target_price, low[idx], MARGIN) \
                or _hit(target_price, close[idx], MARGIN)

        prev = any((close[idx - i] < prices[idx - i]) if up else (close[idx - i] > prices[idx - i]) for i in range(1, 6))

        if touch and prev:
            hits.append(date)

    return hits


factors = [
    Factor('up thru ma20', 'red', lambda df: _calculate_hits(df, MA_20, up=True)),
    Factor('up thru ma60', 'red', lambda df: _calculate_hits(df, MA_60, up=True)),
    Factor('up thru ma120', 'red', lambda df: _calculate_hits(df, MA_120, up=True)),
    Factor('up thru ma200', 'red', lambda df: _calculate_hits(df, MA_200, up=True)),
    Factor('down thru ma20', 'green', lambda df: _calculate_hits(df, MA_20, up=False)),
    Factor('down thru ma60', 'green', lambda df: _calculate_hits(df, MA_60, up=False)),
    Factor('down thru ma120', 'green', lambda df: _calculate_hits(df, MA_120, up=False)),
    Factor('down thru ma200', 'green', lambda df: _calculate_hits(df, MA_200, up=False)),
]
