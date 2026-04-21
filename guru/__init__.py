from datetime import datetime
import pandas as pd

from guru import (
    e1_high_vol,
    e1_low_vol,

    e3_vol_incr_5d,
    e3_vol_decr_5d,

    f1_crash_5d,
    f1_crash_10d,
    f1_crash_20d,

    f2_spike_5d,
    f2_spike_10d,
    f2_spike_20d,

    g1_hit_ma20,
    g1_hit_ma60,
    g1_hit_ma120,
    g1_hit_ma200,

    g2_up_thru_ma20,
    g2_up_thru_ma60,
    g2_up_thru_ma120,
    g2_up_thru_ma200,

    g3_down_thru_ma20,
    g3_down_thru_ma60,
    g3_down_thru_ma120,
    g3_down_thru_ma200,

    h1_long_up_shadow,
    h1_long_down_shadow,
    h1_long_red_bar,
    h1_long_green_bar,
    h1_long_red_range,
    h1_long_green_range,

    h4_up_gap,
    h4_down_gap,

    h5_incr_5d,
    h5_decr_5d,
)

factors = [
    e1_high_vol,
    e1_low_vol,

    e3_vol_incr_5d,
    e3_vol_decr_5d,

    f1_crash_5d,
    f1_crash_10d,
    f1_crash_20d,

    f2_spike_5d,
    f2_spike_10d,
    f2_spike_20d,

    g1_hit_ma20,
    g1_hit_ma60,
    g1_hit_ma120,
    g1_hit_ma200,

    g2_up_thru_ma20,
    g2_up_thru_ma60,
    g2_up_thru_ma120,
    g2_up_thru_ma200,

    g3_down_thru_ma20,
    g3_down_thru_ma60,
    g3_down_thru_ma120,
    g3_down_thru_ma200,

    h1_long_up_shadow,
    h1_long_down_shadow,
    h1_long_red_bar,
    h1_long_green_bar,
    h1_long_red_range,
    h1_long_green_range,

    h4_up_gap,
    h4_down_gap,

    h5_incr_5d,
    h5_decr_5d,
]


def calculate(stock_df: pd.DataFrame) -> dict:
    context = {}
    start_time = datetime.now()

    for factor in factors:
        dates = factor.calculate_hits(stock_df)
        context[factor.KEY] = dates

    print(f'calculate context cost: {(datetime.now() - start_time).total_seconds()}s')
    return context


import guru.plot
