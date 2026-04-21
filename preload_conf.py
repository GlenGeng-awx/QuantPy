from datetime import datetime


def period(years):
    from_date = f'{datetime.now().year - years}-01-01'
    to_date = datetime.now().strftime('%Y-%m-%d')
    return from_date, to_date, '1d'


_BASE = {
    'enable_candlestick': True,
    'enable_close_price': False,
    'enable_min_max': False,
    'enable_sr': False,
    'enable_earnings_call': False,
    'enable_elliott': False,
    'enable_neck_line': False,
    'enable_line': False,
    'enable_implied_neck_line': False,
    'enable_implied_line': False,
    'enable_ma': (False, False, False, False, False, False, False),
    'enable_volume': (True, 2),
    'enable_guru': (False, 2),
    'rows': 2,
}

FULL = {
    **_BASE,
    'enable_elliott': True,
    'enable_neck_line': True,
    'enable_line': True,
}

FOUR_YEAR = {
    **FULL,
    'enable_implied_neck_line': True,
    'enable_implied_line': True,
}

TWO_YEAR = {
    **FOUR_YEAR,
    'enable_sr': True,
    'enable_earnings_call': True,
    'enable_guru': (True, 2),
    'enable_volume': (True, 3),
    'rows': 3,
}


def with_overrides(preset, **kwargs):
    return {**preset, **kwargs}
