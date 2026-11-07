# 参考表 (v3) — 纯查表, 不含规则

## 固定参数 (v2 遗产)

| 参数 | 值 |
|------|-----|
| DCF N / g_terminal | 5 年 / 3% |
| DCF r | 9/10/11% (伟大/好/平庸) — L2d 三档试算, L4 选行 |
| Graham PE / Fisher PE | 8.5+g / 8.5+2g (g<0 封底 8.5) |
| 分位反推 Nth | 30th |
| derating 阈值 | g < 5yr avg × 0.70 |
| CSP sigma N / T | 2.5 / 15 交易日 |
| 折扣系数 2D 表 | Fisher 30 §计分 (×1.0/0.85/0.70/0.67/0.50/0.40) |
| 硬规则 | FCF-SBC<0 → ×0.40 |
| 恐惧体积阈值 | ≥1.5× 错杀候选; <1 负体积; 赔率 <0.5:1 弃牌线 (24) |

## FX (每 3-5 天更新; 优先 Google Finance spot)

| 币种对 | 近似值 | 标的 |
|--------|--------|------|
| CNY/USD ~6.8 / CNY/HKD ~1.1 / TWD/USD ~32 / EUR/USD ~1.15 / DKK/USD ~6.5 / SEK/USD ~10.5 / SGD/USD ~1.35 | | (2026-08-19 更新; NVO 9/30 实测 6.59) |

> 不可信 info.json 字段 (多币种): trailingEps/PE/PB/EV-EBITDA/PS/EV/bookValue; 可信: currentPrice/marketCap/shares/52w/dividendYield/beta。

## Edge Cases (v2 遗产指针)

亏损转换 / 银行股 P/B / 半年报 detector 假阳性 / 并购 step-up / 多币种 ADR / 短历史分位 / CapEx 超级周期 / SBC+回购 / P/E 破低 / 季度 CSV 缺列 — owner 各对应文件。

## 大师出处书单 (v3)

| 大师 | 原典 | 条目出处 |
|------|------|---------|
| Fisher | 《怎样挑选成长股》(Common Stocks and Uncommon Profits, 1958) | 15 条 (第一章) + scuttlebutt |
| Graham | 《聪明的投资者》(The Intelligent Investor, 4th ed.) | 第 8/14/15/20 章 + 《证券分析》 |
| Munger | 《穷查理宝典》(Poor Charlie's Almanack, 3rd ed.) | 第十一讲《人类误判心理学》+ 1996 讲 |
| Buffett | 《巴菲特致股东的信》(1957-2023, annually.com 或 counsel) | 1977/1982/1984/1986/1987/1988/1989/1991/1996/2007/2012 信 |
| 段永平 | 《大道》+ 《段永平投资问答录》 | 博客/雪球问答 |

## 校准案例库 (跨案例规则, 持续积累)

| 案例 | 沉淀规则 | 宿主 |
|------|---------|------|
| ADBE 2026-09 | 时效重跑 (漏财报三差异) | 00 §0.5 |
| PYPL 1/30→6-8 | 刀 → 企稳后错杀 | 24 §1 |
| TTD 8/7→9/29 | 足迹=基本面事件; 负体积; 换轴必须 L1 显形 | 10 §3 / 24 |
| NVO 9/30 | 负体积 0.67×; 顶部扩产 kill; 赔率 0.2:1 弃牌; CapEx 回落期权 (gut 对账) | 23 §2 / 32 / 24 |
| NFLX/0700/SE/BILI | 收敛模式库 | 50 §7 |
