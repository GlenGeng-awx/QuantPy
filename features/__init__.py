from datetime import datetime
import pandas as pd
import plotly.graph_objects as go
from technical.volume import VOLUME_REG

from features import (
    #
    # static features
    #

    # up/down thru ma 5/20/60/120
    g_01, g_02,             # up thru ma5   / down thru ma5
    g_03, g_04,             # up thru ma20  / down thru ma20
    g_05, g_06,             # up thru ma60  / down thru ma60
    g_07, g_08,             # up thru ma120 / down thru ma120

    # up/down touch ma 5/20/60/120
    g_11, g_12,             # down touch ma5   / up touch ma5
    g_13, g_14,             # down touch ma20  / up touch ma20
    g_15, g_16,             # down touch ma60  / up touch ma60
    g_17, g_18,             # down touch ma120 / up touch ma120

    # up/down thru ema 5/10/12/20/26
    g_31, g_32,             # up thru ema5   / down thru ema5
    g_33, g_34,             # up thru ema10  / down thru ema10
    g_35, g_36,             # up thru ema12  / down thru ema12
    g_37, g_38,             # up thru ema20  / down thru ema20
    g_39, g_40,             # up thru ema26  / down thru ema26

    # up/down touch ema 5/10/12/20/26
    g_41, g_42,             # down touch ema5   / up touch ema5
    g_43, g_44,             # down touch ema10  / up touch ema10
    g_45, g_46,             # down touch ema12  / up touch ema12
    g_47, g_48,             # down touch ema20  / up touch ema20
    g_49, g_50,             # down touch ema26  / up touch ema26

    # yesterday is local min/max
    h_01, h_02,             # yesterday is local min / yesterday is local max

    # yesterday is min/max of last 5d/10d/20d/60d/120d
    h_11, h_12,             # yesterday min of last 5d   / yesterday max of last 5d
    h_13, h_14,             # yesterday min of last 10d  / yesterday max of last 10d
    h_15, h_16,             # yesterday min of last 20d  / yesterday max of last 20d
    h_17, h_18,             # yesterday min of last 60d  / yesterday max of last 60d
    h_19, h_20,             # yesterday min of last 120d / yesterday max of last 120d

    # vol
    i_06, i_07,             # vol min of last 5d    / vol max of last 5d
    i_08, i_09,             # vol min of last 10d   / vol max of last 10d

    # statistics
    j_01, j_02,             # trend switch up   / trend switch down
    j_03, j_04,             # bband pst gt 0.85 / bband pst lt 0.15
    j_05, j_06,             # rsi above 70      / rsi below 30
    j_07, j_08,             # macd golden cross / macd death cross

    # up/down to/thru/away sr level min/max
    k_11, k_12,             # up to sr level min   / down away sr level min
    k_13, k_14,             # up thru sr level min / down thru sr level min
    k_15, k_16,             # up away sr level min / down to sr level min

    k_31, k_32,             # up to sr level max   / down away sr level max
    k_33, k_34,             # up thru sr level max / down thru sr level max
    k_35, k_36,             # up away sr level max / down to sr level max

    # vol incr/decr 1d/3d/5d
    l_01, l_02,             # vol incr 1d / vol decr 1d
    l_03, l_04,             # vol incr 3d / vol decr 3d
    l_05, l_06,             # vol incr 5d / vol decr 5d

    # close incr/decr 1d/3d/5d
    l_11, l_12,             # close incr 1d / close decr 1d
    l_13, l_14,             # close incr 3d / close decr 3d
    l_15, l_16,             # close incr 5d / close decr 5d

    # low incr/decr 1d/3d/5d
    l_21, l_22,             # low incr 1d / low decr 1d
    l_23, l_24,             # low incr 3d / low decr 3d
    l_25, l_26,             # low incr 5d / low decr 5d

    # high incr/decr 1d/3d/5d
    l_31, l_32,             # high incr 1d / high decr 1d
    l_33, l_34,             # high incr 3d / high decr 2d
    l_35, l_36,             # high incr 5d / high decr 3d

    # baseline incr/decr 1d/3d/5d
    l_41, l_42,             # baseline incr 1d / baseline decr 1d
    l_43, l_44,             # baseline incr 3d / baseline decr 3d
    l_45, l_46,             # baseline incr 5d / baseline decr 5d

    # red/green bar
    m_01, m_02,             # real red bar / real green bar
    m_03, m_04,             # fake red bar / fake green bar

    # up/down engulfing/harami/gap
    m_31, m_32,             # up engulfing / down engulfing
    m_33, m_34,             # up harami    / down harami
    m_35, m_36,             # up gap       / down gap

    # weekday
    w_01, w_02, w_03, w_04, w_05,

    #
    # dynamic features
    #

    # vol
    i_01, i_02,             # extreme high vol      / extreme low vol
    i_03, i_04, i_05,       # high vol / normal vol / low vol

    # incr/decr top 10pst last 1d/3d/5d/10d/15d/20d
    k_41, k_42,             # incr top 10% today    / decr top 10% today
    k_43, k_44,             # incr top 10% last 3d  / decr top 10% last 3d
    k_45, k_46,             # incr top 10% last 5d  / decr top 10% last 5d
    k_47, k_48,             # incr top 10% last 10d / decr top 10% last 10d
    k_49, k_50,             # incr top 10% last 15d / decr top 10% last 15d
    k_51, k_52,             # incr top 10% last 20d / decr top 10% last 20d

    # incr/decr bottom 10pst last 3d/5d/10d/15d/20d
    k_61, k_62,             # incr bottom 10% last 3d  / decr bottom 10% last 3d
    k_63, k_64,             # incr bottom 10% last 5d  / decr bottom 10% last 5d
    k_65, k_66,             # incr bottom 10% last 10d / decr bottom 10% last 10d
    k_67, k_68,             # incr bottom 10% last 15d / decr bottom 10% last 15d
    k_69, k_70,             # incr bottom 10% last 20d / decr bottom 10% last 20d

    # short/long red/green bar
    m_11, m_12,             # long red bar  / long green bar
    m_13, m_14,             # short red bar / short green bar

    # short/long upper/lower shadow
    m_21, m_22,             # long lower shadow  / long upper shadow
    m_23, m_24,             # short lower shadow / short upper shadow
)


