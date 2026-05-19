from technical.min_max import LOCAL_MAX_PRICE_4TH, LOCAL_MIN_PRICE_4TH
from util import shrink_date_str, get_idx_by_date

TOLERANCE = 0.03


def _recent_closes(stock_df, n=5):
    return [float(v) for v in stock_df['close'].iloc[-n:].values]


def _hit_price(closes, target):
    for close in closes:
        if abs(close - target) / target <= TOLERANCE:
            return close
    return None


def check_elliott_hit(data):
    stock_df = data['stock_df']
    elliott_dates = data['elliott_dates']
    if not elliott_dates:
        return False, '', ''
    prices = []
    for date in elliott_dates:
        try:
            idx = get_idx_by_date(stock_df, date)
            prices.append(float(stock_df.loc[idx]['close']))
        except (IndexError, KeyError):
            print('  warn: elliott date {} not found in {}'.format(date, data.get('stock_name', '?')))
            continue
    if not prices:
        return False, '', ''
    closes = _recent_closes(stock_df)
    for target in prices:
        hit = _hit_price(closes, target)
        if hit:
            return True, '{:.1f}'.format(target), 'Close {:.1f} near {:.1f}'.format(hit, target)
    return False, '', ''


def check_neck_line_hit(data):
    stock_df = data['stock_df']
    neck_lines = data['neck_lines']
    if not neck_lines:
        return False, '', ''
    closes = _recent_closes(stock_df)
    for dates, prices in neck_lines:
        target = prices[0]
        hit = _hit_price(closes, target)
        if hit:
            return True, '{:.1f}'.format(target), 'Close {:.1f} near {:.1f}'.format(hit, target)
    return False, '', ''


def check_trend_line_hit(data):
    primary = data['primary_lines']
    secondary = data['secondary_lines']
    all_lines = primary + secondary
    if not all_lines:
        return False, '', ''
    stock_df = data['stock_df']
    recent = stock_df.iloc[-5:]
    date_close = {shrink_date_str(row['Date']): float(row['close']) for _, row in recent.iterrows()}
    for line in all_lines:
        for date, target in zip(line[0], line[1]):
            d = shrink_date_str(date)
            if d in date_close:
                close = date_close[d]
                if abs(close - target) / target <= TOLERANCE:
                    return True, '{:.1f}'.format(target), 'Close {:.1f} near line {:.1f}'.format(close, target)
    return False, '', ''


def check_minmax_hit(data):
    stock_df = data['stock_df']
    minmax_df = stock_df[stock_df[LOCAL_MAX_PRICE_4TH] | stock_df[LOCAL_MIN_PRICE_4TH]]
    if minmax_df.empty:
        return False, '', ''
    targets = [float(v) for v in minmax_df['close'].values]
    closes = _recent_closes(stock_df)
    for target in targets:
        hit = _hit_price(closes, target)
        if hit:
            return True, '{:.1f}'.format(target), 'Close {:.1f} near {:.1f}'.format(hit, target)
    return False, '', ''


CHECKS = [check_elliott_hit, check_neck_line_hit, check_trend_line_hit, check_minmax_hit]
LABELS = ['Elliott', 'Neck Line', 'Trend Line', 'MinMax 4th']
SHORT = ['Elli', 'Neck', 'Line', '4th']
