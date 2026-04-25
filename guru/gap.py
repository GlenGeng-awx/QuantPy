from guru.factor import Factor


def _up_gap(stock_df):
    dates = stock_df['Date']
    high, low, close = stock_df['high'], stock_df['low'], stock_df['close']

    hits = []
    for idx in stock_df.index[1:]:
        if low[idx] > high[idx - 1] and (low[idx] - high[idx - 1]) / close[idx - 1] > 0.01:
            hits.append(dates[idx])
    return hits


def _down_gap(stock_df):
    dates = stock_df['Date']
    high, low, close = stock_df['high'], stock_df['low'], stock_df['close']

    hits = []
    for idx in stock_df.index[1:]:
        if high[idx] < low[idx - 1] and (low[idx - 1] - high[idx]) / close[idx - 1] > 0.01:
            hits.append(dates[idx])
    return hits


factors = [
    Factor('up gap', 'red', _up_gap),
    Factor('down gap', 'green', _down_gap),
]
