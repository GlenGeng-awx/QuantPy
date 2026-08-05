# Task D：估值汇聚

> 被引用自 `analysis_framework.md`。Task D = 估值（汇聚 A+B+C → 合理价 → 安全边际 → 定档）。
> 依赖：A（现价）+ B（正常化 EPS + 质量地板）+ C（g + 护城河 + 麻烦定性）。

## 目标

汇聚 A+B+C 的输出，算出合理价、安全边际、满仓目标、仓位定档。

---

## 核心公式

```
合理价   = 正常化 EPS × min(8.5 + g, 30)
满仓目标 = 合理价 × 折扣系数
安全边际 = 1 − 现价 / 合理价
```

> 估值三要素关系见 `analysis_framework.md`。各要素的 checklist 详见 `normalize_eps.md` / `forward_g.md` / `discount_coefficient.md`。

---

## D.1 计算链条

### D.1a 确定正常化 EPS（来自 Task B）

```
EPS = min(GAAP EPS, 工具 EPS, v3.1 EPS)

EPS 负值时 → 用恢复 EPS（详见 normalize_eps.md EPS-4b）
```

### D.1b 确定前瞻 g（来自 Task C）

```
g = 剔除不可靠源 + 剔最高 + 均值（详见 forward_g.md G-3）

合理 PE = min(8.5 + g, 30)
```

### D.1c 算合理价

```
合理价 = EPS × 合理 PE
```

### D.1d 确定折扣系数（来自 B 质量地板 + C 护城河/麻烦）

```
质量评分 = B 的 6 项本地指标 + C 的护城河确认 = 0-7 分
麻烦定性 = C 的 6 项检查 = 四档之一

折扣系数 = 查表（质量 × 雇烦 → 系数）

详见 discount_coefficient.md
```

### D.1e 算满仓目标 + 安全边际

```
满仓目标 = 合理价 × 折扣系数
安全边际 = 1 − 现价 / 合理价     （vs 合理价）
安全边际₂ = 1 − 现价 / 满仓目标  （vs 满仓目标）
```

---

## D.2 ~ D.5 估值锚产出

> D 只产出 price-independent 的锚：合理价、满仓、折扣系数。
> 安全边际、好价格判定、归类、操作建议 = join A(price) + D(锚) → 汇总时算。

### D.2 敏感性表

每只给出 EPS × g 双维敏感性：

```
| 前瞻 g | 合理 PE | 合理价 | 满仓目标（×系数） |
|--------|---------|--------|-----------------|
| 熊口径 | 8.5x | $XX | $XX |
| 基准 | XXx | $XX | $XX |
| 牛口径 | XXx | $XX | $XX |
```

### D.3 护栏检查

```
✓ 回购不进 g: g 用业务/净利润增长，不含缩股驱动的 EPS 增长          ← forward_g.md
✓ g 质量: FCF − SBC < 0 → 重麻烦 ×0.40（不否决，总是估值）           ← discount_coefficient.md
✓ 高增长封顶: g ≥ 22% → PE 一律 30x，不追高                          ← forward_g.md
✓ 利润被麻烦压低型: 用恢复后正常 margin EPS                            ← 本节
✓ 亏损股: EPS 负值时用恢复 EPS（剥一次性后），合理价照算              ← normalize_eps.md EPS-4b
✓ 三重保守: EPS min/恢复 + g 保守 + 折扣保守                          ← analysis_framework.md
```

### D.4 质量判定（决定折扣系数）

```
质量判定：[伟大 / 好公司 / 平庸]（GM __%、NM __%、
FCF−SBC 正负、护城河__、缩股/稀释__）× 麻烦[明确一次性 / 一般 / 存疑 / 重]
→ 折扣系数 ×0.__ → 满仓目标 $__
```

> 好价格判定、归类、操作建议不在 D 里——汇总时 join A(price) + D(锚) 算。

---

## 输出格式

详见 `output_format.md`（per-stock output_d.md 模板 + 汇总格式）。

---

## 与其他 Task 的关系

D 是唯一汇聚点，等 A+B+C 全部完成后计算。依赖关系详见 `analysis_framework.md`。
