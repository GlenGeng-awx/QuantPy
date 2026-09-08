# Task 3: Fisher 15 + 折扣系数

> **产出**: 质量档 (伟大/好公司/平庸) + 麻烦档 (无麻烦/存疑/重麻烦) + 折扣系数 + r + 总结。
> 
> **依赖**: output_1 (SCORECARD 损伤 + 趋势表 + 背离检验) + output_2 (g 多档位 → #1 可持续性) + web (负面搜索)。
> 
> Fisher 15 是通用质量清单, 不限成长/价值。15 条天然分两维: 质量 (公司固有好坏) + 麻烦 (当前处境好坏) → 2D 折扣系数。
> 
> **output_3.md 结构 = 本文档节序 (§3.1→§3.2→§3.3); 各 § 节的表格式即 output 格式, 不另设模板。**

### 串行输入 (读前序 output)

- **output_1 定量损伤评估**: "→ Fisher 15 追查" 列 → 指引哪些条目需重点搜
- **output_1 趋势表**: Revenue/GM/NM/SBC 趋势 → #5 (利润率) / #6 (margin 改善) / #13 (稀释) 定量输入
- **output_2 g 多档位**: g 范围 + YoY 方向 → #1 (市场可持续性) 判断 (g 加速 = 市场支撑增长; g 减速 = 市场成熟/萎缩)

## §3.1 评估

### Fisher 15 条 + 两维分拆

```
#1  产品/服务是否有足够大的市场空间支撑数年增长？    [否决项]
    补充: 市场增长是否健康 (公司能从中获利)？技术是否在改变价值分配 (市场增长但定价权下降)？
#2  管理层是否有决心开发新产品/工艺来扩大销售潜力？
#3  R&D 效率如何（相对公司规模）？
#4  是否有优秀的销售组织？
#5  是否有值得的利润率？
    补充: 利润率趋势是否结构性下降？技术商品化是否在侵蚀定价权？
#6  在做什么来维持/改善利润率？
    补充: margin 下降是否来自结构性因素 (技术商品化/竞争加剧) 而非一次性投资？
#7  劳工关系是否出色？
#8  高管关系是否出色？
#9  管理层是否有深度？
#10 成本分析和会计控制有多好？
#11 是否有其他方面给投资者优于竞争对手的洞察？
    补充: 护城河的性质是否在变？技术是否在让公司从"必需品"变为"商品"？竞争对手是否在改变游戏规则 (非抢份额而是重新定义价值)？
#12 短期还是长期视角？
    补充: 公司是否在经历商业模式转换 (高价低量→低价高量；许可→订阅→freemium)？转换是否能持续盈利？
#13 股权融资是否会稀释现有股东？
#14 顺境时坦白，逆境时是否"闭嘴"？
#15 管理层诚信是否毋庸置疑？                        [否决项]
```

> 补充问题 (#1/#5/#6/#11/#12) 在判定时加权: 如补充问题为"是" (风险存在) → 该条目至少 borderline；如补充问题严重影响 → borderline→fail

| 维度 | Fisher 条目 | 评什么 |
|------|-----------|--------|
| **质量** (10 条) | #2,#3,#4,#5,#7,#9,#10,#11,#12,#13 | 公司行不行 |
| **麻烦** (5 条) | #1,#6,#8,#14,#15 | 公司现在有没有麻烦 |

### PK 三态

```
PK 只有三态: pass / fail / borderline
  borderline = neutral: 有顾虑但没到 fail, 既非 pass 也非 fail

计分 (两维度对称, 都数 PASS):
  质量维度 (数 PASS, §3.2): borderline 不计入 PASS → 有 cost (不贡献)
  麻烦维度 (数 PASS, §3.2): borderline 不计入 PASS → 有 cost (不贡献)
  → borderline 在两维度都不贡献 PASS = 隐性降档 (borderline 越多 → PASS 越少 → 档越低)

使用:
  偏 pass → 标 pass; 偏 fail → 标 fail; 真中立 → borderline
  不写 "borderline PASS"/"borderline FAIL" (含糊), 要么 commit 要么 neutral
```

### 每条评估流程 (LLM 优势 = 多搜 + 综合)

```
#{n} {question} [{否决项/可不过}]

搜索层级 (递进, 非穷举):
  1. broad:      "{company} {item topic}"           → 正面 + 背景
  2. negative:   "{company} {negative keywords}"     ← 必须搜
  3. follow-up:  追问 who/what/when/why               ← 负面发现时
  4. deep dive:   事件时间线/影响/对比                ← 必搜条目 + 重大负面

负面搜索结果:
  无结果 → 支持 PASS
  有结果 → follow-up → 如重大 → deep dive (多源交叉验证)

PK: pass / fail / borderline
```

**核心规则:**
- 每条 PASS 必须附 negative_search_result (证明搜过负面)
- 否决项 (#1, #15) 的 FAIL 需要至少 2 个独立 source
- 负面搜索是触发器, 不是终点 — 找到问题后必须追问一层
  - #8 高管变动 → "who replaced? how long gap? forced or voluntary?"
  - #14 管理层归因 → "blamed what? was it accurate? competitors resilient?"
- ⚠ 搜索未执行 (captcha/失败) ≠ 无结果; 未搜索项不 default PASS, 标"未搜索"; DuckDuckGo 失败 → 用 playwright 补搜
- LLM 优势: 人类只搜 1-2 次/条; LLM 可搜 3-5 次/条 (broad + neg + follow-up + deep dive) → 多源交叉验证

### 搜索优先级

| 类别 | 条目 | 能否从 data 推断 | 搜索要求 |
|------|------|-----------------|----------|
| **必搜** | #8 高管 | ❌ 财报无离职信息 | web search; 失败 → playwright; 仍失败 → 标"未搜索" |
| | #15 诚信 [否决] | ❌ SEC/欺诈不在财报 | 同上 |
| | #7 劳工 | ❌ 裁员/文化不在财报 | 同上 |
| | #14 坦白 | ❌ 管理层是否隐瞒要搜 | 同上 |
| | #11 护城河 | 部分 (GM=护城河) | 建议搜竞争动态 |
| | #2 新产品 | 部分 (Rev 增长隐含) | 建议搜产品/管线 |
| | #1 市场 [否决] | 部分 (g=市场支撑) | 建议搜 TAM/份额 |
| **可 default** | #5 利润率 | ✓ NM from output_1 | 标"from data" |
| | #13 稀释 | ✓ SBC+buyback from output_1 | 标"from data" |
| | #4 销售 | ✓ Rev Q YoY from output_2 | 标"from data" |
| | #3 R&D | ✓ R&D/Rev from output_1 | 标"from data" |
| | #6 margin | ✓ 趋势 from output_1 | 标"from data" |
| | #10 成本 | ✓ BS/会计 from output_1 | 标"from data" |
| | #9 管理深度 | 部分 (info.json) | 标"from data" |
| | #12 长期 | 部分 (g from output_2) | 标"from data" |

output 格式 — 汇总表 (质量 10 条, 快速扫描):

| # | 条目 | 判定 | 关键 |
|---|------|------|------|
| #2 | (问题简述) | pass/fail/borderline | (≤50字 关键发现) |
| ... | ... | ... | ... |

output 格式 — 汇总表 (麻烦 5 条, 快速扫描):

| # | 条目 | 判定 | 关键 |
|---|------|------|------|
| #1 | (问题简述) | pass/fail/borderline | (≤50字 关键发现) |
| ... | ... | ... | ... |

output 格式 — 详细分析 (每条叙事, 非 bullet):

```
#### #{n} {问题简述} [{否决项}]

{300-500字 narrative: 搜了什么 → 发现了什么 → 正面负面综合分析 → 为什么这样判定}

**判定**: pass/fail/borderline — {一句话理由}
**来源**: [url1], [url2], ...
```

> "from data" 条目: 标注来源 (output_1/3), 简述为何不搜或搜无果
> "未搜索" 条目: 不 default PASS, 标"未搜索 (captcha/失败)"

output 格式 — 搜索汇总表:

| # | 搜索词 | 关键发现 | 来源 |
|---|--------|---------|------|
| #5 | "Coupang margin pressure" | NM -2.2%, OpInc -$628M | earningslens.ai |
| #7 | "Coupang worker death safety" | 工人死亡 + 员工数据滥用 | KEI, FinancialContent |
| ... | ... | ... | ... |

> 列出所有实际执行的搜索 (broad + negative + follow-up + deep dive), 不列未执行的

output 格式 — 跨条目关联:

| 事件 | 影响条目 | 关联说明 |
|------|----------|---------|
| (事件名) | #N1, #N2, ... | (一个事件如何同时影响多条) |
| (趋势名) | #N1, #N2, ... | (一个趋势如何跨条目体现) |

> 关联表帮助 Task 5 理解: 多条 FAIL 是否同根因 (去重依据 §FAIL 去重)?

### 15 条预定义搜索

```
#1  pos: "{company} market size TAM growth outlook"
    neg: "{company} market share loss competition threat declining"
    fail if: 市场萎缩 or 增速 <3%
    ⚠ 份额流失不是 #1 FAIL — 那是 #4/#11
    补充: "{company} pricing power erosion technology value redistribution"

#2  pos: "{company} new product launch innovation pipeline"
    neg: "{company} product failure discontinued delayed"

#3  pos: "{company} R&D investment technology platform"
    neg: "{company} R&D inefficiency technology lag competitor"

#4  pos: "{company} sales growth customer acquisition"
    neg: "{company} customer loss revenue miss declining sales"

#5  pos: "{company} gross margin net margin profitability"
    neg: "{company} margin decline profitability deteriorating"
    pass if: NM > 8% 或 (GM > 40% + Rev 高增长 + NM 改善中)
    补充: "{company} pricing power commoditization margin structural decline"

#6  pos: "{company} margin improvement operating leverage"
    neg: "{company} margin pressure cost rising competition pricing"
    补充: "{company} margin structural decline vs investment phase AI arms race"

#7  pos: "{company} employee satisfaction glassdoor"
    neg: "{company} employee turnover toxic culture layoffs strike"

#8  pos: "{company} executive team stability retention"
    neg: "{company} executive departure CFO CTO resign leave turnover"
    follow-up: "{company} new CFO CRO appointed replacement {year}"
    fail if: C-level 离职 or 多名高管同时离开
    ⚠ 判定 = 分析日状态, 离职旧闻 ≠ 当前: 已补位 (有序过渡) → borderline;
      空缺 or churn (多任短任期) → fail (TTD 教训: 1月解雇, 7月已重建 5 人)

#9  pos: "{company} management depth organizational strength"
    neg: "{company} management depth weakness chaos restructuring"

#10 pos: "{company} cost control operating efficiency"
    neg: "{company} accounting restatement cost overrun control failure"

#11 pos: "{company} competitive advantage moat market position"
    neg: "{company} competitive disadvantage losing edge moat eroding"
    补充: "{company} moat type changing technology disruption business model commoditization"

#12 pos: "{company} long-term strategy vision"
    neg: "{company} short-term focus quarterly short-sighted"
    补充: "{company} business model transition freemium subscription pricing power viability"

#13 pos: "{company} buyback low dilution shareholder friendly"
    neg: "{company} dilution stock offering SBC excessive"

#14 pos: "{company} management transparency honest guidance"
    neg: "{company} guidance miss blame macro misleading spin"
    fail if: 将结构性恶化包装为"暂时性逆风"

#15 pos: "{company} CEO integrity reputation ethical"
    neg: "{company} SEC investigation scandal fraud lawsuit accounting"
    [否决项] fail if: 会计欺诈/SEC 调查/重大诚信问题
```

### FAIL 去重

```
≥3 条 FAIL 且根因相同 → 风险提示中合并为 1 条 (仅展示)
(注: 麻烦维度数 PASS, FAIL 不计分; 此规则仅影响风险提示展示)
否决项 FAIL 不参与合并
```

## §3.2 评分 → 折扣系数 + r

### 质量评分

```
质量项 (10 条): #2,#3,#4,#5,#7,#9,#10,#11,#12,#13
  ≥9/10 PASS → 伟大
  6-8/10    → 好公司
  ≤5/10    → 平庸
(borderline 不计 PASS)
```

### 麻烦评分

```
麻烦项 (5 条): #1,#6,#8,#14,#15
  (数 PASS, 和质量维度对称; borderline 不计 PASS)

  4-5/5 PASS → 无麻烦 / 明确一次性
  2-3/5 PASS → 存疑
  0-1/5 PASS → 重麻烦
```

### 折扣系数 (2D 映射: 质量 × 麻烦 → ×系数)

```
                   无麻烦(4-5 PASS)    存疑(2-3 PASS)    重麻烦(0-1 PASS)
  伟大              ×1.0               ×0.85            ×0.67
  好公司            ×0.85              ×0.70            ×0.50
  平庸              ×0.67              ×0.50            ×0.40
```

### r 定档

```
r = 质量维度定档:
  伟大 (≥9/10 质量)  → r = 9%
  好公司 (6-8/10)   → r = 10%
  平庸 (≤5/10)      → r = 11%
```

### Override

```
硬规则 (override 2D 系数):
  FCF-SBC < 0 → ×0.40 (不否决, 总是估值)

否决项 override:
  #1 或 #15 FAIL → 麻烦档至少 存疑 (无论 PASS 数)
  (否决项 FAIL = 严重信号, 不因其他条目 pass 而降档)

价值陷阱过滤器 (override 或叠加):
  触发: #1 市场萎缩 + #6 利润率恶化 + #14 不坦白, 三条中 ≥2 FAIL
  档 A: FCF-SBC ≤ 0 OR Revenue YoY < 0 → ×0.40 (强制)
  档 B: FCF-SBC > 0 AND Revenue YoY ≥ 0 → g=0 估值 + ×0.70
  → 被 2D 系数的 "存疑/重麻烦" 行覆盖 (×0.50~×0.70)
  → 硬规则 FCF-SBC < 0 → ×0.40 进一步 override
```

### output 格式

| 质量档 | 麻烦档 | 折扣系数 | r |
|--------|--------|----------|---|
| (伟大/好公司/平庸) | (无麻烦/存疑/重麻烦) | ×{val} | {%} |

> 质量 {N}/10 PASS → {档}; 麻烦 {N}/5 PASS → {档}
> Override: 硬规则 {是否触发 ×0.40}; 否决项 {#1/#15 是否 FAIL}; 价值陷阱 {是否触发}

---

## §3.3 总结 (→ Task 5 快速消费)

| 项 | 内容 |
|----|------|
| 一句话定性 | (伟大/好公司/平庸) + (无麻烦/存疑/重麻烦); 一次性 vs 结构性判断 |
| 关键 flag | 质量档 + PASS 数; 麻烦档 + FAIL 分; 否决项 #1/#15 状态; borderline 条目; 硬规则触发?; 价值陷阱触发? |
| 折扣系数 + r | ×{val}; r = {%}; override? |
| Top risk | Task 5 需关注: 折扣是否足够? borderline 条目风险? 麻烦是一次性还是结构性? |
