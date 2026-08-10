# DCF 交叉验 Checklist v1.0

> 被引用自 `docs/task_d.md`。DCF 是内在价值的理论定义，作为 EPS × PE 模型的交叉验。
> 与 `normalize_eps.md` / `forward_g.md` / `discount_coefficient.md` 并列，是第四个要素 checklist。

## 原理

**DCF 是内在价值的定义。** 企业的价值 = 未来自由现金流的折现总和。

```
内在价值 = Σ (FCF_n / (1+r)^n)  +  Terminal Value / (1+r)^n
```

EPS × PE 模型（框架核心公式 `合理价 = EPS × min(8.5+g, 30)`）是 DCF 的简化快捷版。两者在 FCF ≈ NI 时一致，但在以下情况严重背离：

| 情况 | FCF vs NI | EPS 模型 | DCF | 偏差方向 |
|------|----------|---------|-----|---------|
| 高 SBC + 低 CapEx（TTD/CRM） | FCF >> NI | 低估 | 高 | EPS 模型过于保守 |
| 高 CapEx（GOOG/NVDA） | FCF << NI | 高估 | 低 | EPS 模型过于乐观 |
| 亏损但现金流正（COIN/BNTX） | FCF > 0, NI < 0 | 需恢复 EPS | 直接估值 | DCF 更精确 |
| 成熟稳定（AAPL/KO） | FCF ≈ NI | 一致 | 一致 | 无偏差 |

**结论：EPS 模型不是均匀保守的。** 对高 SBC 公司低估，对高 CapEx 公司高估。DCF 交叉验可修正这两个方向的偏差。

---

## 公式（Gordon 单阶段）

```
DCF per share = base × (1 + g) / (r − g)  +  net_cash / shares
```

| 参数 | 含义 | 来源 |
|------|------|------|
| **base** | FCF/sh 或 (FCF−SBC)/sh | Task B（cf_ttm.csv） |
| **g** | 前瞻可持续增速 | Task C（forward_g.md G-3） |
| **r** | 质量调整折现率 | 本文档 DCF-3 |
| **net_cash** | Cash + ST Inv − Total Debt | Task B（bs_quarterly） |
| **shares** | 稀释股数 | Task B（income_ttm.csv） |

> Gordon 单阶段：`P/FCF₀ = (1+g)/(r−g)`（trailing，base = 当前 TTM FCF），与 EPS 模型的 `P/E = 8.5+g`（同样 trailing，base = TTM EPS）同构。
> 注：`1/(r−g)` 是 forward PE（P/FCF₁，用明年 FCF）。我们用 TTM FCF 作 base，所以乘数是 (1+g)/(r−g)。
> 选单阶段而非两阶段的原因：简单、只需 g 一个假设（Task C 已产出）、terminal value 不单独引入额外假设。代价是 g ≥ r 时需封顶（见 DCF-4）。

---

## DCF-1: 确定基础 FCF（from Task B）

### 两种口径并列

```
口径 A: FCF/sh       = cf_ttm['Free Cash Flow'] / income_ttm['Diluted Average Shares']
口径 B: (FCF−SBC)/sh = (cf_ttm['Free Cash Flow'] − cf_ttm['Stock Based Compensation']) / shares
```

| 口径 | 含义 | 适用条件 |
|------|------|---------|
| **FCF/sh** | 自由现金流（SBC 未扣） | 回购 > SBC → 净缩股 → SBC 已被回购对冲，不是真成本 |
| **(FCF−SBC)/sh** | Buffett owner earnings | 回购 < SBC → 净稀释 → SBC 是真成本；或无法确认时取保守 |

### 何时用哪个

```
回购 = cf_ttm['Repurchase Of Capital Stock']（CSV 存负数，取绝对值）
SBC  = cf_ttm['Stock Based Compensation']

if |回购| > SBC → 净缩股 → 两种口径都展示，FCF 是主口径
if |回购| ≤ SBC → 净稀释/无回购 → FCF−SBC 是主口径
if 回购 = 0 → FCF−SBC
```

> ⚠ FCF−SBC ≈ NI 是常态（FCF = NI + D&A + SBC + ΔWC − CapEx，减 SBC 后 ≈ NI + D&A + ΔWC − CapEx ≈ owner earnings）。
> 当 FCF−SBC ≈ NI 时，DCF FCF−SBC 与 EPS 模型的差异仅来自 PE 公式（8.5+g vs (1+g)/(r−g)）。

---

