import os
import pandas as pd

DATA_DIR = 'financial_data/yahoo'


def load_csv(stock_name, filename):
    path = os.path.join(DATA_DIR, stock_name, '{}.csv'.format(filename))
    if not os.path.exists(path):
        return pd.DataFrame()
    df = pd.read_csv(path, index_col=0)
    return filter_incomplete(df)


def filter_incomplete(df, min_ratio=0.5):
    """Drop columns where less than min_ratio of rows have values."""
    if df.empty:
        return df
    keep = []
    for col in df.columns:
        non_null = df[col].count()
        if non_null >= len(df) * min_ratio:
            keep.append(col)
    return df[keep]


def format_value(v):
    if v != v or v is None:
        return '-'
    if isinstance(v, float) and abs(v) < 100:
        return '{:.2f}'.format(v)
    sign = '-' if v < 0 else ''
    v = abs(v)
    if v >= 1e9:
        return '{}{:.2f}B'.format(sign, v / 1e9)
    if v >= 1e6:
        return '{}{}M'.format(sign, int(v / 1e6))
    if v >= 1e3:
        return '{}{}K'.format(sign, int(v / 1e3))
    return '{}{:.0f}'.format(sign, v)


def print_statement(title, df, fields):
    print('\n===== {} ====='.format(title))
    if df.empty:
        print('  No data')
        return

    periods = [col[:7] for col in df.columns]
    col_width = 14
    label_width = 52

    header = '{:<{w}}'.format('', w=label_width)
    for period in periods:
        header += '{:>{w}}'.format(period, w=col_width)
    print(header)
    print('-' * len(header))

    for field in fields:
        if not field:
            print()
            continue
        line = '{:<{w}}'.format(field, w=label_width)
        for col in df.columns:
            val = df.loc[field, col] if field in df.index else None
            line += '{:>{w}}'.format(format_value(val), w=col_width)
        print(line)
