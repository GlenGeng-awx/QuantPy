# Task C：增长前瞻 + 护城河 + 管理层 + 消息面

> 被引用自 `analysis_framework.md`。Task C = 消息面（g + 护城河 + 管理层 + 新闻 + 熊牛）。
> 数据源：web search（最贵，需 focus）+ 本地 CSV（g 的历史基线，免费）。

## 目标

产出**前瞻 g**（进 Task D 的 PE 公式）+ 护城河/管理层/消息面（进折扣系数 + 熊牛逻辑）。

---

## C.1 增长前瞻（产出 g）

g 的计算（8 源交叉验 + 综合判断 + 护栏）详见 **`forward_g.md`**。

本 stock g = {N}%（{列出 g 源、剔除项、均值计算}）

### g 质量护栏（详见 `forward_g.md` G-4）

- [✓/✗] FCF − SBC > 0（< 0 → 重麻烦 ×0.40，不否决）
- [✓/✗] 回购不进 g
- [✓/✗] 增长持续性（护城河支撑？）
- [✓/✗] g ≥ 22% → 封顶 30x

---

## C.2 护城河

### 壁垒类型（四类）

| 类型 | 说明 | 例子 |
|------|------|------|
| 网络效应 | 用户越多价值越高 | Visa/Mastercard、Meta |
| 切换成本 | 客户迁移代价高 | MSFT (Office/Azure)、CRM |
| 规模/成本 | 规模优势压低成本 | KO 装瓶网络、COST |
| 品牌/牌照 | 品牌心智或监管壁垒 | KO 品牌、JPM SIFI 牌照 |

### 检查项

```
2a. 壁垒类型是什么？（四类之一或组合）
2b. 份额趋势？（稳固/扩张/流失）
2c. 威胁？（新进入者/技术替代/监管/客户垂直整合）
2d. 壁垒是否在侵蚀？（如 Apple 自研 modem → QCOM 份额归零）
```

护城河宽度 = **Task D 折扣系数的质量评分第 7 分**（+1 = 宽）。

---

## C.3 管理层

### 检查项

| # | 项目 | 数据来源 | 看 |
|---|------|---------|-----|
| 1 | CEO 任期/背景 | web search | 创始人 vs 职业经理人，内部晋升 vs 空降 |
| 2 | **CEO 继任/退休计划** | web search（**必查**） | 已宣布退休/过渡/COO 总裁升迁信号 = 重大变化，不能只看现任任期 |
| 3 | 内部人增减持 | web search (SEC Form 4) | 公开市场增持 = 最强看多；卖出 = 弱看空 |
| 4 | 资本配置 | income/cf CSV + web | 回购时机/M&A 成败/SBC 趋势 |
| 5 | 指引 vs 实际 | 逐季对比 | 连续 beat 还是连续 miss |
| 6 | 治理风险 | web search | 空缺/VIE/双层股权/诉讼 |

### 红线

```
零回购 + 零分红 → 重大负面（尤其 VIE）
CEO 退休/继任计划已宣布 → 重大变化，必须标注（不能只写现任任期就完）
CEO 空缺/换帅 → 治理 overhang
创始人售股 → 弱看空（可能税务/遗产规划，非强信号）
CEO 公开市场增持 → 最强看多
```

> ⚠ **常见错误**：只写"CEO XXX（N 年）"就完——必须 web search 查是否有退休/继任/过渡公告。Narayen 19 年任期不代表还在位，可能已宣布交接。
>
> ⚠ **info.json `companyOfficers` 可能 stale**：字段更新滞后，已交接的 CEO title 可能仍标旧人（或新旧人并列、title 混乱）。**不要直接信 info.json 的 CEO title**——必须 web search 官方 IR（如 `corporate.walmart.com/about/leadership`）确认现任 + 交接生效日。案例：WMT info.json 列 Furner 为 CEO（对），但旧报告 `analysis.base.md`（2026-07）仍写 McMillon（错，Furner 2026-02-01 已接任）——报告历史也会 stale，以官方 IR 为准。

---

## C.4 消息面（近 3 月）

### 方法

```
web search: STOCK + news/CEO/earnings/lawsuit/rating 关键词
RSS: Yahoo Finance headline feed（周度扫描）
```

### 关注的事件类型

| 类型 | 例子 | 对 thesis 影响 |
|------|------|---------------|
| CEO 变动 | 罢免/空降/换帅 | 重大 |
| 诉讼 | 集体诉讼/监管调查 | 中-重大 |
| 评级 | S&P 降级/分析师升级 | 中 |
| 收购重组 | 业务剥离/IPO/M&A | 重大 |
| 财报 | beat/miss/指引变化 | 高频 |

### 与 diff 规则的配合

```
两路 diff:
  ① combine diff: combine 输出 vs output 文件
  ② 消息面 diff: WebSearch 近 3 月 vs output_c 记录的消息面

两路都 trivial → 不动
任一 non-trivial → reconfirm → 结论变才改 output，不变则不动
```

---

## C.5 熊市逻辑 / 牛市逻辑

### 熊市逻辑

列出所有看空论据，**带数字**（增速%/bps/倍数/占比/绝对额）：
- 估值：PE/EV/EBITDA 多少，分位多少
- 增长：放缓/停滞/负增长
- 竞争：份额流失、GM 侵蚀
- 资本：FCF 转负、杠杆过高
- 管理层：CEO 卖股、指引 miss

### 牛市逻辑

列出所有看多论据，**带数字**：
- 估值：便宜（P/E/回撤/分位）
- 增长：加速/新引擎/前瞻共识
- 护城河：壁垒稳固/扩张
- 资本：FCF 强/真缩股/分红
- 催化：监管叫停/管线兑现/周期反转

**不许写"健康/强劲"这类无数字断言。**

---

## 与其他 Task 的关系

| 输入 | 来源 |
|------|------|
| GM/OpInc CAGR（g 基线） | 本地 CSV（与 B 同源，不依赖 B 输出） |
| 分析师共识 / 管理层指引 | web search |
| 消息面历史记录 | `ai_report/{STOCK}/analysis.base.md` |

| 输出 | 去向 |
|------|------|
| **g** | Task D（PE = min(8.5+g, 30)） |
| **护城河宽度** | Task D（折扣系数质量评分 +1） |
| **麻烦定性** | Task D（折扣系数交叉查表） |
| 熊牛逻辑 | 分析报告正文 |

C 是**成本中心和瓶颈**——web search 最贵，最先启动、最后完成、逐只精做。
