"""
9 宫格财务健康评分 (Time-Dimension First)
=========================================

输出 9 个独立分数（3 报表 × 3 时间维度），不做总分。
用于识别"过去好 + 最近差 + 财务强"的困境反转模式。

第一层：三大报表
    Income Statement / Cash Flow / Balance Sheet

第二层：三个时间维度（每个维度满分 100）
    3yr  — 年报趋势（最近 3 年）
    TTM  — TTM vs 去年年报（BS 为最新季 vs 一年前同季 YoY）
    5Q   — 最近 5 季度（4Q 正/趋势 + 最新 Q YoY）

评分规则：
    pass=满分, warn=半分, fail=0, skip=权重分给其余指标

===================================================================
INCOME STATEMENT
===================================================================

--- 3yr (100 pts) ---
  Revenue Trend          20    3年正且递增=pass; 正但不递增=warn; 有负=fail
  Op Income Trend        20    同上
  EBITDA Trend           15    同上
  EPS Trend              25    同上
  GM Trend               20    不下降=pass; 累计降≤5pct=warn; 明显恶化=fail

--- TTM (100 pts) ---
  Revenue vs LY          20    正增长=pass; 0~-3%=warn; 更差=fail
  Op Income vs LY        20    同上
  EBITDA vs LY           15    同上
  EPS vs LY              25    同上
  Margins                10    GM>50% or NM>15%=pass; GM>30% or NM>10%=warn
  Interest Coverage      10    >5x=pass; 2-5x=warn; 无债务=pass

--- 5Q (100 pts) ---
  Q YoY Revenue          10    正增长=pass; 0~-3%=warn; 更差=fail
  Q YoY Op Income        10    同上
  Q YoY EBITDA           10    同上
  Q YoY EPS              15    同上
  4Q Revenue +           10    全正=pass; 1季负=warn; 多季负=fail
  4Q Op Income +         15    同上
  4Q GM Trend            15    环比不下降=pass; 轻微下降=warn; 明显恶化=fail
  4Q NM Trend            15    同上

===================================================================
CASH FLOW
===================================================================

--- 3yr (100 pts) ---
  OCF Trend              25    正且递增=pass; 正但不递增=warn; 有负=fail
  FCF Trend              20    同上
  OCF/NI 3yr             15    均值>0.8=pass; 0.5-0.8=warn
  Buyback/Div 3yr        20    3年都有=pass; 1-2年=warn; 0=fail
  SBC/Rev Trend          20    递减或稳定=pass; 轻微上升=warn; 明显恶化=fail

--- TTM (100 pts) ---
  OCF vs LY              25    正增长=pass; 0~-5%=warn; 更差=fail
  FCF > 0                25    正=pass; 否则=fail
  OCF/NI                 15    >0.8=pass; 0.5-0.8=warn
  Net Return             20    |BB|+|Div|-SBC>0=pass; BB+Div>0 but net<0=warn
  SBC/Revenue            15    <10%=pass; 10-15%=warn; >15%=fail

--- 5Q (100 pts) ---
  4Q OCF +               25    全正=pass; 1季负=warn; 多季负=fail
  Q YoY OCF              20    正增长=pass; 否则=fail
  4Q FCF +               25    全正=pass; 1季负=warn; 多季负=fail
  Q YoY FCF              15    正增长=pass; 否则=fail
  4Q Buyback             10    有=pass; 无=warn
  Q OCF/NI                5    >0.8=pass; 0.5-0.8=warn

===================================================================
BALANCE SHEET
===================================================================

--- 3yr (100 pts) ---
  D/E Trend              35    不上升=pass; 累计升≤0.30=warn; 明显恶化=fail
  CR Trend               35    不下降=pass; 累计降≤0.30=warn; 明显恶化=fail
  GW/Assets Trend        30    不上升=pass; 累计升≤0.05=warn; 明显恶化=fail

--- TTM (100 pts) — 最新季 vs 一年前同季 YoY ---
  AR vs Revenue          35    AR增速≤Rev增速×1.5=pass; 否则=fail
  AP vs Revenue          30    AP增速≤Rev增速×1.5=pass; 否则=warn
  Inventory vs Revenue   10    Inventory增速≤Rev增速×1.5=pass; 否则=warn; 无存货=skip
  CapEx/OCF              25    <50%=pass; 50-80%=warn; >80%=fail
                               (OCF>0且营收正增长→可豁免为warn)

--- 5Q (100 pts) ---
  Cash/Debt              25    >0.5=pass; 0.3-0.5=warn; 无债务=pass
  Debt/Equity            20    <1.0=pass; 1.0-2.0=warn; >2.0=fail
                               (负权益+现金/债务>0.3→warn)
  Current Ratio          15    >1.0=pass; 0.8-1.0=warn; 剔除递延收入后>1.0亦pass
  AR YoY                 20    AR增速≤Rev增速×1.5=pass; 否则=fail
  AP YoY                 20    变动<50%=pass; 否则=fail

--- Risk Flags (BS 附加扣分，最高 -15) ---
  商誉减值: GW+Intangibles/Assets>30% 且 NI连续下降 → -10
  表外负债: Lease/Assets>20% → -5
"""
