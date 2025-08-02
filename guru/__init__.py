from datetime import datetime
import pandas as pd

from guru import (
    e1_high_vol,
    e1_low_vol,

    e2_extreme_high_vol,
    e2_extreme_low_vol,

    e3_vol_incr_3d,
    e3_vol_incr_5d,
    e3_vol_decr_3d,
    e3_vol_decr_5d,

    e4_vol_box_3d,
    e4_vol_box_5d,
    e4_vol_box_10d,
    e4_vol_box_15d,

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

    f3_box_3d,
    f3_box_5d,
    f3_box_10d,
    f3_box_15d,

    g1_hit_ma5,
    g1_hit_ma10,
    g1_hit_ma20,
    g1_hit_ma60,
    g1_hit_ma120,

    g2_up_thru_ma10,
    g2_up_thru_ma20,
    g2_up_thru_ma60,
    g2_up_thru_ma120,

    g3_down_thru_ma10,
    g3_down_thru_ma20,
    g3_down_thru_ma60,
    g3_down_thru_ma120,

    h1_long_up_shadow,
    h1_long_down_shadow,
    h1_long_red_bar,
    h1_long_green_bar,

    h2_short_up_shadow,
    h2_short_down_shadow,
    h2_short_red_bar,
    h2_short_green_bar,

    h3_mon,
    h3_tue,
    h3_wed,
    h3_thu,
    h3_fri,

    h4_up_gap,
    h4_up_gap_huge,
    h4_down_gap,
    h4_down_gap_huge,

    h5_incr_3d,
    h5_incr_5d,
    h5_decr_3d,
    h5_decr_5d,

    h6_fake_green_bar,
    h6_fake_red_bar,

    n0_will_crash,
    n0_will_spike,

    n1_will_shoot_down,
    n1_will_shoot_up,
)

factors = [
    e1_high_vol,
    e1_low_vol,

    e2_extreme_high_vol,
    e2_extreme_low_vol,

    e3_vol_incr_3d,
    e3_vol_incr_5d,
    e3_vol_decr_3d,
    e3_vol_decr_5d,

    e4_vol_box_3d,
    e4_vol_box_5d,
    e4_vol_box_10d,
    e4_vol_box_15d,

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

    f3_box_3d,
    f3_box_5d,
    f3_box_10d,
    f3_box_15d,

    g1_hit_ma5,
    g1_hit_ma10,
    g1_hit_ma20,
    g1_hit_ma60,
    g1_hit_ma120,

    g2_up_thru_ma10,
    g2_up_thru_ma20,
    g2_up_thru_ma60,
    g2_up_thru_ma120,

    g3_down_thru_ma10,
    g3_down_thru_ma20,
    g3_down_thru_ma60,
    g3_down_thru_ma120,

    h1_long_up_shadow,
    h1_long_down_shadow,
    h1_long_red_bar,
    h1_long_green_bar,

    h2_short_up_shadow,
    h2_short_down_shadow,
    h2_short_red_bar,
    h2_short_green_bar,

    h3_mon,
    h3_tue,
    h3_wed,
    h3_thu,
    h3_fri,

    h4_up_gap,
    h4_up_gap_huge,
    h4_down_gap,
    h4_down_gap_huge,

    h5_incr_3d,
    h5_incr_5d,
    h5_decr_3d,
    h5_decr_5d,

    h6_fake_green_bar,
    h6_fake_red_bar,
]

targets = [
    n0_will_crash,
    n1_will_shoot_down,

    n0_will_spike,
    n1_will_shoot_up,
]


def calculate(stock_df: pd.DataFrame) -> dict:
    context = {}

    start_time = datetime.now()
    for factor in factors + targets:
        dates = factor.calculate_hits(stock_df)
        context[factor.KEY] = dates
    print(f'calculate context cost: {(datetime.now() - start_time).total_seconds()}s')

    return context


import guru.plot
import guru.train
import guru.predict
