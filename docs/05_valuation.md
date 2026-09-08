# Task 5: 估值

> **产出**: 合理价 + 全方法值 + 范围 + 置信度 + gap 诊断 + r + 折扣 + 总结。
> 
> **依赖**: output_1 (EPS/per-share) + output_2 (g 多档位) + output_3 (折扣/r) + output_4 (分位/derating)。
> 
> Task 5 = 纯估值引擎 (算全部方法, 给范围); Task E = 决策者 (选可信 → 入场/出场 → 归类)。
> 
> **output_5.md 结构 = 本文档节序 (§5.1→§5.2→§5.3→§5.4→§5.5); 各 § 节的表格式即 output 格式, 不另设模板。**

## §5.1 参数 + 方法适用性

### 全部参数 (from output_1/2/3/4)

| 参数 | 值 | 来源 |
|------|-----|------|
| EPS (FINAL) | min(GAAP, tool, v3.1) | output_1 |
| FCF/sh | FCF / shares | output_1 |
| FCF-SBC/sh | (FCF - SBC) / shares | output_1 |
| net_cash/sh | (Cash+ST Inv − Total Debt) / shares | output_1 |
| 回购 vs SBC | buyback vs SBC | output_1 |
| CapEx/OCF | CapEx / OCF | output_1 |
| SBC/Rev | SBC / Revenue | output_1 |
| g 多档位 | 熊/基准/牛/调整 | output_2 |
| 质量档 + 麻烦档 | 伟大/好公司/平庸 × 无麻烦/存疑/重麻烦 | output_3 |
| 折扣系数 | ×{val} (2D 表; FCF-SBC<0 → ×0.40) | output_3 |
| r | {%} (伟大 9% / 好公司 10% / 平庸 11%) | output_3 |
| P/E 5yr range + 30th | high / low / 30th | output_4 |
| P/S 5yr range + 30th | high / low / 30th | output_4 |
| P/B 5yr range + 30th | high / low / 30th | output_4 |
| derating_flag | True/False | output_4 |

> Task 5 总是算合理价 (EPS×PE 或 DCF) — 不引用 ×0.40
> ×0.40 是折扣系数, 只在入场价层应用 (Task E: 入场 = 合理价 × 折扣)
> 能否估值 / 价值陷阱判断 = Task E 职责 (读 output_1 EPS/FCF-SBC + output_3 Fisher + output_5 gap/置信度)

### 方法适用性

| # | 方法 | 公式 | 适用? | 理由 |
|---|------|------|-------|------|
| ① | Graham PE | EPS × (8.5 + g) | ✓/✗ | EPS>0 |
| ② | Fisher PE | EPS × (8.5 + 2g) | ✓/✗ | EPS>0 |
| ③ | 中周期 EPS | mid_EPS × (8.5 + g_mid) | ✓/✗ | 周期股 (fallback, §5.4) |
| ④ | P/E 分位反推 | pe_30th × EPS | ✓/⚠/✗ | 5yr, 无 derating |
| ⑤ | P/S 分位反推 | ps_30th × Rev/shares | ✓/⚠/✗ | 5yr, 无 derating |
| ⑥ | P/B 分位反推 | pb_30th × BVPS | ✓/⚠/✗ | 5yr, 资产较重; 轻资产 ✗ |
| ⑦ | DCF FCF-SBC | (见 DCF 公式, §5.1 下方) | ✓/✗ | FCF-SBC>0; 方法 (一阶段/两阶段) |
| ⑧ | DCF FCF | (见 DCF 公式, §5.1 下方) | ✓/✗ | FCF>0; 方法 (一阶段/两阶段) |

> ① vs ②: Graham 8.5+g = 保守档 (入场基准); Fisher 8.5+2g = 乐观档 (出场基准, 对高 g 奖励翻倍)
> ⑦⑧ 公式 = DCF 方法选择 (§5.1 下方一阶段/两阶段代码块, 单一 owner)
> ①② 只要 EPS>0 都算 (不按 g 限制); ⑦⑧ 只要 FCF>0/FCF-SBC>0 都算
> ④⑤⑥ 如 derating_flag=True → 标"⚠ 不可信 (derating)"; 列出但不作合理价/入场/出场
> ⑥ 如 GM>60% 或 CapEx/Rev<5% (轻资产) → ✗ 不适用
> 角色不写死在表里 — 动态由路径决定 (入场/出场配对):
>   EPS 路径 (回购>SBC): ①×折扣=入场, ②=出场, ⑦⑧ 并列参考
>   DCF 路径 (回购≤SBC): ⑦×折扣=入场, ⑧=出场, ①② 并列参考
> g 越高 → ①② gap 越大 → 不确定性越高; SBC 越重 → ⑦⑧ gap 越大 → 同理

