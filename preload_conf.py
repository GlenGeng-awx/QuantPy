from datetime import datetime
from dateutil.relativedelta import relativedelta


# 48m/42m/36m
def period_train(to_date: str, months):
    from_date = (datetime.strptime(to_date, '%Y-%m-%d') - relativedelta(months=months)).strftime('%Y-%m-%d')
    return from_date, to_date, '1d'


# 18m
def period_predict(to_date: str):
    from_date = (datetime.strptime(to_date, '%Y-%m-%d') - relativedelta(months=18)).strftime('%Y-%m-%d')
    return from_date, to_date, '1d'


def period_ny(years: int):
    if years == 7:
        from_date = '2018-01-01'
    elif years == 6:
        from_date = '2019-01-01'
    elif years == 5:
        from_date = '2020-01-01'
    elif years == 4:
        from_date = '2021-01-01'
    elif years == 3:
        from_date = '2022-01-01'
    else:
        raise ValueError(f'unsupported years {years}')
    to_date = datetime.now().strftime('%Y-%m-%d')
    return from_date, to_date, '1d'


def period_1y():
    from_date = (datetime.now() - relativedelta(months=18)).strftime('%Y-%m-%d')
    to_date = datetime.now().strftime('%Y-%m-%d')
    return from_date, to_date, '1d'


def _default_args():
    args = {
        'enable_candlestick': True,
        'enable_close_price': False,

        'enable_min_max': False,
        'enable_sr': False,

        'enable_ec': False,
        'enable_transaction': False,

        'enable_elliott': False,
        'enable_neck_line': False,
        'enable_line': False,

        'enable_implied_neck_line': False,
        'enable_implied_line': False,

        # 5/10/20/60/120/200/250
        'enable_ma': (False, False, False, False, False, False, False),

        'enable_volume': (True, 2),
        'rows': 2,
    }

    return args


def _high_args():
    args = {
        'enable_elliott': True,
        'enable_neck_line': True,
        'enable_line': True,
    }

    return args


def _mid_args():
    args = {
        'enable_implied_neck_line': True,
        'enable_implied_line': True,
    }

    return args


def _low_args():
    args = {
        'enable_sr': True,
        'enable_ec': True,
        'enable_transaction': True,
    }

    return args


def _guru_args():
    args = {
        'enable_guru': (True, 2, 14),  # (True, 2, None)
        'enable_volume': (True, 3),
        'rows': 3
    }

    return args


def display_args(with_high=False, with_mid=False, with_low=False, with_guru=False, **kwargs):
    args = _default_args()
    args.update(kwargs)

    if with_high:
        args.update(_high_args())
    if with_mid:
        args.update(_mid_args())
    if with_low:
        args.update(_low_args())
    if with_guru:
        args.update(_guru_args())

    return args


def model_args():
    args = _default_args()
    args.update(_high_args())
    args.update(_guru_args())
    return args
