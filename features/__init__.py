import pandas as pd
import plotly.graph_objects as go

from features import (
    # up/down thru ma 60/20/5
    f_029_b, f_029_s,       # up thru ma60 / down thru ma60
    f_001_b, f_001_s,       # up thru ma20 / down thru ma20
    f_002_b, f_002_s,       # up thru ma5  / down thru ma5

    # up/down touch ma 60/20/5
    f_030_b, f_030_s,       # down touch ma60 / up touch ma60
    f_025_b, f_025_s,       # down touch ma20 / up touch ma20
    f_026_b, f_026_s,       # down touch ma5  / up touch ma5

    # yesterday is local min/max
    f_003_b, f_003_s,       # yesterday is local min / yesterday is local max

    # yesterday is min/max of last 5d/10d/20d/60d/120d
    f_031_b, f_031_s,       # yesterday is min of last   5d / yesterday is max of last   5d
    f_032_b, f_032_s,       # yesterday is min of last  10d / yesterday is max of last  10d
    f_013_b, f_013_s,       # yesterday is min of last  20d / yesterday is max of last  20d
    f_044_b, f_044_s,       # yesterday is min of last  60d / yesterday is max of last  60d
    f_045_b, f_045_s,       # yesterday is min of last 120d / yesterday is max of last 120d

    # vol
    f_005_b, f_005_s,           # extreme high vol / extreme low vol
    f_014_0, f_014_1, f_014_2,  # high vol / normal vol / low vol
    f_060_b, f_060_s,           # vol is min of last  5d / vol is max of last  5d
    f_061_b, f_061_s,           # vol is min of last 10d / vol is max of last 10d

    # red/green bar
    f_038_b, f_038_s,       # real red bar / real green bar
    f_039_b, f_039_s,       # fake red bar / fake green bar

    # statistics
    f_004_b, f_004_s,       # trend switch up / trend switch down
    f_006_b, f_006_s,       # bband pst gt 0.85 / bband pst lt 0.15
    f_007_b, f_007_s,       # rsi above 70 / rsi below 30
    f_008_b, f_008_s,       # macd golden cross / macd death cross

    # s level / r level
    f_009_b, f_009_s,       # up thru r level / down thru s level
    f_010_b,                # up thru r level, retrace, bounds back

    # up/down to/thru/away sr level
    f_022_b, f_022_s,       # up to   sr level / down away sr level
    f_024_b, f_024_s,       # up thru sr level / down thru sr level
    f_023_b, f_023_s,       # up away sr level / down to   sr level

    # incr/decr top 10pst last 1d/3d/5d/10d
    f_015_b, f_015_s,       # incr top 10% today    / decr top 10% today
    f_011_b, f_011_s,       # incr top 10% last 3d  / decr top 10% last 3d
    f_033_b, f_033_s,       # incr top 10% last 5d  / decr top 10% last 5d
    f_012_b, f_012_s,       # incr top 10% last 10d / decr top 10% last 10d

    # vol incr/decr 1d/3d/5d
    f_046_b, f_046_s,       # vol incr 1d / vol decr 1d
    f_019_b, f_019_s,       # vol incr 3d / vol decr 3d
    f_034_b, f_034_s,       # vol incr 5d / vol decr 5d

    # close incr/decr 1d/3d/5d
    f_041_b, f_041_s,       # close incr 1d / close decr 1d
    f_020_b, f_020_s,       # close incr 3d / close decr 3d
    f_036_b, f_036_s,       # close incr 5d / close decr 5d

    # low incr/decr 1d/3d/5d
    f_042_b, f_042_s,       # low incr 1d / low decr 1d
    f_050_b, f_050_s,       # low incr 3d / low decr 3d
    f_052_b, f_052_s,       # low incr 5d / low decr 5d

    # high incr/decr 1d/3d/5d
    f_043_b, f_043_s,       # high incr 1d / high decr 1d
    f_054_b, f_054_s,       # high incr 3d / high decr 2d
    f_056_b, f_056_s,       # high incr 5d / high decr 3d

    # baseline incr/decr 1d/3d/5d
    f_057_b, f_057_s,       # baseline incr 1d / baseline decr 1d
    f_058_b, f_058_s,       # baseline incr 3d / baseline decr 3d
    f_059_b, f_059_s,       # baseline incr 5d / baseline decr 5d

    # short/long red/green bar
    f_017_b, f_017_s,       # long red bar / long green bar
    f_018_b, f_018_s,       # short red bar / short green bar

    # short/long upper/lower shadow
    f_016_b, f_016_s,       # long lower shadow / long upper shadow
    f_021_b, f_021_s,       # short lower shadow / short upper shadow

    # up/down engulfing/harami
    f_027_b, f_027_s,       # up engulfing / down engulfing
    f_028_b, f_028_s,       # up harami / down harami

    # weekday
    f_040_0, f_040_1, f_040_2, f_040_3, f_040_4,
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
    f_014_0, f_014_1, f_014_2,
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
    f_025_b, f_025_s,
    f_026_b, f_026_s,
    f_027_b, f_027_s,
    f_028_b, f_028_s,
    f_029_b, f_029_s,
    f_030_b, f_030_s,
    f_031_b, f_031_s,
    f_032_b, f_032_s,
    f_033_b, f_033_s,
    f_034_b, f_034_s,
    f_036_b, f_036_s,
    f_038_b, f_038_s,
    f_039_b, f_039_s,
    f_040_0, f_040_1, f_040_2, f_040_3, f_040_4,
    f_041_b, f_041_s,
    f_042_b, f_042_s,
    f_043_b, f_043_s,
    f_044_b, f_044_s,
    f_045_b, f_045_s,
    f_046_b, f_046_s,
    f_050_b, f_050_s,
    f_052_b, f_052_s,
    f_054_b, f_054_s,
    f_056_b, f_056_s,
    f_057_b, f_057_s,
    f_058_b, f_058_s,
    f_059_b, f_059_s,
    f_060_b, f_060_s,
    f_061_b, f_061_s,
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
        (f_001_b.KEY, f_001_b.VAL, 'red'),   (f_001_s.KEY, f_001_s.VAL, 'green'),
        (f_002_b.KEY, f_002_b.VAL, 'red'),   (f_002_s.KEY, f_002_s.VAL, 'green'),
        (f_003_b.KEY, f_003_b.VAL, 'red', 2),   (f_003_s.KEY, f_003_s.VAL, 'green', 2),
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
        (f_014_0.KEY, f_014_0.VAL, 'red', 2),   (f_014_1.KEY, f_014_1.VAL, 'green', 2),   (f_014_2.KEY, f_014_2.VAL, 'green', 2),
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
        (f_025_b.KEY, f_025_b.VAL, 'red', 2),   (f_025_s.KEY, f_025_s.VAL, 'green', 2),
        (f_026_b.KEY, f_026_b.VAL, 'red', 2),   (f_026_s.KEY, f_026_s.VAL, 'green', 2),
        (f_027_b.KEY, f_027_b.VAL, 'red'),      (f_027_s.KEY, f_027_s.VAL, 'green'),
        (f_028_b.KEY, f_028_b.VAL, 'red'),      (f_028_s.KEY, f_028_s.VAL, 'green'),
        (f_029_b.KEY, f_029_b.VAL, 'red'),      (f_029_s.KEY, f_029_s.VAL, 'green'),
        (f_030_b.KEY, f_030_b.VAL, 'red'),      (f_030_s.KEY, f_030_s.VAL, 'green'),
        (f_031_b.KEY, f_031_b.VAL, 'red'),      (f_031_s.KEY, f_031_s.VAL, 'green'),
        (f_032_b.KEY, f_032_b.VAL, 'red'),      (f_032_s.KEY, f_032_s.VAL, 'green'),
        (f_033_b.KEY, f_033_b.VAL, 'red'),      (f_033_s.KEY, f_033_s.VAL, 'green'),
        (f_034_b.KEY, f_034_b.VAL, 'red'),      (f_034_s.KEY, f_034_s.VAL, 'green'),
        (f_036_b.KEY, f_036_b.VAL, 'red'),      (f_036_s.KEY, f_036_s.VAL, 'green'),
        (f_038_b.KEY, f_038_b.VAL, 'red', 2),   (f_038_s.KEY, f_038_s.VAL, 'green', 2),
        (f_039_b.KEY, f_039_b.VAL, 'red', 2),   (f_039_s.KEY, f_039_s.VAL, 'green', 2),
        (f_040_0.KEY, f_040_0.VAL, 'red', 2),
        (f_040_1.KEY, f_040_1.VAL, 'red', 2),
        (f_040_2.KEY, f_040_2.VAL, 'red', 2),
        (f_040_3.KEY, f_040_3.VAL, 'red', 2),
        (f_040_4.KEY, f_040_4.VAL, 'red', 2),
        (f_041_b.KEY, f_041_b.VAL, 'red', 2),   (f_041_s.KEY, f_041_s.VAL, 'green', 2),
        (f_042_b.KEY, f_042_b.VAL, 'red', 2),   (f_042_s.KEY, f_042_s.VAL, 'green', 2),
        (f_043_b.KEY, f_043_b.VAL, 'red', 2),   (f_043_s.KEY, f_043_s.VAL, 'green', 2),
        (f_044_b.KEY, f_044_b.VAL, 'red'),      (f_044_s.KEY, f_044_s.VAL, 'green'),
        (f_045_b.KEY, f_045_b.VAL, 'red'),      (f_045_s.KEY, f_045_s.VAL, 'green'),
        (f_046_b.KEY, f_046_b.VAL, 'red', 2),   (f_046_s.KEY, f_046_s.VAL, 'green', 2),
        (f_050_b.KEY, f_050_b.VAL, 'red', 2),   (f_050_s.KEY, f_050_s.VAL, 'green', 2),
        (f_052_b.KEY, f_052_b.VAL, 'red', 2),   (f_052_s.KEY, f_052_s.VAL, 'green', 2),
        (f_054_b.KEY, f_054_b.VAL, 'red', 2),   (f_054_s.KEY, f_054_s.VAL, 'green', 2),
        (f_056_b.KEY, f_056_b.VAL, 'red', 2),   (f_056_s.KEY, f_056_s.VAL, 'green', 2),
        (f_057_b.KEY, f_057_b.VAL, 'red', 2),   (f_057_s.KEY, f_057_s.VAL, 'green', 2),
        (f_058_b.KEY, f_058_b.VAL, 'red', 2),   (f_058_s.KEY, f_058_s.VAL, 'green', 2),
        (f_059_b.KEY, f_059_b.VAL, 'red', 2),   (f_059_s.KEY, f_059_s.VAL, 'green', 2),
        (f_060_b.KEY, f_060_b.VAL, 'red', 2),   (f_060_s.KEY, f_060_s.VAL, 'green', 2),
        (f_061_b.KEY, f_061_b.VAL, 'red', 2),   (f_061_s.KEY, f_061_s.VAL, 'green', 2),
    ]:
        _build_graph(stock_df, fig, *params)


if __name__ == '__main__':
    for i in range(len(FEATURE_BUF)):
        print(f'{i:<10}\t{FEATURE_BUF[i].KEY:40}\t{FEATURE_BUF[i].RECALL_DAYS}d')

    abbrs = [
        [10, 29],
    ]

    for abbr in abbrs:
        print(abbr, ' / '.join([FEATURE_BUF[i].KEY for i in abbr]))