### DCF 方法选择 (一阶段 vs 两阶段)

```
if g > 3%:
    两阶段 DCF (N=5 年高增长, 然后 g_terminal=3% 永续)
    base = (FCF-SBC)/sh (⑦) 或 FCF/sh (⑧)
    PV_stage1 = Σ_{t=1}^{5} base × (1+g)^t / (1+r)^t
    TV = base × (1+g)^5 × (1+g_terminal) / (r - g_terminal) / (1+r)^5
    DCF = PV_stage1 + TV + net_cash/sh

elif g ≤ 3%:
    一阶段 DCF (Gordon Growth, g 终值 = g, 不假设加速)
    base = (FCF-SBC)/sh (⑦) 或 FCF/sh (⑧)
    DCF = base × (1+g) / (r - g) + net_cash/sh
    → g=0% 时: DCF = base / r + net_cash/sh (最保守)
```

> g > 3% → 有"高增长期"需单独建模 → 两阶段
> g ≤ 3% → 无"高增长期" (g ≤ GDP, 不假设加速) → 一阶段
> per-scenario: 不同 g 档位可能用不同 DCF 方法

## §5.2 估值矩阵

### EPS 路径 (回购 > SBC)

| 情景 | g | ①Graham | ②Fisher |
|------|---|---------|---------|
| 熊 | ...% | $XX | $XX |
| 基准 | ...% | $XX | $XX |
| 牛 | ...% | $XX | $XX |
| 调整 | ...% | $XX | $XX |

### DCF 路径 (一阶段/两阶段, 方法由 g 决定)

| 情景 | g | ⑦FCF-SBC | ⑧FCF | 方法 |
|------|---|----------|------|------|
| 熊 | ...% | $XX | $XX | 一阶段/两阶段 |
| 基准 | ...% | $XX | $XX | 一阶段/两阶段 |
| 牛 | ...% | $XX | $XX | 一阶段/两阶段 |
| 调整 | ...% | $XX | $XX | 一阶段/两阶段 |

> 方法: g ≤ 3% → 一阶段 (Gordon Growth); g > 3% → 两阶段 (N=5 + g_terminal=3%)
> per-scenario: 不同 g 档位可能用不同方法 (如 调整 g=0% 一阶段, 牛 g=15% 两阶段)
> 角色随路径: EPS 路径 (回购>SBC) 时 ⑦⑧ 并列参考; DCF 路径 (回购≤SBC) 时 ⑦=合理价+入场, ⑧=出场

### DCF debug info (逐年贡献值)

output 格式 (调整 g, 每个 DCF 方法各一张, 列在 DCF 路径表正下方):

```
⑦DCF FCF-SBC (调整 g=0%, r=11%, 方法: 一阶段):
  base = $0.83, g = 0%, r = 11%

  | 年 | CF | PV | 累计 PV |
  |----|-----|-----|---------|
  | 1  | $0.83 | $0.75 | $0.75 |
  | 2  | $0.83 | $0.68 | $1.43 |
  | ... | ... | ... | ... |
  | TV | — | $X.XX | $X.XX |
  | net_cash | — | $2.19 | $X.XX |

  DCF = $X.XX
  方法: 一阶段 (g=0% ≤ 3%)
  TV 占比: NN%
```

> 展示各年 CF + PV + 累计 + TV + net_cash + 方法标注
> TV 占比高 = 终值主导 = 对 g_terminal 假设敏感 (debug 信号)
> 一阶段无逐年表 (Gordon Growth 是永续公式); 仅展示 base/r/g/DCF/TV 占比

### 分位反推 ④⑤⑥ (from output_4)

| # | 方法 | 30th 分位值 | 反推价格 | 可信? |
|---|------|------------|----------|-------|
| ④ | P/E 分位 | ...x | $XX | ✓ 或 ⚠ derating |
| ⑤ | P/S 分位 | ...x | $XX | ✓ 或 ⚠ derating |
| ⑥ | P/B 分位 | ...x | $XX | ✓ 或 ⚠ derating 或 不适用 |

### 合理价 (机械规则)

```
if 回购 > SBC: 合理价 = ① Graham (EPS × (8.5 + g))
elif 回购 ≤ SBC: 合理价 = ⑦ DCF FCF-SBC
if CapEx/OCF > 30%: 合理价 = ① Graham (DCF 被 CapEx 压低)
```

output: 合理价 = **$XX** (调整 g, 机械规则)

### 范围 + 置信度

```
可用方法 = 排除 ⚠ 不可信 (derating/轻资产不适用) 的方法
范围 = [min(可用方法), max(可用方法)]

置信度 (按可用方法 gap):
  gap < 15%: 高
  gap 15-50%: 中
  gap > 50%: 低 (方法分歧大, 见 §5.3 gap 诊断)
  仅 1-2 方法可用: 低
```

