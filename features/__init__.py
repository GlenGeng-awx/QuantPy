import pandas as pd
import plotly.graph_objects as go

from features import (
    f_001_b, f_001_s,       # above ma20 / below ma20
    f_002_b, f_002_s,       # above ma5 / below ma5
    f_003_b, f_003_s,       # yesterday is local min / yesterday is local max
    f_004_b, f_004_s,       # trend switch up / trend switch down
    f_005_b, f_005_s,       # up with high volume / down with high volume
    f_006_b, f_006_s,       # bband pst gt 0.85 / bband pst lt 0.15
    f_007_b, f_007_s,       # rsi above 70 / rsi below 30
    f_008_b, f_008_s,       # macd golden cross / macd death cross
    f_009_b, f_009_s,       # up thru r level / down thru s level
    f_010_b,                # up thru r level, retrace, bounds back
    f_011_b, f_011_s,       # incr top 10% in last 3d / decr top 10% in last 3d
    f_012_b, f_012_s,       # incr top 10% in last 10d / decr top 10% in last 10d
    f_013_b, f_013_s,       # yesterday is min of last 20d / yesterday is max of last 20d
    f_014_b, f_014_s,       # high volume / low volume
    f_015_b, f_015_s,       # incr top 10% today / decr top 10% today
    f_016_b, f_016_s,       # long lower shadow / long upper shadow
    f_017_b, f_017_s,       # long red bar / long green bar
    f_018_b, f_018_s,       # short red bar / short green bar
    f_019_b, f_019_s,       # vol incr 3d / vol decr 3d
    f_020_b, f_020_s,       # price incr 5d / price decr 5d
    f_021_b, f_021_s,       # incr with short upper shadow / decr with short lower shadow
    f_022_b, f_022_s,       # up to sr level / down away sr level
    f_023_b, f_023_s,       # up away sr level / down to sr level
    f_024_b, f_024_s,       # up thru sr level / down thru sr level
)

FEATURE_BUF = [
    f_001_b, f_001_s,
    f_002_b, f_002_s,
    f_003_b, f_003_s,
    f_004_b, f_004_s,
    f_005_b, f_005_s,
    f_006_b, f_006_s,
    f_007_b, f_007_s,
    f_008_b, f_008_s,
    f_009_b, f_009_s,
    f_010_b,
    f_011_b, f_011_s,
    f_012_b, f_012_s,
    f_013_b, f_013_s,
    f_014_b, f_014_s,
    f_015_b, f_015_s,
    f_016_b, f_016_s,
    f_017_b, f_017_s,
    f_018_b, f_018_s,
    f_019_b, f_019_s,
    f_020_b, f_020_s,
    f_021_b, f_021_s,
    f_022_b, f_022_s,
    f_023_b, f_023_s,
    f_024_b, f_024_s,
]


def calculate_feature(stock_df: pd.DataFrame):
    for f in FEATURE_BUF:
        f.execute(stock_df)


def _build_graph(stock_df: pd.DataFrame, fig: go.Figure,
                 key: str, value: int, color: str, size: float = 3):

    condition = stock_df[key]
    df = stock_df[condition]

    dates = df['Date']
    values = [value] * len(df)

    fig.add_trace(
        go.Scatter(
            name=key, x=dates, y=values,
            mode='markers', marker=dict(color=color, size=size),
        ),
        row=2, col=1,
    )


def plot_feature(stock_df: pd.DataFrame, fig: go.Figure):
    for params in [
        (f_001_b.KEY, f_001_b.VAL, 'red', 2),   (f_001_s.KEY, f_001_s.VAL, 'green', 2),
        (f_002_b.KEY, f_002_b.VAL, 'red', 2),   (f_002_s.KEY, f_002_s.VAL, 'green', 2),
        (f_003_b.KEY, f_003_b.VAL, 'red'),      (f_003_s.KEY, f_003_s.VAL, 'green'),
        (f_004_b.KEY, f_004_b.VAL, 'red'),      (f_004_s.KEY, f_004_s.VAL, 'green'),
        (f_005_b.KEY, f_005_b.VAL, 'red'),      (f_005_s.KEY, f_005_s.VAL, 'green'),
        (f_006_b.KEY, f_006_b.VAL, 'red', 2),   (f_006_s.KEY, f_006_s.VAL, 'green', 2),
        (f_007_b.KEY, f_007_b.VAL, 'red', 2),   (f_007_s.KEY, f_007_s.VAL, 'green', 2),
        (f_008_b.KEY, f_008_b.VAL, 'red'),      (f_008_s.KEY, f_008_s.VAL, 'green'),
        (f_009_b.KEY, f_009_b.VAL, 'red'),      (f_009_s.KEY, f_009_s.VAL, 'green'),
        (f_010_b.KEY, f_010_b.VAL, 'red'),
        (f_011_b.KEY, f_011_b.VAL, 'red'),      (f_011_s.KEY, f_011_s.VAL, 'green'),
        (f_012_b.KEY, f_012_b.VAL, 'red'),      (f_012_s.KEY, f_012_s.VAL, 'green'),
        (f_013_b.KEY, f_013_b.VAL, 'red'),      (f_013_s.KEY, f_013_s.VAL, 'green'),
        (f_014_b.KEY, f_014_b.VAL, 'red', 2),   (f_014_s.KEY, f_014_s.VAL, 'green', 2),
        (f_015_b.KEY, f_015_b.VAL, 'red'),      (f_015_s.KEY, f_015_s.VAL, 'green'),
        (f_016_b.KEY, f_016_b.VAL, 'red'),      (f_016_s.KEY, f_016_s.VAL, 'green'),
        (f_017_b.KEY, f_017_b.VAL, 'red'),      (f_017_s.KEY, f_017_s.VAL, 'green'),
        (f_018_b.KEY, f_018_b.VAL, 'red', 2),   (f_018_s.KEY, f_018_s.VAL, 'green', 2),
        (f_019_b.KEY, f_019_b.VAL, 'red', 2),   (f_019_s.KEY, f_019_s.VAL, 'green', 2),
        (f_020_b.KEY, f_020_b.VAL, 'red', 2),   (f_020_s.KEY, f_020_s.VAL, 'green', 2),
        (f_021_b.KEY, f_021_b.VAL, 'red', 2),   (f_021_s.KEY, f_021_s.VAL, 'green', 2),
        (f_022_b.KEY, f_022_b.VAL, 'red', 2),   (f_022_s.KEY, f_022_s.VAL, 'green', 2),
        (f_023_b.KEY, f_023_b.VAL, 'red', 2),   (f_023_s.KEY, f_023_s.VAL, 'green', 2),
        (f_024_b.KEY, f_024_b.VAL, 'red'),      (f_024_s.KEY, f_024_s.VAL, 'green'),
    ]:
        _build_graph(stock_df, fig, *params)
