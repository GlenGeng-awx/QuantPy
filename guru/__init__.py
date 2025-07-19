import pandas as pd

from guru import (
    f0_high_vol,
    f0_low_vol,
    f0_extreme_high_vol,
    f0_extreme_low_vol,

    f1_crash_1d,
    f1_crash_3d,
    f1_crash_5d,
    f1_crash_10d,
    f1_crash_15d,

    f2_spike_1d,
    f2_spike_3d,
    f2_spike_5d,
    f2_spike_10d,
    f2_spike_15d,

    f3_long_up_shadow,
    f3_long_down_shadow,
    f3_long_red_bar,
    f3_long_green_bar,

    f4_short_up_shaodow,
    f4_short_down_shadow,
    f4_short_red_bar,
    f4_short_green_bar,

    f5_incr_3d,
    f5_decr_3d,
    f5_up_gap,
    f5_down_gap,
    f5_fake_green_bar,
    f5_fake_red_bar,

    f8_hit_ma5,
    f8_hit_ma10,
    f8_hit_ma20,
    f8_hit_ma60,
    f8_hit_ma120,

    g0_will_crash,
    g0_will_spike,
    g1_will_shoot_down,
    g1_will_shoot_up,
)

factors = [
    f0_high_vol,
    f0_low_vol,
    f0_extreme_high_vol,
    f0_extreme_low_vol,

    f1_crash_1d,
    f1_crash_3d,
    f1_crash_5d,
    f1_crash_10d,
    f1_crash_15d,

    f2_spike_1d,
    f2_spike_3d,
    f2_spike_5d,
    f2_spike_10d,
    f2_spike_15d,

    f3_long_up_shadow,
    f3_long_down_shadow,
    f3_long_red_bar,
    f3_long_green_bar,

    f4_short_up_shaodow,
    f4_short_down_shadow,
    f4_short_red_bar,
    f4_short_green_bar,

    f5_incr_3d,
    f5_decr_3d,
    f5_up_gap,
    f5_down_gap,
    f5_fake_green_bar,
    f5_fake_red_bar,

    f8_hit_ma5,
    f8_hit_ma10,
    f8_hit_ma20,
    f8_hit_ma60,
    f8_hit_ma120,
]

targets = [
    g0_will_crash,
    g1_will_shoot_down,

    g0_will_spike,
    g1_will_shoot_up,
]

def calculate(stock_df: pd.DataFrame) -> dict:
    context = {}

    for factor in factors + targets:
        dates = factor.calculate_hits(stock_df)
        context[factor.KEY] = dates

    return context


import guru.plot
import guru.train
import guru.predict
