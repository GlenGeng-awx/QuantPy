from conf import *

USD_HKD = 7.83
USD_CNY = 6.81
USD_TWD = 31.7

TRADING = {
    TENCENT: USD_HKD,
}


def to_usd(amount, stock_name, scenario=TRADING):
    rate = scenario.get(stock_name, 1.0)
    return amount / rate
