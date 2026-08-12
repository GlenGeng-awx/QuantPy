# DIS — Task D：估值锚
> 更新: 2026-08-07

## D.1 三要素

### 正常化 EPS（from Task B）

| 口径 | EPS (USD) | 来源 |
|------|----------|------|
| GAAP (TTM CSV, Jun 2026) | **$4.85** | TTM Diluted EPS（不含 Q2'25 tax benefit；= MacroTrends $4.84 ✓） |
| 工具 | $5.45 | Normalized Income $9.70B / 1.78B（剥离 Unusual −$1.52B） |
| v3.1 | −$0.66 | **排除**（GMDrop 假阳性：TTM CSV COGS 数据错误 → GM 21.1% vs hist 35.6% → v3.1 过度剥离 $14.4B） |
| **FINAL** | **$4.85** | **min(GAAP, tool) = $4.85**（v3.1 排除） |

> ⚠ **v3.1 排除原因**：TTM CSV COGS $78B 异常偏高（quarterly sum $61B，差 $16.87B）→ TTM GM 21.1% 失真（实际 ~37%）→ GMDrop detector 剥离 $14.4B "excess gross profit" → v3.1 NI = −$1.17B → EPS −$0.66。**假阳性，排除**。
>
> ⚠ **旧 output 用 v3.1 $5.60**（当时 TTM CSV 未损坏）→ 现 v3.1 = −$0.66（TTM CSV COGS 错误）。FINAL 降至 $4.85。
>
> ⚠ **info.json trailingEps $6.25** vs FINAL $4.85：差异因 TTM 时点（info = Mar 2026 含 Q2'25 tax benefit $2.73B；FINAL = Jun 2026 不含）。FINAL $4.85 更"干净"。

### 前瞻 g（from Task C）

g = 7%（G-3: 营收 CAGR 4.5% + Q YoY 6.5% + PEG 7.1% 均值 6.0% → Step 5 +1% streaming 盈利拐点）

### 合理 PE

```
合理 PE = min(8.5 + 7, 30) = min(15.5, 30) = 15.5x
```

### 折扣系数（from B 质量地板 + C 护城河/麻烦）

质量评分:

| 指标 | 值 | ✓/✗ |
|------|-----|-----|
| GM >60% 稳 | ~37%（稳定但非 60%+） | ✗ |
| NM >20% | 8.7% | ✗ |
| FCF−SBC >0 | +$6.77B | ✓ |
| 真缩股 | 1.83B→1.77B 3yr −3.3% | ✓ |
| ROIC >15% 或 ROE >15% | ROIC 7.2% / ROE 11.0% | ✗ |
| 护城河宽 | 中-宽（IP + parks + streaming） | ✓ |

→ 3/6 = **好公司**

麻烦定性: **一般**（streaming 盈利拐点确认 + parks 复苏 = 正面；但 linear 衰退 + CapEx 重 + Iger 继任 overhang = 持续压力。非一次性困境，也非结构性恶化）

→ 折扣系数 = **×0.67**（好公司 × 一般）

## D.2 合理价 + 满仓目标（估值锚, 低频）

```
合理价 = 正常化 EPS $4.85 × 合理 PE 15.5x = $75.18
满仓目标 = $75.18 × 0.67 = $50.37
锚定: EPS=$4.85, g=7%, PE=15.5x, 系数=×0.67, 日期: 2026-08-07
```

> D 不含现价/满仓目标/操作建议——汇总时 join A(price) + D(锚) 算。

## D.2b DCF 交叉验

> 与 D.2 EPS 模型并列。详见 `docs/dcf.md`。

```
r = 10% (好公司)
g = 7% (from Task C)
P/FCF0 = min((1+7%)/(10%-7%), 30) = 30x
net_cash/sh = $-23.43
EPS (FINAL from D.1) = $4.85
```

EPS 模型合理价 = $4.85 x 15.5 = **$75.17**

| 口径 | base ($/sh) | P/FCF0 | DCF/sh | vs EPS 合理价 |
|------|-------------|--------|--------|---------------|
| DCF FCF-SBC | $3.81 | 30x | $90.8 | 21% |
| DCF FCF | $4.66 | 30x | $116.4 | 55% |

回购 $6730M > SBC -> FCF 为主口径

gap 分析:
- gap 1 (EPS->FCF-SBC): $15.6 -> PE 公式差异
- gap 2 (FCF-SBC->FCF): $25.6 -> SBC 差异 ($0.85/sh x 30 = $25.6)

**DCF 揭示低估**: EPS $75.2 < DCF FCF-SBC $90.8 < DCF FCF $116.4
## D.3 敏感性表（正常化 EPS × g 双维）

| 口径 | 正常化 EPS | g | 合理 PE | 合理价 | 满仓目标（×0.67） |
| ------ | ---------- | --- | --------- | -------- | ------------------- |
| 熊（linear 加速衰退 + streaming 竞争） | $4.00 | 5% | 13.5x | $54.00 | $36.18 |
| **基准（TTM Jun 2026）** | **$4.85** | **7%** | **15.5x** | **$75.18** | **$50.37** |
| 牛（streaming 持续盈利 + parks 定价） | $5.45（tool） | 8% | 16.5x | $89.93 | $60.25 |

>

## D.4 护栏检查

- [✓] 回购不进 g: g=7% 用业务增长 + streaming 拐点
- [✓] **g 质量: FCF − SBC = +$6.77B > 0**（不触发 ×0.40）
- [✓] g = 7% < 22% → 不封顶
- [✓] 正常化 EPS = min(GAAP $4.85, tool $5.45) = $4.85（v3.1 排除，假阳性）
- [✓] 折扣只在满仓层（×0.67 不进合理价）
- [✓] 三重保守: EPS min + g 保守（7% < PEG 7.1%）+ 折扣保守（×0.67）

## D.5 质量判定（决定折扣系数）

```
质量判定：好公司（GM ~37% ✗、NM 8.7% ✗、
FCF−SBC +$6.77B ✓、真缩股 ✓、ROIC 7.2% ✗、护城河中-宽 ✓ = 3/6）
× 麻烦 一般（streaming 拐点 + parks 复苏 vs linear 衰退 + CapEx 重 + Iger overhang）
→ 折扣系数 ×0.67 → 满仓目标 $50.37
```

> 好价格判定、归类、操作建议不在 D 里——汇总时 join A(price) + D(锚) 算。
