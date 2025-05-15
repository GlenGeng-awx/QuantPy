import pandas as pd

from base_engine import BaseEngine
from guru.hit_line import HitLine
from guru.hit_line_expo import HitLineExpo
from guru.hit_neck_line import HitNeckLine
from guru.hit_sr import HitSR
from guru.hit_volume import HitVolume

OFFSET = 0


def hit_line_cond(stock_df: pd.DataFrame, hit_line: HitLine) -> list:
    dates = [date for date, _ in hit_line.line_hits]
    count = 0
    for i in range(-4, 1):
        if stock_df['Date'].iloc[i - OFFSET] in dates:
            count += 1

    if count >= 2:
        return [('enable_line', True,), ('enable_hit_line', True)]
    else:
        return []


def hit_line_expo_cond(stock_df: pd.DataFrame, hit_line_expo: HitLineExpo) -> list:
    dates = [date for date, _ in hit_line_expo.lines_expo_hits]
    count = 0
    for i in range(-4, 1):
        if stock_df['Date'].iloc[i - OFFSET] in dates:
            count += 1

    if count >= 2:
        return [('enable_line_expo', True,), ('enable_hit_line_expo', True)]
    else:
        return []


def hit_neck_line_cond(stock_df: pd.DataFrame, hit_neck_line: HitNeckLine) -> list:
    dates = [date for date, _ in hit_neck_line.neck_line_hits]
    count = 0
    for i in range(-4, 1):
        if stock_df['Date'].iloc[i - OFFSET] in dates:
            count += 1

    if count >= 2:
        return [('enable_neck_line', True,), ('enable_hit_neck_line', True)]
    else:
        return []


def hit_sr_cond(stock_df: pd.DataFrame, hit_sr: HitSR) -> list:
    dates = [date for date, _ in hit_sr.hits]
    count = 0
    for i in range(-4, 1):
        if stock_df['Date'].iloc[i - OFFSET] in dates:
            count += 1

    if count >= 2:
        return [('enable_sr', True,), ('enable_hit_sr', True)]
    else:
        return []


def hit_high_vol(stock_df: pd.DataFrame, hit_volume: HitVolume) -> list:
    dates = [date for date, _ in hit_volume.high_hits]
    count = 0
    for i in range(-4, 1):
        if stock_df['Date'].iloc[i - OFFSET] in dates:
            count += 1

    if count >= 2:
        return [('enable_hit_high_vol', (True, 2))]
    else:
        return []


def hit_low_vol(stock_df: pd.DataFrame, hit_volume: HitVolume) -> list:
    dates = [date for date, _ in hit_volume.low_hits]
    count = 0
    for i in range(-4, 1):
        if stock_df['Date'].iloc[i - OFFSET] in dates:
            count += 1

    if count >= 2:
        return [('enable_hit_low_vol', (True, 2))]
    else:
        return []


def pick(base_engine: BaseEngine) -> tuple:
    stock_df = base_engine.stock_df

    var_p = []
    var_p.extend(hit_line_cond(stock_df, base_engine.hit_line))
    var_p.extend(hit_line_expo_cond(stock_df, base_engine.hit_line_expo))
    var_p.extend(hit_neck_line_cond(stock_df, base_engine.hit_neck_line))
    var_p.extend(hit_sr_cond(stock_df, base_engine.hit_sr))

    var_v = []
    var_v.extend(hit_high_vol(stock_df, base_engine.hit_volume))
    var_v.extend(hit_low_vol(stock_df, base_engine.hit_volume))

    return var_p, var_v
