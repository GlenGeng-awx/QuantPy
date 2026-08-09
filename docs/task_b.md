# Task B：财务健康 + 正常化 EPS

> 被引用自 `analysis_framework.md`。Task B = 财务（SCORECARD + 正常化 EPS）。
> 数据源：`financial_data/` 下全部 CSV（本地，免费，财报后更新）。

## 目标

判断"这是不是一家好公司" + 算出"干净的盈利 EPS"。

---

## B.1 SCORECARD 九宫格

### 结构

| 维度 | 3yr | TTM | 5Q | 权重 |
|------|------|-----|-----|------|
| Income | 100 | 100 | 100 | 25% |
| CF | 100 | 100 | 100 | 35% |
| BS | 100 | 100 | 100 | 40% |

### 背离检验（核心方法）

SCORECARD 是**报案人不是评委**。机械信号 vs 原始财报的 gap = 错杀/陷阱藏身处：

| 机械信号 | 原始财报 | 背离方向 |
|---------|---------|---------|
| 丑（低分） | 健康（一次性/情绪扣分误伤） | **错杀 = 机会** |
| 漂亮（高分） | 恶化（一次性收益垫高/周期顶） | **陷阱 = 危险** |
| 同向 | 已正确定价 | alpha 少 |

### 伤口模式

3yr 高分 + TTM/5Q 低分 = 困境反转候选。
但须区分：
- **情绪伤口**（基本面完好、市场恐慌）→ 机会
- **结构性伤口**（真实竞争侵蚀）→ 陷阱

### 工具

```bash
python3 -m fundamental.health STOCK    # 自动跑九宫格
```

完整检查项列表详见 `local_data_tools.md` 的 health 章节。

---

## B.2 财报 Heuristic（基于原始 CSV）

### 利润表逐季拆解

```
文件: income_quarterly.csv  列0=最新季（新→旧）

列近 5 季: Revenue / GM% / OpM% / Tax% / NM% / dilEPS / dilShares

看什么:
  - GM 连续下滑 → 定价权/成本恶化
  - SGA/R&D 突跳 → 收购或战略投入
  - 税率异常扭曲 EPS → 需正常化
  - OpInc vs NI 背离 → 非经营项主导利润
```

### 利润增长质量（降本 vs 增长）

```
OpInc 倍数暴涨但营收停滞 → 桥接拆解:
  增量来自"营收增长"还是"砍费用"？
  砍费用 = 一次性台阶（砍到位即止）
  营收增长 = 可持续斜率
  "拧毛巾 vs 接新水"
```

### GAAP 异常正常化

```
OpInc 与 NI 背离 → 非经营项主导
识别一次性项（重组/减值/诉讼/处置）→ 算正常化 EPS
Other Income 大额波动 → 投资损益或 FX
```

### 现金流

```
文件: cf_ttm.csv

| 项目 | key | 看 |
|------|-----|-----|
| OCF | `Operating Cash Flow` | OCF/NI >1 = 利润含金量高 |
| FCF | `Free Cash Flow` | yield 见 A（FCF/MCap，随 price 变） |
| SBC | `Stock Based Compensation` | FCF−SBC 真实现金创造 |
| 回购 | `Repurchase Of Capital Stock` | 真 缩股 vs 仅对冲 SBC |
| CapEx | `Capital Expenditure` | 急增可能吞噬 FCF |
```

> ⚠ **SBC 字段缺失 = 非科技公司**（WMT/MCD/KO/PG 等现金薪酬为主）：cf_ttm 无 `Stock Based Compensation` 行或值为 $0 → SBC=$0 → FCF−SBC = FCF。health scorecard 显示 "SBC/Rev Trend: Insufficient data" 时别卡住，直接标 "SBC=$0（非科技）"，FCF−SBC 检查仍 ✓（= FCF > 0 即可）。

**⚠ FCF 质量必查**：现金充裕时查来源（留存收益 > 发股 > 发债 > 浮存）。
负营运资本浮存（应付膨胀）随销量反向回流、非永久，作锚要打折。

### 资产负债表

```
文件: bs_quarterly.csv  (BS 无 TTM — snapshot 口径)

| 项目 | key | 看 |
|------|-----|-----|
| 净现金/债 | `Cash Cash Equivalents And Short Term Investments` − `Total Debt` | 净债 → 无托底 |
| D/E | `Total Debt` / `Stockholders Equity` | 银行本质高杠杆，非经营恶化 |
| **利息覆盖** | `Operating Income` / `Interest Expense` (income_ttm) | **>5x pass / 2-5x ⚠ / ≤2x fail（代码 health/income.py）** |
| Goodwill | `Goodwill And Other Intangible Assets` | 跳升 = 收购，查标的 |
| 权益 | `Stockholders Equity` | 负权益 = 长期回购超净利 |
```

---

## B.3 正常化 EPS

详见 **`normalize_eps.md`**（v3.1 checklist，含 8 个 detector + 已知问题 + 恢复 EPS）。

```
正常化 EPS = min(GAAP EPS, 工具 EPS, v3.1 EPS)
EPS 负值时 → 用恢复 EPS（详见 normalize_eps.md EPS-4b）
```

实装：`python3 docs/normalize_eps.py {STOCK}`

---

## B.4 质量预判（给 Task D 的地板）

B 完成后可给 D 一个**质量地板**（不含护城河，等 C 确认后可升级）：

```
GM > 60% 稳 + FCF 强 + 真缩股 → 至少"好公司 ×0.67"
GM 薄 + FCF 弱 → "平庸 ×0.60"
中间 → 待 C 确认护城河
```

详见 `discount_coefficient.md` 的质量评分部分。

---

## 与其他 Task 的关系

| 输入 | 来源 |
|------|------|
| 全部 financial_data CSV | `fundamental.download`（财报后更新） |

| 输出 | 去向 |
|------|------|
| 九宫格分数 + 背离检验 | Task D（好公司判断） |
| **正常化 EPS** | Task D（合理价 = EPS × PE；满仓目标 = 合理价 × 折扣） |
| **FCF 金额** | Task A（A 算 FCF yield = FCF/MCap） |
| 质量地板（GM/FCF/缩股） | Task D（折扣系数预判） |
| GM/OpInc CAGR | Task C（g 计算的基线） |

B 完全独立（只需本地 CSV），price 无关，可与 A、C 并行。
