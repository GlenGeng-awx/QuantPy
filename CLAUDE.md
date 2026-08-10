# 选股分析框架

## 投资哲学

| 哲学家 | 原则 | 对应 Task |
|--------|------|-----------|
| 格雷厄姆 | 好价格（安全边际） | A（粗筛/分位）+ E（安全边际/操作） |
| 费雪 | 好公司（GM/FCF/护城河） | B + C |
| 巴菲特 | 一次性麻烦（暂时困境） | C + D |

三者缺一不可：

| 条件 | 归类 |
|------|------|
| 只有好价格 | 价值陷阱（便宜的烂公司） |
| 只有好公司 | 买贵了 |
| 好公司 + 好价格但麻烦非一次性 | 结构性恶化 |
| 三者齐备 | **最佳买点** |

## 三核心公式

```
# EPS 模型（保守下限）
合理价 = 正常化 EPS × min(8.5 + g, 30)
满仓目标 = 合理价 × 折扣系数

# DCF 交叉验（并列，非替代）
DCF per share = base × (1+g)/(r−g) + net_cash/shares
  base = FCF/sh 或 (FCF−SBC)/sh
  r = 质量调整：伟大 9% / 好公司 10% / 平庸 11%
  P/FCF₀ = min((1+g)/(r−g), 30)  ← g 接近 r 时封顶 30x
```

EPS 模型是保守下限，DCF 是内在价值定义。两者并列展示，当 FCF ≈ NI 时一致，高 SBC / 高 CapEx 时背离。详见 `docs/dcf.md`。

## ABCDE 工作流

| Task | 内容 | 数据源 |
|------|------|--------|
| A | 价格层（daily）— 粗筛 8 项 + 双分位 | 本地 CSV + web + B v3.1 |
| B | 财务健康 + 正常化 EPS | 本地 CSV |
| C | 增长前瞻 + 护城河 + 消息面 | web search |
| D | 估值锚（low-freq）— 合理价 + 满仓 + DCF | B+C 输出 |
| E | 决策（daily）— 安全边际 + 操作 + 归类 | A+D 输出 |

依赖图两条线：B→A→E，B,C→D→E。A 和 D 并行（都只等 B），E 等 A+D。

## 分析预检（每次分析股票 / 汇总 / 校验前必须完成）

⚠️ 收到任何股票分析请求、或"汇总/校验"请求时，先用 read 工具加载以下 `docs/*.md`，全部读完才开始（不论分析一只还是汇总所有标的）：

1. `docs/analysis_framework.md` — 框架全景 + 公式 + FX + 数据源
2. `docs/task_a.md` — 价格粗筛方法
3. `docs/task_b.md` — 财务健康方法
4. `docs/normalize_eps.md` — EPS 检查清单（8 检测器）
5. `docs/task_c.md` — 增长/护城河/管理层/消息面方法
6. `docs/forward_g.md` — g 检查清单（8 源）
7. `docs/task_d.md` — 估值锚方法
8. `docs/task_e.md` — 决策层方法
9. `docs/discount_coefficient.md` — 折扣系数清单（6 分+5 档，含无麻烦列）
10. `docs/dcf.md` — DCF 交叉验（Gordon 单阶段 + 质量调整 r + 封顶）
11. `docs/local_data_tools.md` — 工具用法 + 数据格式速查
12. `docs/output_format.md` — 输出格式 + 存档规则
13. `docs/batches.md` — 查标的所在批次 + 元标记
14. `docs/mistakes.md` — 历史复查发现的常见错误 + 提交前自检清单

全部读完后 context 里有完整方法论 + 已知错误，再开始 ABCDE 分析或汇总校验。

> ⚠️ 写完 `output_d.md` + `output_e.md` 后，**必须过一遍 `docs/mistakes.md` 第九节"提交前自检清单"**，逐项打勾再提交。任一项 ✗ = 未完成。

> **`docs/*.md`（框架文本）vs `docs/*.py`（工具）**：框架 .md 必须读（是分析/汇总/校验的 lens，不论一只还是全部）；工具 .py（normalize_eps / dcf / gen_comparison）直接调用，出问题再看源码。

