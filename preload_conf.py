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


def period_4y():
    to_date = datetime.now().strftime('%Y-%m-%d')
    return '2021-01-01', to_date, '1d'


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
        'enable_elliott': False,

        'enable_line': False,
        'enable_neck_line': False,

        # 5/10/20/60/120/200/250
        'enable_ma': (False, False, False, False, False, False, False),

        'enable_implied_neck_line': False,
        'enable_implied_line': False,

        'enable_volume': (True, 2),
        'rows': 2,
    }

    return args


def _high_args():
    args = {
        'enable_elliott': True,
        'enable_line': True,
        'enable_neck_line': True,
    }

    return args


def _mid_args():
    args = {
        'enable_implied_line': True,
        'enable_implied_neck_line': True,
    }

    return args


def _low_args():
    args = {
        'enable_ec': True,
        'enable_sr': True,
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


def display_args(with_high=False, with_mid=False, with_low=False, with_guru=False):
    args = _default_args()
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
