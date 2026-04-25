from guru.factor import Factor
from guru.util import pick_top_percentile


def _up_shadow(stock_df):
    _open, close, high = stock_df['open'], stock_df['close'], stock_df['high']
    candidates = []
    for idx in stock_df.index:
        top = max(_open[idx], close[idx])
        candidates.append(((high[idx] - top) / top, idx))
    return pick_top_percentile(stock_df, candidates)


def _down_shadow(stock_df):
    _open, close, low = stock_df['open'], stock_df['close'], stock_df['low']
    candidates = []
    for idx in stock_df.index:
        bottom = min(_open[idx], close[idx])
        candidates.append(((bottom - low[idx]) / bottom, idx))
    return pick_top_percentile(stock_df, candidates)


def _bar(stock_df, red):
    _open, close = stock_df['open'], stock_df['close']
    candidates = []
    for idx in stock_df.index:
        if (close[idx] < _open[idx]) if red else (close[idx] > _open[idx]):
            candidates.append((None, idx))
        else:
            candidates.append((abs(close[idx] - _open[idx]) / _open[idx], idx))
    return pick_top_percentile(stock_df, candidates)


def _range(stock_df, red):
    _open, close = stock_df['open'], stock_df['close']
    high, low = stock_df['high'], stock_df['low']
    candidates = []
    for idx in stock_df.index:
        if (close[idx] < _open[idx]) if red else (close[idx] > _open[idx]):
            candidates.append((None, idx))
        else:
            candidates.append(((high[idx] - low[idx]) / low[idx], idx))
    return pick_top_percentile(stock_df, candidates)


factors = [
    Factor('long up shadow', 'green', _up_shadow),
    Factor('long down shadow', 'red', _down_shadow),
    Factor('long red bar', 'red', lambda df: _bar(df, red=True)),
    Factor('long green bar', 'green', lambda df: _bar(df, red=False)),
    Factor('long red range', 'red', lambda df: _range(df, red=True)),
    Factor('long green range', 'green', lambda df: _range(df, red=False)),
]
