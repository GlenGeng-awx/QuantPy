# Task 3: Fisher 15 + 折扣系数

> **产出**: 质量档 (伟大/好公司/平庸) + 麻烦档 (无麻烦/存疑/重麻烦) + 折扣系数 + r + 报告 (调查叙事, §3.3) + 总结。
> 
> **依赖**: output_1 (SCORECARD 损伤 + 趋势表 + 背离检验) + output_2 (g 多档位 → #1 可持续性) + web (负面搜索)。
> 
> Fisher 15 是通用质量清单, 不限成长/价值。15 条天然分两维: 质量 (公司固有好坏) + 麻烦 (当前处境好坏) → 2D 折扣系数。
> 
> output_3.md 结构 = 认知顺序 (调查→判定→计分→总结), 是 §0.5 "output = 文档节序" 全局约定的显式例外 (见 §3.3)。
> - 其他 task 是计算 — 数据进表格出, 表格即内容, 边算边写;
> - Fisher 15 是调查 — 判定从证据里长出来, 弧在搜索中显形, 汇总表只是调查结束后的计分。§3.1 管"怎么判" (规则), §3.3 报告层管"怎么写" (output 格式唯一 owner)。

### 串行输入 (读前序 output)

- **output_1 定量损伤评估**: "→ Fisher 15 追查" 列 → 指引哪些条目需重点搜
- **output_1 趋势表**: Revenue/GM/NM/SBC 趋势 → #5 (利润率) / #6 (margin 改善) / #13 (稀释) 定量输入
- **output_2 g 多档位**: g 范围 + YoY 方向 → #1 (市场可持续性) 判断 (g 加速 = 市场支撑增长; g 减速 = 市场成熟/萎缩)

## §3.1 判定规则 (15 条定义 + 三态 + 搜索协议)

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
  2. negative:   "{company} {negative keywords}"    ← 必须搜
  3. follow-up:  追问 who/what/when/why              ← 负面发现时
  4. deep dive:   事件时间线/影响/对比                 ← 必搜条目 + 重大负面

闲聊视角交叉 (scuttlebutt lens, 与递进层级正交 — 见"闲聊视角"节):
  同一问题换 stakeholder 问 (管理层/员工/客户/竞对/监管)
  意外来自视角碰撞, 不来自挖更深; 管理层单方口径 = 单源, 不算交叉

负面搜索结果:
  无结果 → 支持 PASS
  有结果 → follow-up → 如重大 → deep dive (多源交叉验证)

PK: pass / fail / borderline
```

**核心规则:**
- 经搜索判定的条目: 每条 PASS 必须附 negative_search_result (证明搜过负面); default 条目 (纯水平, 未触发升级) 在速览表 "负面搜索" 列标 "default (未升级)" — 与 "未搜索" (captcha/失败) 是两个状态
- 否决项 (#1, #15) 的 FAIL 需要至少 2 个独立 source
- 负面搜索是触发器, 不是终点 — 找到问题后必须追问一层
  - #8 高管变动 → "who replaced? how long gap? forced or voluntary?"
  - #14 管理层归因 → "blamed what? was it accurate? competitors resilient?"
- ⚠ 搜索未执行 (captcha/失败) ≠ 无结果; 未搜索项不 default PASS, 标"未搜索"; DuckDuckGo 失败 → 用 playwright 补搜
- LLM 优势: 人类只搜 1-2 次/条; LLM 可搜 3-5 次/条 (broad + neg + follow-up + deep dive) → 多源交叉验证

### 搜索优先级 + from data → 必搜升级

**设计哲学 = Fisher 闲聊法 (scuttlebutt), web search 就是我们的"闲聊"** — 跟各 stakeholder 了解情况。应搜尽搜, 但成本可控: 数据没问题时纯水平条目可 default, 疑点出现时升级。

| 类别 | 条目 | 能否从 data 推断 | 搜索要求 |
|------|------|-----------------|----------|
| **必搜** | #8 高管 | ❌ 财报无离职信息 | web search; 失败 → playwright; 仍失败 → 标"未搜索" |
| | #15 诚信 [否决] | ❌ SEC/欺诈不在财报 | 同上 |
| | #7 劳工 | ❌ 裁员/文化不在财报 | 同上 |
| | #14 坦白 | ❌ 管理层是否隐瞒要搜 | 同上 |
| **建议搜** | #11 护城河 | 部分 (GM=护城河) | 建议搜竞争动态 |
| | #2 新产品 | 部分 (Rev 增长隐含) | 建议搜产品/管线 |
| | #1 市场 [否决] | 部分 (g=市场支撑) | 建议搜 TAM/份额 |
| **可 default → 必搜升级** | #5 利润率 | ✓ 水平 (NM); 性质要搜 | 触发升级规则 (见下) |
| | #13 稀释 | ✓ 水平; 可持续性要搜 | 同上 |
| | #4 销售 | ✓ 水平 (Rev YoY) | 同上 |
| | #3 R&D | ✓ 水平 (R&D/Rev) | 同上 |
| | #6 margin | ✓ 趋势; 结构 vs 一次性要搜 | 同上 |
| | #10 成本 | ✓ 水平; 会计事件要搜 | 同上 |
| | #9 管理深度 | 部分 (info.json) | 同上 |
| | #12 长期 | 部分 (g) | 同上 |

**from data → 必搜 升级触发** (任一命中):

```
1. output_1 定量损伤 flag 该维度        (如 ADBE #6: OpM 5 季下滑被损伤表 flag)
2. 该条目判定将落在 borderline 候选       (判定悬在补充问题上 → 数据答不了"性质")
3. 补充问题问"性质"非"水平"              (#5/#6 margin 性质 / #9 梯队 / #12 模式转换 / #10 会计事件)

纯水平条目 (数据没问题) 维持 default: #3 R&D / #4 销售 / #13 稀释
  → 数字本身就是答案; 升级触发命中时才搜 (应搜尽搜 ≠ 全量搜, = 疑点驱动)
```

### 闲聊视角 (scuttlebutt lens)

Fisher 闲聊法的杠杆是**视角交叉**, 不是递进深度 — 意外来自"换个人问", 不来自"挖更深"。管理层口径 = 单源, 不算交叉。

| 闲聊对象 | 信息源 |
|----------|--------|
| 管理层 | 指引 / 电话会 / 采访 |
| 员工 | Glassdoor / Blind / TheLayoff / 裁员备案 (Cal-WARN) |
| 客户 | 用户社区 / 续费流失报道 / 渠道 |
| 竞对 (的用户) | 竞品社区替换讨论 / 对比评测 |
| 监管/媒体 | 执法 / 诉讼 / 深度报道 |

```
规则 (只对必搜 + 升级条目生效):
  必搜/升级条目 ≥2 个闲聊视角
  判定悬在补充问题上的条目 ≥3 个 (管理层单方口径 = 单源, 不算交叉)
成本: 每条 +1-2 次搜索 — 换判定从"管理层说"升级到"多方对质"
```

例: #6 margin 降 — 递进式只搜 "margin pressure"; 闲聊式 = 管理层说"投资期" (指引) + 员工说 G&A 花在哪 (Blind) + 客户说有没有被涨价 (用户社区) — 三方对质, 结构 vs 一次性自然显形。

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
≥3 条 FAIL 且根因相同 → 总结 Top risk (§3.4) 中合并为 1 条 (仅展示)
(注: 麻烦维度数 PASS, FAIL 不计分; 此规则仅影响展示)
否决项 FAIL 不参与合并
```

> **本节 (§3.1) 只管规则**: 15 条怎么判、搜索怎么跑、PK 三态、去重 — 全部 output 格式 (含汇总表/折扣表/关键列写法) 见 §3.3 报告层 (唯一 owner)。

## §3.2 计分规则 (判定 → 档位 → 折扣系数 + r)

### 质量评分

```
质量项 (10 条): #2,#3,#4,#5,#7,#9,#10,#11,#12,#13
  ≥9/10 PASS  → 伟大
  6-8/10      → 好公司
  ≤5/10       → 平庸
(borderline 不计 PASS)
```

### 麻烦评分

```
麻烦项 (5 条): #1,#6,#8,#14,#15
  (数 PASS, 和质量维度对称; borderline 不计 PASS)

  4-5/5 PASS  → 无麻烦 / 明确一次性
  2-3/5 PASS  → 存疑
  0-1/5 PASS  → 重麻烦
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
  优先级: 档 B 的 ×0.70 是上限 — 2D "存疑/重麻烦" 行 (×0.50~×0.70) 更低时取 2D;
          档 A / 硬规则 (FCF-SBC < 0 → ×0.40) 为最终 override, 2D 系数盖不过
```

---

## §3.3 报告层 (output 叙事格式 — 唯一 owner)

> **§3.1 管"怎么判", 本节管"怎么写"。** output_3 的全部格式在此定义 — 含机器层 (汇总表 ×2 + 折扣表 + 关键列写法, 本节"机器层格式"小节) 与故事层。
>
> **双层设计**:
> - **机器层** (Task 5/E 机械消费): 汇总表 ×2 + 折扣表 (本节"机器层格式"小节) + 总结 (§3.4)
> - **故事层** (人读): 故事卡 + 叙事弧 + 深挖 + 反直觉发现 + 翻案条件
>
> **合规不降** (07_checklist 全部保留): 15 条全判定 + 每条经搜索判定的 PASS 附负面搜索证据 (default 未升级条目在速览表标注) + 来源 URL。故事层只重新分配篇幅, 不减少证据 — from-data 条目进速览表, 搜索动作全量记录进搜索汇总表。

### 报告结构 (output_3.md) — 认知顺序, 非节序

**为什么打破节序**: Fisher 15 的工作流是"边搜边写", 不是"边算边写"——前一条搜索的发现改变后一条的搜法 (搜 #15 发现 DOJ → 波及 #14; 搜 #8 发现空缺 → 关联 #9), 弧在调查中显形, 判定是弧的计分。先写判定表再补故事 = 先判决书后卷宗。叙事优先 = 写作顺序 = 认知顺序 = 阅读顺序。Task 5/E 机械消费不受影响 (grep 表格不看位置)。

```
# {STOCK} — Task 3: Fisher 15
> 元信息行 (更新日期 / 串行输入 / web 搜索范围)
> **故事卡** (§3.3.1, 100-150 字)          ← 报告头, 30 秒读完

## 调查 — 叙事 (规则 §3.3.2-3.3.5)          ← 边搜边写, 先成文
  3-5 个叙事弧 (含深挖条目, 每弧 200-400 字)
  速览表 (from-data 条目, 证据不减)
  反直觉发现 (1-3 条)
  borderline 翻案条件表
  附: 跨条目关联表 (弧骨架) + 搜索汇总表 (合规审计)

## 判定 — 15 条汇总 (规则 §3.1)             ← 调查收口后填表 (数 PASS)
  质量 10 条表 + 麻烦 5 条表 (机器层; 深挖条目 ★) + PASS 计数

## 计分 — 折扣系数 + r (规则 §3.2)

## 总结 (规则 §3.4)
```

> 章节标题用语义名 (调查/判定/计分/总结) + 括号里 § 指针标规则归属 — 不带 § 序号排序, 顺序 = 认知顺序。
> 写作流程: 搜索中发现即落笔成弧 (草稿) → 弧收口 → 填判定表 (15 条判定此刻才定稿) → 计分 → 总结。

### 机器层格式 — 汇总表 ×2 (产出 = §3.1 判定; 格式 owner = 本节)

output 格式 — 汇总表 (质量 10 条, 快速扫描; 深挖条目加 ★, 见 §3.3.3):

| # | 条目 | 判定 | 关键 |
|---|------|------|------|
| #2 | (问题简述) | pass/fail/borderline | (≤50字 关键发现) |
| ... | ... | ... | ... |

output 格式 — 汇总表 (麻烦 5 条, 快速扫描; 深挖条目加 ★):

| # | 条目 | 判定 | 关键 |
|---|------|------|------|
| #1 | (问题简述) | pass/fail/borderline | (≤50字 关键发现) |
| ... | ... | ... | ... |

**关键列写法** (机器层唯一叙事单元格): 数字 + 语境, 不写动作、不写分类词。判定的证据压缩成一句人话。

- ✗ "回购 4.5x SBC" → ✓ "$9.3B 回购 = SBC 4.5x, 四年股数 -16%, 但吃了 88% FCF"
- ✗ "R&D 效率高" → ✓ "R&D 18% Rev, Rev 增速跑赢 R&D 增速"
- pass 条目允许轻量反差 (发现一个正面意外) — 这是速览表唯一的"故事配额"

### 机器层格式 — 折扣表 (产出 = §3.2 计分; 格式 owner = 本节)

| 质量档 | 麻烦档 | 折扣系数 | r |
|--------|--------|----------|---|
| (伟大/好公司/平庸) | (无麻烦/存疑/重麻烦) | ×{val} | {%} |

> 质量 {N}/10 PASS → {档}; 麻烦 {N}/5 PASS → {档}
>
> Override: 硬规则 {是否触发 ×0.40}; 否决项 {#1/#15 是否 FAIL}; 价值陷阱 {是否触发}
>
> (引用块内多行之间必须加空 `>` 行 — 连续 `>` 行在 CommonMark 里合并为单段落渲染)

### §3.3.1 故事卡 (报告头, 100-150 字)

模板:

```
**{STOCK}**: {一句生意定性, 带数字锚}。{一句市场叙事 — 它为什么跌/为什么有麻烦}。
带着这个故事去搜证据: {核心发现一句}。{次要发现一句}。
**{质量档} × {麻烦档} → ×{折扣}**
```

ADBE 例:

> **ADBE**: NM 28% 的创意软件现金牛, 一年跌掉一半市值。市场讲的故事是 "AI 民主化创意工具, Adobe 定价权要完"。带着这个故事去搜证据: 护城河在磨损但没破 — GM 89% / FCF $10.6B 仍是统治级; 真正的麻烦是三件小事叠加: CFO 椅子空了 3 个半月、DOJ 3 月罚了 $150M、margin 压缩被管理层自己的指引确认。**好公司 (7/10) × 存疑 (2/5) → ×0.70**。

### §3.3.2 叙事弧 (3-5 个)

- **弧来源 = 跨条目关联表的根因 cluster**。孤立条目不硬造弧 — 信息量大的 (如判定与共识冲突) 按 §3.3.3 深挖配额单独深挖, 其余进速览表
- 每弧 200-400 字, 结构: 标题 → 事件时间线 → 验证过程 (搜了什么 + **反方证据**) → 波及条目与判定 → 一句弧结论
- 弧标题写冲突不写分类: "换帅进行时" 而非 "高管分析"; "AI 颠覆疑云" 而非 "#11 评估"
- 弧内含深挖条目 (300-500 字, 格式见下方模板):

```
#### #{n} {question} [{否决项}]

{300-500字 narrative: 搜了什么 → 发现了什么 → 正面负面综合分析 → 为什么这样判定}

**判定**: pass/fail/borderline — {一句话理由}
**来源**: [url1], [url2], ...
```

### §3.3.3 深挖配额 + 速览表

深挖对象 (300-500 字/条, **上限 5 条**), 按信息量分配篇幅:

| 深挖对象 | 理由 |
|----------|------|
| 弧主条目 | 故事骨架 |
| 否决项 #1/#15 (无论判定) | 一票否决权 |
| fail 且有事件 | 判定最重 |
| 判定与市场共识/直觉冲突 | 信息量最大 |

其余条目 (from data 默认) → **速览表** (一行一条, 证据不减 — 判定+数字+语境+负面搜索结果):

| # | 条目 | 判定 | 一句话关键 (数字+语境) | 负面搜索 |
|---|------|------|----------------------|---------|
| #3 | R&D 效率 | pass | R&D 18% Rev, Rev 增速 > R&D 增速 | 无结果 |
| ... | ... | ... | ... | ... |

> "未搜索" 条目: 不 default PASS, 标"未搜索 (captcha/失败)" — 速览表同口径

### §3.3.4 反直觉发现 (1-3 条)

格式: **搜前预期 → 搜后发现 → 对判定的影响**。

- 这是 LLM 多搜优势唯一显形处 (人搜 1-2 次/条, 意外只能来自第 3-5 层)
- 无真意外 → 写 "无反直觉发现", 不硬凑

### §3.3.5 borderline 翻案条件表

| # | 现判定 | 翻 pass 需要 | 翻 fail 需要 |
|---|--------|-------------|-------------|
| #6 | borderline | Q4 OpM ≥36% | 连续第 6 季下滑 + freemium ARPU 崩 |

> 只列 borderline + 近边界条目。人读 (期望管理): 翻案条件 = 持仓期间的降级/升级监控清单, 不进 Task E 机械消费

### §3.3.6 语言规则

| ✗ 过程日志 | ✓ 叙事 |
|------------|--------|
| "负面搜索无结果" | "专门搜了 SEC 调查 — 什么都没有; 这个空白就是 #15 没翻 fail 的证据" |
| "CFO 空缺 3.5mo" | "Durn 6 月走 → Day 顶上 → 9/6 媒体还在问 'CFO 搜索怎么样了' → 今天椅子还空着" |
| "回购 4.5x SBC" | "$9.3B 回购是 SBC 的 4.5 倍, 四年股数 -16% — 但买单的是 88% 的 FCF 和 $1.8B 短债" |

- 判定行保持机械 (`**判定**: pass — 一句话理由`), 叙事只进正文
- 搜索执行细节 (playwright/日期) 只进搜索汇总表, 不进正文

### §3.3.7 附表 (产出 = §3.1 搜索协议; 格式 owner = 本节)

**跨条目关联** (弧骨架):

| 事件 | 影响条目 | 关联说明 |
|------|----------|---------|
| (事件名) | #N1, #N2, ... | (一个事件如何同时影响多条) |

> 关联表帮助 Task 5 理解: 多条 FAIL 是否同根因 (去重依据 FAIL 去重)?
> borderline 同根因集中 (≥4 条, 如 ADBE: AI 焦虑吃 #5/#6/#10/#11/#12) → 关联表标 "根因集中" flag (计分不变 — borderline 有 cost 是设计); 人读注记: 该根因证伪/证实 → 多条判定联动 → 档位跳变 (期望管理, 非机械消费)

**搜索汇总表** (合规审计: 人不读, checklist 读):

| # | 搜索词 | 关键发现 | 来源 |
|---|--------|---------|------|
| #5 | "Coupang margin pressure" | NM -2.2%, OpInc -$628M | earningslens.ai |
| ... | ... | ... | ... |

> 列出所有实际执行的搜索 (broad + negative + follow-up + deep dive), 不列未执行的

---

## §3.4 总结 (→ Task 5 快速消费)

| 项 | 内容 |
|----|------|
| 一句话定性 | (伟大/好公司/平庸) + (无麻烦/存疑/重麻烦); 一次性 vs 结构性判断 |
| 关键 flag | 质量档 + PASS 数; 麻烦档 + FAIL 分布; 否决项 #1/#15 状态; borderline 条目; 硬规则触发?; 价值陷阱触发? |
| 折扣系数 + r | ×{val}; r = {%}; override? |
| Top risk | Task 5 需关注: 折扣是否足够? borderline 条目风险? 麻烦是一次性还是结构性? |
