from datetime import datetime
from dateutil.relativedelta import relativedelta


def period_4y():
    from_date = (datetime.now() - relativedelta(months=48)).strftime('%Y-%m-%d')
    to_date = datetime.now().strftime('%Y-%m-%d')
    return from_date, to_date, '1d'


def period_1y():
    from_date = (datetime.now() - relativedelta(months=12)).strftime('%Y-%m-%d')
    to_date = datetime.now().strftime('%Y-%m-%d')
    return from_date, to_date, '1d'


def default_args():
    args = {
        'enable_candlestick': True,
        'enable_close_price': False,

        'enable_min_max': False,
        'enable_sr': False,         #

        'enable_elliott': False,    #
        'enable_tech': False,       #

        'enable_line': False,       #
        'enable_neck_line': False,  #

        'enable_rd': False,
        'enable_gap': False,

        'enable_ma20': False,
        'enable_ma60': False,
        'enable_ma120': False,

        'enable_volume': (True, 2),

        'guru_start_date': '2000-01-01',
        'guru_end_date': '2099-12-31',

        'enable_hit_elliott': False,
        'enable_hit_line': False,
        'enable_hit_line_expo': False,
        'enable_hit_neck_line': False,
        'enable_hit_sr': False,
        'enable_hit_ma20': False,
        'enable_hit_ma60': False,
        'enable_hit_ma120': False,
        'enable_hit_low_vol': (False, 2),
        'enable_hit_high_vol': (False, 2),

        'rows': 2,
    }

    return args


def args_4y():
    customized = {
        'enable_sr': False,
        'enable_elliott': True,     #
        'enable_tech': False,
        'enable_line': True,        #
        'enable_neck_line': False,
    }

    args = default_args()
    args.update(customized)
    return args


def args_1y():
    customized = {
        'enable_sr': True,          #
        'enable_elliott': False,
        'enable_tech': True,        #
        'enable_line': True,        #
        'enable_neck_line': True,   #
    }

    args = default_args()
    args.update(customized)
    return args