> Task 5 = 纯估值引擎: 算全部方法, 给范围 + 置信度 + gap; 不定入场/出场 (Task E 的决策)

## §5.3 gap 诊断

**机制前提 (防"双扣"误判, 单源):**
- SBC 是非现金项 → OCF 已加回 → FCF 不含 SBC → FCF-SBC 只扣 SBC 一次 (和 EPS 一样)
- ②(EPS) 与 ⑦(FCF-SBC) 都只扣 SBC 一次, 二者 gap 不是"SBC 双扣"
- ② vs ⑧(FCF, 不扣 SBC): ⑧ > ② 当 SBC 重 → 这才是"SBC 压低 EPS"
- EPS 模型本身即 CapEx 正常化估值 (D&A 分摊, 不受 CapEx 扭曲)

output — 先放方法汇总表 (快速扫描全部值):

| 方法 | 值 | 角色 |
|------|-----|------|
| ①Graham (EPS) | $XX | 合理价 (EPS 路径) / 并列参考 (DCF 路径) |
| ②Fisher (EPS) | $XX | 出场 (EPS 路径) / 并列参考 |
| ⑦DCF FCF-SBC | $XX | 入场基准 (DCF 路径) / 并列参考 |
| ⑧DCF FCF | $XX | 出场 (DCF 路径) / 并列参考 |
| ④P/E 分位 | $XX | ✓ 或 ⚠ derating |
| ⑤P/S 分位 | $XX | ✓ 或 ⚠ derating |

> 角色按路径动态填 (见 §5.1 配对); ⚠ 方法也列出 (标不可信)

诊断参考表:

| gap 模式 | 原因 | 诊断 | 更可信 |
|----------|------|------|--------|
| 所有方法接近 | FCF≈NI | 高置信 | 都可信 |
| ①② > ⑦⑧ | CapEx (CapEx/OCF>30%) | DCF 低估 | EPS |
| ①② > ⑦⑧ | WC build (应收/存货暴增) | DCF 低估 (暂时) | EPS |
| ② < ⑧ (FCF) | SBC (SBC/Rev>5%) | EPS 扣 SBC, FCF 没扣 | 看回购 vs SBC |
| ② > ⑦ + 回购≤SBC | 稀释未反映 | EPS 不反映稀释 | ⑦ FCF-SBC |
| ①② < ⑦⑧ | v3.1 过度剥离 | EPS 被压低 | DCF 或 GAAP |
| ④⑤⑥ vs ①②⑦⑧ 大 | 分位含旧范式 | derating_flag=True | 排除分位 |
| 周期峰值: ①② >> ③ | EPS 在峰值 | 低 P/E = E 涨快于 P | ③中周期 |
| DCF N/A | FCF 负 | 单口径, 最低置信 | EPS |

output — gap 模式表:

| gap 模式 | 原因 | 诊断 | 更可信 |
|----------|------|------|--------|
| (模式) | (原因) | (诊断) | (方法) |

## §5.4 周期股处理 — 默认标准, 仅明显不合理才 fallback

**默认: 所有标的用标准 Task 5 估值。**

Fallback 触发条件 (满足任一):
```
1. EPS 为负 → PE 无效 → 用恢复 EPS 或 P/B
2. EPS 峰谷差 > 2x AND 波动来自业务周期 (非收购/一次性)
3. P/E < 5yr 10th AND EPS 在历史最高
```

Fallback 方法: ③中周期 EPS, P/B 分位, 净现金/清算价值

> 正例: NVDA — EPS $0.17→$6.53, NM 63% → 触发
> 反例: AVGO — VMware 收购 → 不触发
> 反例: TSM — GM 64%+ 稳 → 不触发

---

## §5.5 总结

| 项 | 内容 |
|----|------|
| 一句话定性 | (合理价 $XX, 范围 [$XX, $XX], 置信度); 合理价口径; flag (Task E §6.1 复判) |
| 合理价 + 范围 | $XX (机械规则); [$XX, $XX] (可用方法, 排除 ⚠); ④⑤⑥ $XX (⚠ 不可信, 仅列); 置信度 (高/中/低) |
| gap 诊断 | (模式 + 诊断 + 更可信口径 + 不可信方法) |
| r + 折扣 | r = {%}; 折扣 = ×{val} |
| Top risk | (置信度低? gap 大? derating? 哪些方法不可信?) |

> Task 5 产出: 合理价 + 全方法值 + 范围 + 置信度 + gap + r + 折扣
> Task E 职责: BS 生存力 → 能否估值/价值陷阱判断 (读 output_1 + output_3 + output_5) → 选可信方法 → 入场/出场 → 比现价 → 归类 → 入场策略
