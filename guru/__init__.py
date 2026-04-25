from datetime import datetime
import pandas as pd

from guru.vol import factors as vol
from guru.price_move import factors as price_move
from guru.hit_ma import factors as hit_ma
from guru.thru_ma import factors as thru_ma
from guru.candle import factors as candle
from guru.gap import factors as gap
from guru.price_consecutive import factors as price_consecutive

factors = vol + price_move + hit_ma + thru_ma + candle + gap + price_consecutive


def calculate(stock_df: pd.DataFrame) -> dict:
    context = {}
    start_time = datetime.now()

    for factor in factors:
        dates = factor.calculate_hits(stock_df)
        context[factor.KEY] = dates

    print(f'calculate context cost: {(datetime.now() - start_time).total_seconds()}s')
    return context


import guru.plot
