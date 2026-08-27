"""
估值倍数 + close (display, 不进 ranking/count)。

6 列: Close + P/E + P/S + P/B + FCF yield + EV/EBITDA
ETF/BTC 无 fundamentals → 全 '-' (仅 close)。
FCF<=0 → '-'；多币种 EV/EBITDA 不可信 → '-' (见 docs.v2 §07)。

返回 2-tuple (value, detail) — display 契约 (无 hit, 不进 ranking), 与 check_* 的 3-tuple 区分。
"""
from fundamental.data import format_value, get_info_val


def display_close(data):
    stock_df = data['stock_df']
    if stock_df.empty:
        return '-', ''
    close = float(stock_df['close'].iloc[-1])
    return '{:.1f}'.format(close), 'Close {:.2f}'.format(close)


def display_pe(data):
    info = data['info']
    pe = get_info_val(info, 'trailingPE')
    if pe is None or pe <= 0:
        return '-', ''
    return '{:.1f}x'.format(pe), 'P={}, E={}'.format(info.get('currentPrice'), info.get('trailingEps'))


def display_ps(data):
    info = data['info']
    ps = get_info_val(info, 'priceToSalesTrailing12Months')
    if ps is None or ps <= 0:
        return '-', ''
    return '{:.1f}x'.format(ps), 'MCap={}, Rev={}'.format(format_value(info.get('marketCap')), format_value(info.get('totalRevenue')))


def display_pb(data):
    info = data['info']
    pb = get_info_val(info, 'priceToBook')
    if pb is None or pb <= 0:
        return '-', ''
    return '{:.1f}x'.format(pb), 'BV={}'.format(info.get('bookValue'))


def display_fcf_yield(data):
    fcf = data.get('fcf')
    info = data['info']
    mcap = info.get('marketCap')
    if fcf is None or mcap is None or mcap <= 0:
        return '-', ''
    yld = fcf / mcap * 100
    if yld <= 0:
        return '-', 'FCF<=0 (negative yield)'
    return '{:.1f}%'.format(yld), 'FCF={}, MCap={}'.format(format_value(fcf), format_value(mcap))


def display_ev_ebitda(data):
    info = data['info']
    if str(info.get('financialCurrency', 'USD')).upper() != 'USD':
        return '-', 'multi-currency EV/E unreliable (见 §07)'
    ev_ratio = get_info_val(info, 'enterpriseToEbitda')
    if ev_ratio is None or ev_ratio <= 0:
        return '-', ''
    return '{:.1f}x'.format(ev_ratio), 'EV={}, EBITDA={}'.format(format_value(info.get('enterpriseValue')), format_value(info.get('ebitda')))


# ---------- registries ----------
VALUATION = [display_close, display_pe, display_ps, display_pb, display_fcf_yield, display_ev_ebitda]
VALUATION_LABELS = ['Close', 'P/E', 'P/S', 'P/B', 'FCF%', 'EV/E']
VALUATION_SHORT = ['Close', 'P/E', 'P/S', 'P/B', 'FCF', 'EV/E']
