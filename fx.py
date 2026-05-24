from conf import *

FX = {
    'USD': 1.0,
    'HKD': 7.83,
    'CNY': 6.81,
    'TWD': 31.7,
    'DKK': 6.44,
    'EUR': 0.86,
    'SEK': 9.37,
}

TRADING = {
    TENCENT: FX['HKD'],
}


def to_usd(amount, stock_name, scenario=TRADING):
    rate = scenario.get(stock_name, 1.0)
    return amount / rate


def correct_ratio(info, key):
    val = info.get(key)
    if not val:
        return None
    fin_fx = FX.get(info.get('financialCurrency', 'USD'), 1.0)
    cur_fx = FX.get(info.get('currency', 'USD'), 1.0)
    return val * fin_fx / cur_fx
