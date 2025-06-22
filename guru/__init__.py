from guru import (
    f0_high_vol,
    f0_low_vol,
    f1_incr_3pst,
    f1_decr_3pst,
    f2_incr_3d,
    f2_decr_3d,
    f3_long_up_shadow,
    f3_long_down_shadow,
    f4_long_red_bar,
    f4_long_green_bar,
    f5_short_up_shaodow,
    f5_short_down_shadow,
    f6_short_red_bar,
    f6_short_green_bar,
    f7_up_gap,
    f7_down_gap,
    f8_hit_ma20,
    f8_hit_ma60,
    f8_hit_ma120,
)

factors = [
    f0_high_vol,
    f0_low_vol,
    f1_incr_3pst,
    f1_decr_3pst,
    f2_incr_3d,
    f2_decr_3d,
    f3_long_up_shadow,
    f3_long_down_shadow,
    f4_long_red_bar,
    f4_long_green_bar,
    f5_short_up_shaodow,
    f5_short_down_shadow,
    f6_short_red_bar,
    f6_short_green_bar,
    f7_up_gap,
    f7_down_gap,
    f8_hit_ma20,
    f8_hit_ma60,
    f8_hit_ma120,
]

import guru.plot
import guru.train
import guru.predict