## DCF-2: 确定前瞻 g（from Task C）

```
g = forward_g.md G-3 产出（剔高 + 均值 + 定性调整）
```

> g 已经过保守处理（剔最高源 + 不外推 hypergrowth），DCF 不再额外保守。
> 与 EPS 模型共用同一个 g → 两个模型的差异完全来自 base（FCF vs EPS）和 PE 公式（(1+g)/(r−g) vs 8.5+g）。

---

## DCF-3: 质量调整折现率 r

```
r = 基准 + 质量调整

伟大 (5-6/6)   → r = 9%     (低风险，折现率低，估值高)
好公司 (3-4/6) → r = 10%    (标准)
平庸 (0-2/6)  → r = 11%     (高风险，折现率高，估值低)
```

### 为什么质量调整

| 质量 | FCF 确定性 | r | 理由 |
|------|----------|---|------|
| 伟大 | 高（护城河宽 + GM 稳 + FCF 强） | 9% | FCF 更可持续 → 低折现 |
| 好公司 | 中（有裂痕但 FCF 正） | 10% | 标准折现 |
| 平庸 | 低（GM 薄/FCF 弱/护城河窄） | 11% | FCF 不确定性高 → 高折现 |

> 质量评分来自 `discount_coefficient.md` D-1（B 的 5 项 + C 的护城河 = 0-6 分）。
> r 与折扣系数共享同一个质量评分 → 框架自洽。

### r 与框架 PE 的隐含关系

两者都是 trailing PE（base = TTM），可直接比较：

```
框架 PE  = 8.5 + g               (base = TTM EPS)
Gordon PE = (1+g) / (r − g)      (base = TTM FCF)

设两者相等 → 8.5+g = (1+g)/(r_framework − g)
→ r_framework = (1+g)/(8.5+g) + g
```

| g | 框架 PE | Gordon PE (r=10%) | 框架隐含 r | Gordon vs 框架 |
|---|---------|-------------------|-----------|---------------|
| 0% | 8.5x | 10.0x | 11.8% | +18% |
| 3% | 11.5x | 14.7x | 12.0% | +28% |
| 5% | 13.5x | 21.0x | 12.8% | +56% |
| 7% | 15.5x | 35.7x → 封顶 30x | 14.6% | +94% |
| 8% | 16.5x | 54.0x → 封顶 30x | 14.6% | +82% |

> 框架 PE (8.5+g) 隐含 r ≈ 12-15%，比 DCF 的 r=10% 保守 20-50%。
> g 越高，框架越保守 → DCF 对高增长公司的修正越大。

---

## DCF-4: g ≥ r 封顶

Gordon 模型 g ≥ r 时分母 ≤ 0 → 公式失效。即使 g < r 但接近 r，乘数 (1+g)/(r−g) 爆炸性增长。

### 封顶规则

```
P/FCF₀ = min((1+g)/(r−g), 30)

即：
if (1+g)/(r−g) ≤ 30:
  P/FCF₀ = (1+g)/(r−g)    ← Gordon 公式（trailing）
else:
  P/FCF₀ = 30              ← 封顶 30x
```

### 封顶触发点

设 (1+g)/(r−g) = 30 → g = (30r − 1) / 31

| 质量 | r | 封顶触发 g | 含义 |
|------|---|-----------|------|
| 伟大 | 9% | g ≥ 5.5% | 高增长伟大公司封顶 |
| 好公司 | 10% | g ≥ 6.5% | 高增长好公司封顶 |
| 平庸 | 11% | g ≥ 7.4% | 高增长平庸公司封顶 |

> 封顶 30x 与 EPS 模型的 `min(8.5+g, 30)` 一致 → 两模型在高增长时 P/FCF₀ 和 P/EPS₀ 均封顶 30x。
> 区别：DCF 用 FCF/sh，EPS 模型用 EPS。当 FCF/sh > EPS（高 SBC 公司）时，DCF 封顶后仍高于 EPS 模型封顶。

---

## DCF-5: 计算

```
# 质量评分 → r
r = 伟大 9% / 好公司 10% / 平庸 11%

# 封顶（trailing 乘数）
P_FCF = min((1 + g) / (r − g), 30)

# 两种口径
DCF_FCF      = FCF/sh      × P_FCF + net_cash / shares
DCF_FCF-SBC  = (FCF-SBC)/sh × P_FCF + net_cash / shares

# 净现金
net_cash = bs_quarterly['Cash Cash Equivalents And Short Term Investments'] − bs_quarterly['Total Debt']
```

