"""
价格回撤信号 (入场条件, 进 ranking/count)。

6 信号:
    1Y Drawdown   > 40%     过去一周低点 vs 一年高点
    2Y Drawdown   > 60%     过去一周低点 vs 两年高点
    Near 52W Low  ≤ 15%     现价距 52 周低
    crash5d/10d/20d         近 3 交易日 guru 90pct 回撤命中 (rolling 200d)

crash: guru price_move 因子, pick_top_percentile(ratio=0.1) = 滚动 200 日 90pct 回撤日。
"""
from util import shrink_date_str

CRASH_WINDOW = 3  # 近 3 交易日发生 crash


# ---------- helpers ----------
def _drawdown(stock_df, days):
    # days 不够时用全部可用历史 (如 SPCX 上市<1年); iloc[-days:] 自动 clip
    closes = stock_df['close']
    period_high = float(closes.iloc[-days:].max())
    if period_high <= 0:
        return None, '-', ''
    week_low = float(closes.iloc[-5:].min())
    dd = (period_high - week_low) / period_high * 100
    return dd, '{:.0f}%'.format(dd), 'Low {:.1f} vs High {:.1f}'.format(week_low, period_high)


def _check_crash(data, key):
    stock_df = data['stock_df']
    guru_ctx = data.get('guru_context') or {}
    hit_dates = guru_ctx.get(key) or []
    if not hit_dates:
        return False, '-', ''
    recent = set(shrink_date_str(d) for d in stock_df['Date'].iloc[-CRASH_WINDOW:].values)
    hits = [d for d in hit_dates if shrink_date_str(d) in recent]
    if hits:
        return True, '✓', '{} @ {}'.format(key, shrink_date_str(hits[-1]))
    return False, '-', ''


# ---------- checks ----------
def check_1y_drawdown(data):
    dd, value, detail = _drawdown(data['stock_df'], 252)
    if dd is None:
        return False, value, detail
    return dd > 40, value, detail


def check_2y_drawdown(data):
    dd, value, detail = _drawdown(data['stock_df'], 504)
    if dd is None:
        return False, value, detail
    return dd > 60, value, detail


def check_near_52w_low(data):
    stock_df = data['stock_df']
    if stock_df.empty:
        return False, '-', ''
    closes = stock_df['close']
    current = float(closes.iloc[-1])
    low_52w = float(closes.iloc[-252:].min())  # 短历史自动 clip 到可用
    if low_52w <= 0:
        return False, '-', ''
    above = (current - low_52w) / low_52w * 100
    value = '+{:.0f}%'.format(above)
    detail = 'Cur {:.1f} vs Low {:.1f}'.format(current, low_52w)
    return above <= 15, value, detail


def check_crash5d(data):
    return _check_crash(data, 'crash 5d')


def check_crash10d(data):
    return _check_crash(data, 'crash 10d')


def check_crash20d(data):
    return _check_crash(data, 'crash 20d')


# ---------- registries ----------
PRICE = [check_1y_drawdown, check_2y_drawdown, check_near_52w_low,
         check_crash5d, check_crash10d, check_crash20d]
PRICE_LABELS = ['1Y DD', '2Y DD', '52W', 'crash5d', 'crash10d', 'crash20d']
PRICE_SHORT = ['1Y', '2Y', '52W', 'c5d', 'c10d', 'c20d']
