# 选股分析框架 v2

## 投资哲学

| 哲学家 | 原则 | 对应 Task |
|--------|------|-----------|
| 格雷厄姆 | 好价格（安全边际） | 4（粗筛/分位）+ E（安全边际/操作） |
| 费雪 | 好公司（GM/FCF/护城河） | 1 + 3（Fisher 15） |
| 巴菲特 | 一次性麻烦（暂时困境） | 3（麻烦档）+ E（归类） |

三者缺一不可：

| 条件 | 归类 |
|------|------|
| 只有好价格 | 价值陷阱（便宜的烂公司） |
| 只有好公司 | 买贵了 |
| 好公司 + 好价格但麻烦非一次性 | 结构性恶化 |
| 三者齐备 | **最佳买点** |

## 核心公式（docs/00_framework.md §0.1 是 owner）

```
# EPS 模型（保守下限）
合理价 = 正常化 EPS × PE(g)        # PE = 8.5+g (Graham, 入场基准) 或 8.5+2g (Fisher, 出场基准)
入场价 (满仓) = 合理价 × 折扣系数  # Fisher 15 2D 表; 应用在 Task E Step 3

# DCF（内在价值, 与 EPS 并列）
DCF/sh = 一阶段/两阶段 + net_cash/sh  # g≤3% Gordon; g>3% 两阶段 (N=5, g_terminal=3%)
                                     # base: 回购≤SBC → ⑦FCF-SBC; 回购>SBC → ⑧FCF
回购≤SBC 时: 合理价 = ⑦; 入场价 = ⑦ × 折扣系数

# gap = 置信度信号
EPS vs DCF gap → 看来源 → 决定合理价口径（§5.3 机械规则）
```

## 串行工作流（1→2→3→4→5→E，docs/00_framework.md §0.2 依赖图是 owner）

| Task | 内容 | 产出 |
|------|------|------|
| 1 | 财务健康（SCORECARD + 正常化 EPS + BS 生存力） | output_1 |
| 2 | g 计算（8 源 + g-baseline + 多档位） | output_2 |
| 3 | Fisher 15（质量×麻烦 数 PASS → 2D 折扣 + r） | output_3 |
| 4 | 价格层（粗筛 + 分位门 + derating） | output_4 |
| 5 | 估值（纯引擎：全方法矩阵 + gap + 置信度，不做决策） | output_5 |
| E | 决策（估值能力 → 选可信 → 入场/出场 → 安全边际 → 场景 → 策略 → 归类） | output_e |

每个 task 只读前序 output，不回指。Task E 独有：重取最新 EOD 现价（Task 4 当日价可能已过时）。

## 分析预检（每次分析股票 / 汇总 / 校验前必须完成）

⚠️ 收到任何股票分析请求、或"汇总/校验"请求时，先 read 全部 `docs/*.md`（9 文件，不论一只还是全部）：

1. `docs/00_framework.md` — 全景 + 核心公式 + 依赖图 + 目录结构 + 术语表 + 退役清单
2. `docs/01_financials.md` — 财务健康 + 正常化 EPS（8 检测器）
3. `docs/02_growth.md` — g 计算（8 源 + g-baseline + 多档位）
4. `docs/03_fisher15.md` — Fisher 15 + 数 PASS 评分 + 2D 折扣
5. `docs/04_price.md` — 粗筛 + 分位门 + derating
6. `docs/05_valuation.md` — 估值矩阵（①~⑧ 方法 + gap 诊断）
7. `docs/06_decision.md` — Task E 决策（Step 1-4 + 策略 A/B/C/D + 归类映射）
8. `docs/07_checklist.md` — 提交前自检清单（指针式）
9. `docs/08_reference.md` — 固定参数 + FX + edge cases（按需查表）