### 边界情况

| 情况 | 处理 |
|------|------|
| FCF < 0（亏损现金流） | DCF N/A → 用 P/B 或恢复 EPS |
| FCF−SBC < 0 | DCF FCF−SBC N/A → 仅展示 DCF FCF，标注 FCF−SBC < 0 |
| 银行（BAC/GS/JPM/MS） | FCF 不适用（贷款流动扭曲）→ P/B 估值，DCF N/A |
| g = 0% | P/FCF₀ = 1/r = 10x（好公司）→ DCF = FCF/sh × 10 + nc/sh |
| g < 0 | 封底 g = 0% |

---

## DCF-6: 三口径体系

```
EPS 模型 (保守下限)  ≤  DCF FCF−SBC (中性)  ≤  DCF FCF (乐观上限)

合理价区间 = [EPS model, DCF FCF−SBC, DCF FCF]
```

| 口径 | 公式 | 含义 | 保守程度 |
|------|------|------|---------|
| EPS 模型 | EPS × min(8.5+g, 30) | 会计利润 × 框架 PE（隐含 r≈12-16%） | 最保守 |
| DCF FCF−SBC | (FCF−SBC)/sh × P_FCF + nc/sh | Buffett owner earnings × Gordon PE（r=9-11%） | 中性 |
| DCF FCF | FCF/sh × P_FCF + nc/sh | 自由现金流 × Gordon PE（SBC 由回购对冲时） | 乐观 |

### 三个 gap 的来源

```
gap 1: EPS 模型 → DCF FCF−SBC
  = PE 公式差异 (8.5+g vs (1+g)/(r−g)) + (FCF−SBC vs NI 的非 SBC 差异如 D&A/CapEx/ΔWC)
  通常小（FCF−SBC ≈ NI）→ gap 主要来自 PE 公式

gap 2: DCF FCF−SBC → DCF FCF
  = SBC 的口径差异
  FCF/sh − (FCF−SBC)/sh = SBC/sh
  gap 大 = SBC 高 → 需判断 SBC 是否被回购对冲

gap 3: EPS 模型 → DCF FCF
  = gap 1 + gap 2 = PE 差异 + SBC 差异
  对高 SBC + 低 CapEx 公司（TTD/CRM）最大
```

### 何时 DCF 改变结论

| 场景 | EPS 模型说 | DCF 说 | 行动 |
|------|----------|--------|------|
| 高 SBC + 回购>SBC + 低估 | 买贵了 | FCF 口径便宜 | **重新审视**——EPS 被 SBC 压低，DCF FCF 更准确 |
| 高 CapEx + 高估 | 接近合理价 | FCF 口径贵 | **重新审视**——EPS 虚高，DCF FCF 揭示真实成本 |
| FCF ≈ NI | 一致 | 一致 | 无需调整 |
| FCF<0 | N/A | N/A | 两模型都失效，用 P/B |

---

## 实际例子

### TTD（高 SBC + 回购>SBC → DCF >> EPS）

```
参数: FCF $848M, FCF-SBC $396M, SBC $452M, 回购 $974M, shares 480.6M
      g=3%, r=10% (好公司), net_cash $1,060M
      (1+g)/(r−g) = 1.03/0.07 = 14.7x < 30 → 用 Gordon, P/FCF₀ = 14.7x

DCF FCF     = ($848M/480.6M) × 14.7 + $1,060M/480.6M
             = $1.765 × 14.7 + $2.205
             = $26.0 + $2.2 = $28.2

DCF FCF-SBC = ($396M/480.6M) × 14.7 + $2.205
             = $0.824 × 14.7 + $2.205
             = $12.1 + $2.2 = $14.3

EPS 模型    = $0.84 × 11.5 = $9.66

三口径: $9.66 (EPS) < $14.3 (DCF FCF-SBC) < $28.2 (DCF FCF)
现价:   $13.80

gap 1 (EPS→FCF-SBC): $14.3 − $9.66 = $4.6  → PE 公式差异 (11.5x vs 14.7x)
gap 2 (FCF-SBC→FCF): $28.2 − $14.3 = $13.9 → SBC 差异 ($0.94/sh × 14.7 = $13.9)
gap 3 (EPS→FCF):    $28.2 − $9.66 = $18.5  → PE + SBC 叠加

判断: 回购 $974M > SBC $452M → 净缩股 → FCF 是正确口径
     DCF FCF $28.2 → 安全边际 +105% → 便宜!
     DCF FCF-SBC $14.3 → 安全边际 −3.5% → 接近合理价
     EPS 模型 $9.66 → 安全边际 −42.9% → 买贵了
```

