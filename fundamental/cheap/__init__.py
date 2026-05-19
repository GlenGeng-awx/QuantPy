"""
Usage:
    python3 -m fundamental.cheap AAPL       # single stock
    python3 -m fundamental.cheap            # all stocks + ranking

寻找格雷厄姆的"被忽视的大公司"，按满足条件数排序。

Signals (排序依据):
    1Y Drawdown   > 40%     过去一周低点 vs 一年高点
    2Y Drawdown   > 60%     过去一周低点 vs 两年高点
    Near 52W Low  ≤ 15%     当前价距 52 周低点
    P/E TTM       < 15x
    EV/EBITDA     < 10x
    P/S           < 2.0x

Hints (过去 5 天技术信号):
    Elliott Hit             触及 Elliott 波浪关键点位
    Neck Line Hit           触及颈线支撑/阻力
    Trend Line Hit          触及趋势线
    MinMax 4th Hit          触及四阶局部极值
"""
