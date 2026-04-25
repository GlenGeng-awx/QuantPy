from guru.factor import Factor
from guru.util import pick_top_percentile


def _calculate_hits(stock_df, sz, crash):
    close = stock_df['close']
    candidates = []

    for idx in stock_df.index[sz:]:
        diff = close[idx - sz] - close[idx] if crash else close[idx] - close[idx - sz]
        if diff <= 0:
            candidates.append((None, idx))
        else:
            candidates.append((diff / close[idx - sz], idx))

    return pick_top_percentile(stock_df, candidates)


factors = [
    Factor('crash 5d', 'green', lambda df: _calculate_hits(df, 5, crash=True)),
    Factor('crash 10d', 'green', lambda df: _calculate_hits(df, 10, crash=True)),
    Factor('crash 20d', 'green', lambda df: _calculate_hits(df, 20, crash=True)),
    Factor('spike 5d', 'red', lambda df: _calculate_hits(df, 5, crash=False)),
    Factor('spike 10d', 'red', lambda df: _calculate_hits(df, 10, crash=False)),
    Factor('spike 20d', 'red', lambda df: _calculate_hits(df, 20, crash=False)),
]