### GOOG（高 CapEx → DCF << EPS）

```
参数: FCF/sh $4.35, FCF-SBC/sh $2.05, EPS $19.93 (含投资收益虚高)
      g=15%, r=9% (伟大), net_cash ~$7/share
      (1+g)/(r−g) = 1.15/(-0.06) < 0 → g > r → 封顶 P/FCF₀ = 30x

DCF FCF     = $4.35 × 30 + $7 = $130.5 + $7 = $137.5
DCF FCF-SBC = $2.05 × 30 + $7 = $61.5 + $7 = $68.5
EPS 模型    = $10.03 × min(8.5+15, 30) = $10.03 × 23.5 = $235.71

三口径: $68.5 (DCF FCF-SBC) < $137.5 (DCF FCF) < $235.71 (EPS 模型)
现价:   $360.10

判断: EPS $19.93 含 $148.8B 投资收益虚高; FCF 被 $200B+ capex 压低
     DCF FCF-SBC $68.5 → 安全边际 −426% → 极度买贵了
     EPS 模型 $235.71 → 安全边际 −53% → 买贵了
     DCF 揭示 EPS 模型高估了 GOOG ~2x
```

> ⚠ GOOG 的 DCF FCF 可能过度保守（capex 含增长投资，非纯维护）。实际 owner earnings 介于 FCF 和 FCF+SBC 之间。但方向正确：EPS 模型对高 CapEx 公司高估。

---

## 在框架中的位置

```
Task D 估值锚:
  D.1 EPS × PE (保守下限)           ← 现有，不变
  D.2 DCF FCF-SBC (中性基准)         ← 新增交叉验
  D.3 DCF FCF (乐观上限, 回购>SBC时) ← 新增交叉验
  D.4 敏感性表 (EPS × g 双维)        ← 现有
  D.5 质量判定 + 折扣系数             ← 现有
```

### 与 EPS 模型的关系

- **EPS 模型不被替代**——它是保守下限，体现"哪怕错过不做错"
- **DCF 是交叉验**——揭示 EPS 模型的偏差方向和幅度
- **当 DCF 与 EPS 模型一致**（FCF ≈ NI）→ 结论稳健，无需调整
- **当 DCF >> EPS**（高 SBC + 回购>SBC）→ EPS 模型低估，DCF FCF 更准确
- **当 DCF << EPS**（高 CapEx）→ EPS 模型高估，DCF FCF-SBC 更保守
- **满仓目标仍用 EPS 模型**（最保守口径 × 折扣系数），DCF 作为"合理价区间"的上限参考
- **DCF 安全边际 = 1 − A.现价 / D.DCF FCF — 在 Task E 算**（join A price + D anchor），不在 D 里

### output_d.md 新增章节

在 D.2 后增加 D.2b:

```
### D.2b DCF 交叉验

| 口径 | base | P/FCF | DCF/sh | vs 现价 |
|------|------|-------|--------|---------|
| DCF FCF-SBC | $XX | XXx | $XX | ±XX% |
| DCF FCF | $XX | XXx | $XX | ±XX% |

r = X% (伟大/好公司/平庸)
g = X% (from Task C)
封顶: (1+g)/(r−g) {≤/≥} 30 → P/FCF₀ = {(1+g)/(r−g) / 30x}
净缩股/稀释: 回购 $XXM {>/≤} SBC $XXM → {FCF/FCF-SBC} 为主口径

gap 分析:
- gap 1 (EPS→FCF-SBC): $XX → PE 公式差异
- gap 2 (FCF-SBC→FCF): $XX → SBC 差异
- 判断: {DCF 与 EPS 一致 / DCF 揭示低估 / DCF 揭示高估}
```

---

## 与其他 checklist 的关系

| 要素 | checklist | 公式中的角色 |
|------|-----------|-------------|
| 正常化 EPS | normalize_eps.md | EPS 模型的 base |
| 前瞻 g | forward_g.md | 两模型共用 |
| 折扣系数 | discount_coefficient.md | 满仓目标 × 系数 |
| **DCF** | **本文档** | **base = FCF/sh 或 (FCF−SBC)/sh** |

