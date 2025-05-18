from base_engine import BaseEngine
from guru.hit_elliott import HitElliott
from guru.hit_line import HitLine
from guru.hit_line_expo import HitLineExpo
from guru.hit_neck_line import HitNeckLine
from guru.hit_sr import HitSR
from guru.hit_ma import HitMA
from guru.hit_volume import HitVolume


def hit_elliott_cond(hit_elliott: HitElliott, selected_dates) -> list:
    count = 0
    for date, _ in hit_elliott.hits:
        if date in selected_dates:
            count += 1
    if count >= 2:
        return [('enable_elliott', True), ('enable_hit_elliott', True)]
    else:
        return []


def hit_line_cond(hit_line: HitLine, selected_dates) -> list:
    count = 0
    for date, _ in hit_line.line_hits:
        if date in selected_dates:
            count += 1
    if count >= 1:
        return [('enable_line', True,), ('enable_hit_line', True)]
    else:
        return []


def hit_line_expo_cond(hit_line_expo: HitLineExpo, selected_dates) -> list:
    count = 0
    for date, _ in hit_line_expo.lines_expo_hits:
        if date in selected_dates:
            count += 1
    if count >= 1:
        return [('enable_line_expo', True,), ('enable_hit_line_expo', True)]
    else:
        return []


def hit_neck_line_cond(hit_neck_line: HitNeckLine, selected_dates) -> list:
    count = 0
    for date, _ in hit_neck_line.neck_line_hits:
        if date in selected_dates:
            count += 1
    if count >= 2:
        return [('enable_neck_line', True,), ('enable_hit_neck_line', True)]
    else:
        return []


def hit_sr_cond(hit_sr: HitSR, selected_dates) -> list:
    count = 0
    for date, _ in hit_sr.hits:
        if date in selected_dates:
            count += 1
    if count >= 2:
        return [('enable_sr', True,), ('enable_hit_sr', True)]
    else:
        return []


def hit_ma(hit_ma_: HitMA, selected_dates) -> list:
    var = []

    # hit ma20
    count = 0
    for date, _ in hit_ma_.ma_20.ma_hits:
        if date in selected_dates:
            count += 1
    if count >= 1:
        var.extend([('enable_ma20', True,), ('enable_hit_ma20', True)])

    # hit ma60
    count = 0
    for date, _ in hit_ma_.ma_60.ma_hits:
        if date in selected_dates:
            count += 1
    if count >= 1:
        var.extend([('enable_ma60', True,), ('enable_hit_ma60', True)])

    # hit ma120
    count = 0
    for date, _ in hit_ma_.ma_120.ma_hits:
        if date in selected_dates:
            count += 1
    if count >= 1:
        var.extend([('enable_ma120', True,), ('enable_hit_ma120', True)])

    return var


def hit_high_vol(hit_volume: HitVolume, selected_dates) -> list:
    count = 0
    for date, _ in hit_volume.high_hits:
        if date in selected_dates:
            count += 1
    if count >= 2:
        return [('enable_hit_high_vol', (True, 2))]
    else:
        return []


def hit_low_vol(hit_volume: HitVolume, selected_dates) -> list:
    count = 0
    for date, _ in hit_volume.low_hits:
        if date in selected_dates:
            count += 1
    if count >= 2:
        return [('enable_hit_low_vol', (True, 2))]
    else:
        return []


def pick(base_engine: BaseEngine, selected_dates: list) -> tuple:
    var_p = []
    var_p.extend(hit_elliott_cond(base_engine.hit_elliott, selected_dates))
    # var_p.extend(hit_line_cond(base_engine.hit_line, selected_dates))
    var_p.extend(hit_line_expo_cond(base_engine.hit_line_expo, selected_dates))
    var_p.extend(hit_neck_line_cond(base_engine.hit_neck_line, selected_dates))
    var_p.extend(hit_sr_cond(base_engine.hit_sr, selected_dates))
    var_p.extend(hit_ma(base_engine.hit_ma, selected_dates))

    var_v = []
    var_v.extend(hit_high_vol(base_engine.hit_volume, selected_dates))
    var_v.extend(hit_low_vol(base_engine.hit_volume, selected_dates))

    return var_p, var_v
