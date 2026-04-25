from guru.factor import Factor


def _consecutive(stock_df, ascending):
    dates = stock_df['Date']
    close = stock_df['close']
    hits = []
    for idx in stock_df.index[5:]:
        if all((close[idx - i] < close[idx - i + 1]) if ascending else (close[idx - i] > close[idx - i + 1]) for i in range(5, 0, -1)):
            hits.append(dates[idx])
    return hits


factors = [
    Factor('incr 5d', 'red', lambda df: _consecutive(df, ascending=True)),
    Factor('decr 5d', 'green', lambda df: _consecutive(df, ascending=False)),
]