> DCF 不改变现有框架流程，只在 Task D 增加一个交叉验视角。
> 质量评分同时决定 r（DCF 折现率）和折扣系数（满仓目标）→ 两系统共享一个质量判定，自洽。

---

## 实装

```bash
# 自动（推荐）— docs/dcf.py 从 CSV 读取，输出完整 DCF 表 + gap 分析
python3 docs/dcf.py WMT 6 好公司 2.609       # STOCK G(%) QUALITY [EPS]
python3 docs/dcf.py NVDA 15 伟大 10.03      # 高增长封顶 30x 演示
python3 docs/dcf.py TTD 3 好公司 0.84        # 高 SBC 演示（DCF>EPS）

# g 接受 6 / 6% / 0.06 三种写法；QUALITY ∈ {伟大,好公司,平庸}→r{9%,10%,11%}
# EPS 可选（给则算 gap vs EPS 模型；不给只输出 DCF）

# 编程接口（返回 dict）
python3 -c "import sys; sys.path.insert(0,'docs'); from dcf import dcf; print(dcf('WMT',0.06,'好公司',2.609))"
```

> 已实装 `docs/dcf.py`（与 `normalize_eps.py` 同级）。验证：TTD 输出 DCF FCF $28.17 / FCF−SBC $14.33 / EPS $9.66，与本文档"Gordon 公式推导"前的手算例子一致。

### 边界情况（脚本自动处理）

| 情况 | 脚本行为 |
|------|---------|
| FCF < 0 | 输出 "DCF N/A，用 P/B 或恢复 EPS" |
| FCF−SBC < 0 | 标 "重麻烦 ×0.40"，仅展示 DCF FCF |
| g ≥ r | P/FCF 封顶 30x，显示 "∞ (g≥r)" |
| SBC = $0（非科技如 WMT/MCD/KO） | FCF−SBC = FCF，gap 2 = $0，两口径相同 |

---

## 附录：Gordon 公式推导

### 目标

证明：

```
Value = FCF₀ × (1 + g) / (r − g)
```

### 推导

企业价值 = 未来所有 FCF 的折现和，从 t=1（明年）起：

```
Value = Σ_{t=1}^{∞}  FCF₀ × (1+g)^t / (1+r)^t
```

提取 FCF₀，令 **q = (1+g)/(1+r)**：

```
Value = FCF₀ × Σ_{t=1}^{∞}  q^t
```

这是一个**从 t=1 起的等比级数**：

```
Σ_{t=1}^{∞} q^t = q + q² + q³ + ... = q / (1-q)         （|q| < 1，即 g < r）
```

> 注：不是 1/(1-q)。1/(1-q) = 1 + q + q² + ... 是从 t=0 起的级数（含"今天"不折现）。
> 从 t=1 起 = 1/(1-q) − 1 = q/(1-q)，殊途同归。

代入 q：

```
q/(1-q) = [(1+g)/(1+r)] / [1 − (1+g)/(1+r)]
        = [(1+g)/(1+r)] / [(1+r−1−g)/(1+r)]
        = (1+g) / (r−g)
```

因此：

```
Value = FCF₀ × (1+g) / (r−g)
```

### 等价写法

```
方法 A:  Value = FCF₀ × (1+g) / (r−g)     ← base = 当前 TTM FCF
方法 B:  Value = FCF₁ / (r−g)             ← base = 明年 FCF = FCF₀ × (1+g)
```

框架用方法 A（base = TTM FCF from CSV），乘 (1+g) 将当前 FCF 投影到明年再折现。

### 为什么从 t=1 而非 t=0

t=0 = 今天。今天的 FCF 已经在账上（反映在 net_cash 里），不能既算进 net_cash 又算进 DCF。

```
t=0 起: 1/(1-q) = (1+r)/(r−g)  ← 含今天 FCF（不折现），重复计入 net_cash
t=1 起: q/(1-q) = (1+g)/(r−g)  ← 仅未来 FCF，与 net_cash 不重叠 ✓
```

### 与 PE 公式的关系

Gordon 模型给出 `P/FCF = (1+g)/(r−g)`。当 base ≈ EPS（FCF≈NI 时）：

```
P/EPS = (1+g)/(r−g)     ← Gordon 隐含 PE

框架 PE = 8.5 + g        ← 格雷厄姆简化 PE

设两者相等 → 8.5+g = (1+g)/(r−g) → r ≈ 12-15%（依 g 而变）
框架隐含 r 比 DCF 显式 r（9-11%）高 2-5pp → 框架更保守
```