> **docs/*.md（框架 lens，必读） vs docs/normalize_eps.py（工具，直接调）**：工具出问题再看源码。
> 写完 output_5 + output_e 后，**过一遍 `docs/07_checklist.md` 逐项打勾**，任一项 ✗ = 未完成。

## 硬规则（不读 doc 也不能违反）

- **FCF − SBC < 0 → ×0.40**，不否决、总是估值（§3.2 唯一硬规则）
- **折扣只乘在入场价（满仓）层，不进合理价**（§6.1 Step 3）
- **合理价口径**：回购>SBC → EPS 模型；回购≤SBC → DCF ⑦；CapEx/OCF>30% → EPS（§5.3 机械规则）
- **DCF 方法**：g≤3% 一阶段 Gordon；g>3% 两阶段（N=5, g_terminal=3%）；r = 伟大 9%/好公司 10%/平庸 11%（§5.1）
- **分位门 P/E + P/S 都 ≤30%** 才算便宜；derating_flag=True → 分位标"不可信"；查不到则暂停，严禁估算（§4.2/4.3）
- **正常化 EPS = min(GAAP, 工具, v3.1)**，只剔收益不加回亏损；EPS 负值时用恢复 EPS（§1.3）
- **麻烦判定 = 分析日状态**：离职旧闻 ≠ 当前（C-suite 已重建 → borderline，非 fail）（§3.1 #8）
- **g 必须跑完全部 8 源（含 web #7+#8）**，未搜 = 未完成（§2.2）
- **回购不进 g**，g 用 Revenue/NI 增长；EPS CAGR 只作背离信号（§2.1）
- **FCF yield 是估值指标** → 在 Task 4 粗筛 #5（§4.1）
- **1/2/3/5 严格无 price**（安全边际只在 E；Task 5 只产合理价+范围+置信度，不做决策）
- **汇总/校验读所有 output_e**
- **盲评/盲测 {TICKER} → 先读 `prompts/gut_check.md`**（owner，勿自造协议 — NFLX/0700 两轮教训）：新数据（portfolio + CSV + EOD + 近 2 周新闻）+ **不读 docs/ai_report**（防锚定）；gut 先于 docs 预检锁定

## web 数据抓取（Task 4 分位 / Task 3 消息面）

- **优先用 playwright 浏览器**（navigate + evaluate）抓 web 数据
- **`webfetch` 易被反爬**：MacroTrends / GuruFocus / stockanalysis / Simply Wall St / Yahoo Finance 子页 常返 Cloudflare 403
- playwright 首次导航遇 Cloudflare 挑战页 → **等 5 秒再读**，真浏览器能过
- **拿不到则标"暂停"**（严禁估算），绝不编造、绝不用旧值冒充
- 分位常用源：MacroTrends P/E (`/pe-ratio`)，季度历史表用 evaluate 提取，公式 `(current−low)/(high−low)`；GAAP 与正常化 P/E 共用同一 5yr 范围
- Fisher 15 负面搜索必带 follow-up 层（who replaced / forced or voluntary / 何时生效）

## 分析报告

- 产出：`ai_report/{STOCK}/output_1.md ~ output_5.md + output_e.md`
- **output 结构 = 对应 task doc 节序**（§0.5 全局约定），不另设模板
- 盲评产出：`ai_report/{STOCK}/gut_check.md`（框架分析**前**锁定：头部标协议 + 时间戳 + 字节验证，防 write 静默丢失）
- 盲评对账：框架全链路完成后，output_e 末尾落**对账附录**——三列表（维度/盲评/框架 v2/对账：结论方向、隐含公允价、触发器、最脆弱假设、gut 抓框架钝感、框架抓 gut 盲区、归类词）+ 对账头条（最有趣的发现一段）
- 跨案例收敛模式（持续积累）：SE 符号相反 / BILI 时间轴分歧 / NFLX 全收敛（中间带）/ 0700 双误差抵消（知识断层成本）
- 汇总/校验工具：v1 gen_comparison 已退役；v2 汇总器待建（读全量 output_e）

## 代码风格

- 不用列表推导式 — 用显式 for 循环 + append
- 紧凑作用域用短变量名（sr/su/sf）
- 不写过长单行表达式 — 拆多行
- 极少注释，仅在 WHY 不明显时写
