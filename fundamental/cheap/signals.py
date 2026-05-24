from fundamental.data import format_value, get_info_val


def _drawdown(stock_df, days):
    if stock_df.shape[0] < days:
        return None, '-', ''
    week_low = float(stock_df['close'].iloc[-5:].min())
    period_high = float(stock_df['close'].iloc[-days:].max())
    dd = (period_high - week_low) / period_high * 100
    return dd, '{:.0f}%'.format(dd), 'Low {:.1f} vs High {:.1f}'.format(week_low, period_high)


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
    if stock_df.shape[0] < 252:
        return False, '-', ''
    current = float(stock_df['close'].iloc[-1])
    low_52w = float(stock_df['close'].iloc[-252:].min())
    above = (current - low_52w) / low_52w * 100
    value = '+{:.0f}%'.format(above)
    detail = 'Cur {:.1f} vs Low {:.1f}'.format(current, low_52w)
    return above <= 15, value, detail


def check_pe(data):
    info = data['info']
    pe = get_info_val(info,'trailingPE')
    if pe is None or pe <= 0:
        return False, '-', ''
    price = info.get('currentPrice')
    price = '{:.1f}'.format(price) if price else '-'
    eps = info.get('trailingEps')
    eps = '{:.2f}'.format(eps) if eps else '-'
    return pe < 15, '{:.1f}x'.format(pe), 'P={}, E={}'.format(price, eps)


def check_ev_ebitda(data):
    info = data['info']
    ev_ratio = get_info_val(info,'enterpriseToEbitda')
    if ev_ratio is None or ev_ratio <= 0:
        return False, '-', ''
    ev = info.get('enterpriseValue')
    ev = format_value(ev) if ev else '-'
    ebitda = info.get('ebitda')
    ebitda = format_value(ebitda) if ebitda else '-'
    return ev_ratio < 10, '{:.1f}x'.format(ev_ratio), 'EV={}, EBITDA={}'.format(ev, ebitda)


def check_ps(data):
    info = data['info']
    ps = get_info_val(info,'priceToSalesTrailing12Months')
    if ps is None or ps <= 0:
        return False, '-', ''
    mcap = info.get('marketCap')
    mcap = format_value(mcap) if mcap else '-'
    rev = info.get('totalRevenue')
    rev = format_value(rev) if rev else '-'
    return ps < 2.0, '{:.1f}x'.format(ps), 'MCap={}, Rev={}'.format(mcap, rev)


CHECKS = [check_1y_drawdown, check_2y_drawdown, check_near_52w_low,
          check_pe, check_ev_ebitda, check_ps]
LABELS = ['1Y Drawdown', '2Y Drawdown', 'Near 52W Low',
          'P/E TTM', 'EV/EBITDA', 'P/S']
SHORT = ['1Y', '2Y', '52W', 'P/E', 'EV/E', 'P/S']