STATIC_FEATURES = [
    m_01, m_02, m_03, m_04,
    m_31, m_32, m_33, m_34, m_35, m_36,
    g_01, g_02, g_03, g_04, g_05, g_06, g_07, g_08,
    g_11, g_12, g_13, g_14, g_15, g_16, g_17, g_18,
    g_31, g_32, g_33, g_34, g_35, g_36, g_37, g_38, g_39, g_40,
    g_41, g_42, g_43, g_44, g_45, g_46, g_47, g_48, g_49, g_50,
    i_06, i_07, i_08, i_09,
    h_01, h_02, h_11, h_12, h_13, h_14, h_15, h_16, h_17, h_18, h_19, h_20,
    j_01, j_02, j_03, j_04,j_05, j_06, j_07, j_08,
    k_11, k_12, k_13, k_14, k_15, k_16,
    k_31, k_32, k_33, k_34, k_35, k_36,
    l_01, l_02, l_03, l_04, l_05, l_06,
    l_11, l_12, l_13, l_14, l_15, l_16,
    l_21, l_22, l_23, l_24, l_25, l_26,
    l_31, l_32, l_33, l_34, l_35, l_36,
    l_41, l_42, l_43, l_44, l_45, l_46,
    w_01, w_02, w_03, w_04, w_05,
]


DYNAMIC_FEATURES = [
    m_11, m_12, m_13, m_14, m_21, m_22, m_23, m_24,
    i_01, i_02, i_03, i_04, i_05,
    k_41, k_42, k_43, k_44, k_45, k_46, k_47, k_48, k_49, k_50, k_51, k_52,
    k_61, k_62, k_63, k_64, k_65, k_66, k_67, k_68, k_69, k_70,
]


def calculate_feature(stock_df: pd.DataFrame, stock_name: str, static: bool) -> pd.DataFrame:
    if static:
        feature_buf = STATIC_FEATURES
    else:
        feature_buf = DYNAMIC_FEATURES

        volume = stock_df['volume']
        stock_df[VOLUME_REG] = (volume - volume.mean()) / volume.std()

    start_time = datetime.now()
    for f in feature_buf:
        f.execute(stock_df)
        stock_df = stock_df.copy()

    time_cost = (datetime.now() - start_time).total_seconds()
    print(f'----> {stock_name} calculate_feature(static={static}) finished, cost: {time_cost}s')
    return stock_df


def _build_graph(stock_df: pd.DataFrame, fig: go.Figure,
                 key: str, value: int, color: str, size: float = 2):

    condition = stock_df[key]
    df = stock_df[condition]

    dates = df['Date']
    values = [value] * len(df)

    fig.add_trace(
        go.Scatter(
            name=key, x=dates, y=values,
            mode='markers', marker=dict(color=color, size=size),
        ),
        row=3, col=1,
    )


def plot_feature(stock_df: pd.DataFrame, fig: go.Figure):
    for idx, feature in enumerate(STATIC_FEATURES + DYNAMIC_FEATURES):
        _build_graph(stock_df, fig, feature.KEY, idx * 5, feature.COLOR)