## 硬规则（不读 doc 也不能违反）

- **FCF − SBC < 0 → 重麻烦 → ×0.40**，不否决、总是估值
- **g ≥ 22% → 合理 PE 封顶 30x**，不追高增长
- **合理价 = 正常化 EPS × min(8.5+g, 30)**，折扣只在满仓目标层，不进合理价
- **DCF 交叉验 = base × (1+g)/(r−g) + net_cash/sh**，与 EPS 模型并列展示，非替代
- **5 年估值分位须 ≤30%**（双分位：GAAP + 正常化 P/E，两个都 ≤30%），查不到则暂停，严禁估算
- **正常化 EPS = min(GAAP, tool, v3.1)**，只剔收益不加回亏损；EPS 负值时用恢复 EPS（剥一次性后估正常化盈利）
- **回购不进 g**，g 用业务/净利润增长
- **FCF yield 是估值指标不是质量指标** → 在 A 粗筛 #5，不在 D 质量评分（6/6）
- **B/C/D 严格无 price**（FCF yield/MCap/安全边际 不进 B/C/D；安全边际在 E）

## web 数据抓取（Task A.2 双分位 / Task C 同业·消息面）

- **优先用 playwright 浏览器**（`playwright_browser_navigate` + `playwright_browser_evaluate`）抓 web 数据
- **`webfetch` 易被反爬**：MacroTrends / GuruFocus / stockanalysis / Simply Wall St / Yahoo Finance 子页 等常返 Cloudflare 403（"Just a moment..."）或 403 Forbidden，webfetch 直拿会失败
- playwright 首次导航若遇 Cloudflare 挑战页，**等 5 秒**（`playwright_browser_wait_for time=5`）再读，真浏览器能过
- **拿不到则按硬规则标"暂停"**（"查不到则暂停，严禁估算"），绝不编造、绝不用旧值冒充
- A.2 双分位常用源：[MacroTrends](https://www.macrotrends.net) P/E (`/pe-ratio`) 或 P/B (`/price-book`) 页，季度历史表用 evaluate 提取，公式 `(current−low)/(high−low)` 算分位。GAAP P/E 和正常化 P/E 共用同一 5yr 范围。

## 分析报告

- 产出文件：`ai_report/{STOCK}/output_a.md` ~ `output_e.md`（ABCDE 五任务分文件）
- 格式规范详见 `docs/output_format.md`

## 每日汇总 + 校验（gen_comparison）

> 触发"汇总/校验"同样按"分析预检"先读全部 `docs/*.md`（框架是 lens，汇总也需在 context），再跑下面命令。

刷完 Task A + E 后跑汇总+校验（一条命令，verify 是汇总前置步骤，自动跑）：

```
python3 docs/gen_comparison.py --date {YYYY-MM-DD}
```

产出（`ai_report/` 下并列两文件）：
- `comparison.{date}.md` — 决策汇总（8 章节：① 决策摘要 ② 买点详情 ③ 三 Top 10（EPS/DCF FCF/回撤信号）④ 隐藏机会 ⑤ 全量主表 ⑥ 特殊档 ⑦ DCF 信号分组 ⑧ 数据质量）
- `verify.{date}.md` — 数据校验日志（Phase 1：5 项 a+d 检查，自动化 `docs/mistakes.md` §9）

verify 规则（Flag 不阻断）：
- 违规标的主表标 `⚠` 仍保留，决策不阻断
- ⚠ 标的需重跑 Task A/D/E 修复源数据，再重跑 gen_comparison 至 verify 归零
- 5 检查：① 安全边际符号（1−现价/合理价 符号）② 满仓=合理价×系数 ③ 合理 PE=min(8.5+g,30) ④ g≥22 封顶（折叠进③）⑤ 伟大+无trouble→×1.0

gen_comparison 只读 `output_e.md`（E 聚合 A 信号 + D 锚 + 计算决策），不重算 join。

## 代码风格

- 不用列表推导式 — 用显式 for 循环 + append
- 紧凑作用域用短变量名（sr/su/sf）
- 不写过长单行表达式 — 拆多行
- 极少注释，仅在 WHY 不明显时写
