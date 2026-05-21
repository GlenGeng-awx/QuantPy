"""
Usage:
    python3 -m fundamental.health | pbcopy   # 全量评分
    python3 -m fundamental.health ADBE       # 单只评分

评分规则: Q > TTM > 3yr，权重 0.5 / 0.3 / 0.2
    pass=1.0, warn=0.5, fail=0.0, skip=权重分给其余层
    指标得分 = 加权和 × 该指标分值
    Overall = BS × 0.40 + CashFlow × 0.35 + Income × 0.25

INCOME STATEMENT (100 pts, weight 25%)
───────────────────────────────────────────────────────
Metric                  3yr    TTM    Q     Pts

Revenue Growth          ✓      ✓      ✓     15
  3yr: 年报 3年为正且逐年递增
  TTM: TTM vs 去年年报 正增长
  Q:   最近4季全部为正 + 最新季 YoY 正增长

Op Income Growth        ✓      ✓      ✓     15
  3yr: 年报 3年为正且逐年递增
  TTM: TTM vs 去年年报 正增长
  Q:   最近4季全部为正 + 最新季 YoY 正增长

EBITDA Growth           ✓      ✓      ✓     15
  3yr: 年报 3年为正且逐年递增
  TTM: TTM vs 去年年报 正增长
  Q:   最近4季全部为正 + 最新季 YoY 正增长

EPS Trend               ✓      ✓      ✓     30
  3yr: 年报 3年为正且逐年递增
  TTM: TTM vs 去年年报 正增长
  Q:   最近4季全部为正 + 最新季 YoY 正增长

Margins                 -      ✓      -     15
  TTM: GM > 50% 或 NM > 15% pass; GM > 30% 或 NM > 10% warn

Interest Coverage       -      ✓      -     10
  TTM: OpIncome / Interest Expense > 5x pass, 2-5x warn
  无债务直接 pass
                                            ───
                                            100

CASH FLOW (100 pts, weight 35%)
───────────────────────────────────────────────────────
Metric                  3yr    TTM    Q     Pts

OCF Trend               ✓      ✓      ✓     30
  3yr: 年报 3年为正且逐年递增
  TTM: TTM vs 去年年报 正增长
  Q:   最近4季全部为正 + 最新季 YoY 正增长

Earnings Quality        -      ✓      -     15
  TTM: OCF / NI > 0.8 pass, 0.5-0.8 warn

Free Cash Flow          ✓      ✓      ✓     25
  3yr: 年报 3年为正
  TTM: TTM > 0
  Q:   最近4季全部为正 + 最新季 YoY 正增长

Shareholder Return      ✓      ✓      -     15
  3yr: 连续3年每年有 Buyback 或 Dividend
       3年=pass, 1-2年=warn, 0=fail
  TTM: (|Buyback| + |Dividend| - SBC) > 0

SBC Ratio               -      ✓      -     15
  TTM: SBC / Revenue < 10% pass, 10-15% warn
                                            ───
                                            100

BALANCE SHEET (100 pts, weight 40%)
───────────────────────────────────────────────────────
Metric                  3yr    TTM    Q     Pts

Cash Adequacy           -      -      ✓     30
  Q: (Cash + STI) / Total Debt > 0.5 pass, 0.3-0.5 warn
  无债务直接 pass

Debt/Equity             -      -      ✓     30
  Q: Total Debt / Equity < 1.0 pass, 1.0-2.0 warn
  无债务直接 pass，负权益直接 fail

Current Ratio           -      -      ✓     20
  Q: CA / CL > 1.0 pass, 0.8-1.0 warn
  剔除 Deferred Revenue 后 > 1.0 亦 pass（SaaS）

AR Growth               -      -      ✓     10
  Q: AR YoY 增速 ≤ Revenue YoY 增速 × 1.5 pass

AP Stability            -      -      ✓     10
  Q: AP YoY 变动 < 50% pass

Risk Flags                                  -15（额外扣分）
  · Goodwill + Intangibles / Total Assets > 30% 且 NI 连续下降 → -10
  · Operating Leases / Total Assets > 20% → -5
                                            ───
                                            100
"""
