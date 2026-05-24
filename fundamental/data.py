import os
import json
import pandas as pd

from conf import CN_INDEX, US_INDEX

STATEMENT_DIR = 'financial_data'
PRICE_DIR = 'stock_data'
SKIP = set(CN_INDEX + US_INDEX)


def filter_incomplete(df, min_ratio=0.5):
    if df.empty:
        return df
    keep = [col for col in df.columns if df[col].count() >= len(df) * min_ratio]
    return df[keep]


def load_statement(stock_name, filename):
    path = os.path.join(STATEMENT_DIR, stock_name, '{}.csv'.format(filename))
    if not os.path.exists(path):
        return pd.DataFrame()
    df = pd.read_csv(path, index_col=0)
    return filter_incomplete(df)


def load_info(stock_name):
    path = os.path.join(STATEMENT_DIR, stock_name, 'info.json')
    if not os.path.exists(path):
        return {}
    with open(path) as f:
        return json.load(f)


def load_price(stock_name):
    path = os.path.join(PRICE_DIR, '{}_1d.csv'.format(stock_name))
    if not os.path.exists(path):
        return pd.DataFrame()
    return pd.read_csv(path)


def get_val(df, field, col_idx=0):
    if df.empty or field not in df.index or col_idx >= len(df.columns):
        return None
    val = df.loc[field].iloc[col_idx]
    if pd.isna(val):
        return None
    return float(val)


def get_series(df, field, count=None):
    """Returns [(period_str, value), ...] newest first."""
    if df.empty or field not in df.index:
        return []
    if count:
        cols = list(df.columns)[:count]
    else:
        cols = list(df.columns)
    result = []
    for col in cols:
        val = df.loc[field, col]
        if pd.isna(val):
            result.append((col[:7], None))
        else:
            result.append((col[:7], float(val)))
    return result


def get_info_val(info, key):
    """从 info 取值，对已知有 FX 问题的 key 做修正"""
    from fx import correct_ratio
    val = info.get(key)
    if val is None:
        return None
    if key == 'priceToSalesTrailing12Months':
        return correct_ratio(info, key)
    return val


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
