from datetime import datetime
from dateutil.relativedelta import relativedelta


# 48m/42m/36m
def period_train(to_date: str, months):
    from_date = (datetime.strptime(to_date, '%Y-%m-%d') - relativedelta(months=months)).strftime('%Y-%m-%d')
    return from_date, to_date, '1d'


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


def default_args():
    args = {
        'enable_candlestick': True,
        'enable_close_price': False,

        'enable_min_max': False,
        'enable_sr': False,

        'enable_elliott': False,
        'enable_fs': False,

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


def guru_args():
    args = {
        'enable_guru': (True, 2, 14),  # (True, 2, None)
        'enable_volume': (True, 3),
        'rows': 3
    }

    return args


def args_4y():
    customized = {
        'enable_sr': False,
        'enable_elliott': True,
        'enable_fs': False,
        'enable_line': True,
        'enable_neck_line': True,
        'enable_implied_line': True,
        'enable_implied_neck_line': True,
    }

    args = default_args()
    args.update(customized)
    return args


def args_4y_guru():
    args = args_4y()
    args.update(guru_args())
    return args


def args_1y():
    customized = {
        'enable_sr': True,
        'enable_elliott': False,
        'enable_fs': True,
        'enable_line': True,
        'enable_neck_line': True,
        'enable_implied_line': True,
        'enable_implied_neck_line': True,
    }

    args = default_args()
    args.update(customized)
    return args


def args_1y_guru():
    args = args_1y()
    args.update(guru_args())
    return args
