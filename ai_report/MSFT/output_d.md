# MSFT — Task D：估值汇聚
> 更新: 2026-08-09（修正满仓 N/A → ×1.0；修正 net_cash 误用总负债 → 正确净现金；财报 FY26 Q4/全年，2026-07-29 发）

## D.1 三要素

### 正常化 EPS（from Task B）
| 口径 | EPS | 来源 |
|------|-----|------|
| GAAP | $17.95 | income_annual Diluted EPS（FY26 = TTM，2026-06-30；income_ttm Diluted EPS=nan 用 annual 兜底） |
| 工具 | $17.33 | Normalized Income $129.135B / 7.453B shares |
| v3.1 | $16.20 | norm_ni $120.72B / 7.453B shares（剥 OtherInc $10.447B + Unusual $5.725B，diff 45.2%>20% 判独立） |
| **FINAL** | **$16.20** | **min(三者) = v3.1** |

> ⚠️ income_ttm.csv Diluted EPS + Diluted Average Shares 均为 nan（数据下载问题）。GAAP EPS 取 income_annual col0（FY26）$17.95；shares 7.453B 取 income_annual Diluted Average Shares。v3.1 手工计算（normalize_eps.py 因 TTM 缺 shares 返 $0.00）。
> v3.1 剥 $16.172B pre-tax 中含 OpenAI $7.6B 一次性（正确剥离）+ Gain On Sale $5.9B + 其他投资收益 $2.6B（可能含经常性利息收入 → v3.1 可能过度保守，normalize_eps.md 已知问题 #2）。但 per 框架硬规则 FINAL = min(GAAP, tool, v3.1) = $16.20，**不许取 GAAP 上界**（`mistakes.md` 二: "合理价 EPS 必须 = min，不许取 GAAP 上界"）。

### 前瞻 g（from Task C）
g = 13%（历史 3yr CAGR 10.6-15% 与前瞻共识 13-15% 的保守交集）

### 合理 PE
PE = min(8.5 + 13, 30) = **21.5x**

### 折扣系数（from B 质量地板 + C 护城河/麻烦）

质量评分:

| 指标 | ✓/✗ |
|------|-----|
| GM >60% 稳 | ✓（67.9%, 稳） |
| NM >20% | ✓（40.3%） |
| FCF yield >5% | ✗（见 A） |
| FCF−SBC >0 | ✓（$54.58B） |
| 真缩股 | ✓（7.49B→7.46B, 回购 $22.27B > SBC $12.41B） |
| ROIC >15% 或 ROE >15% | ✓（ROE 34.0%） |
| 护城河宽 | ✓（Azure +39% + Office/Azure 切换成本 + 规模） |

→ **6/7 = 伟大**（FCF yield <5% 是唯一 miss; CapEx $116B AI 数据中心吞噬 FCF）

麻烦定性: **无** — 无困境; AI capex 是增长投资非恶化; Azure +39% 强劲; 近 ATH
→ **折扣系数 = ×1.0**（伟大 + 无麻烦，`discount_coefficient.md` 主表无麻烦列；巴菲特"合理价买伟大公司"——合理价三重保守即边际，无需额外折扣。`mistakes.md` 三·25: "连官方范例 NVDA 都被误套 ×0.75，AAPL/MSFT/GOOG/AMZN 全犯"，此处修正）

## D.2 合理价 + 满仓目标

```
合理价   = $16.20 × 21.5 = $348.30
满仓目标 = $348.30 × 1.0 = $348.30
锚定: EPS=$16.20(v3.1 min), g=13%, PE=21.5x, 系数=×1.0(伟大+无麻烦), 日期: 2026-08-09
```

> 旧 output 用 GAAP $17.95 → 合理价 $385.93 → **修正为 v3.1 $16.20 → 合理价 $348.30**（per min 规则）。
> 旧 output "满仓目标 = 不适用" → **修正为 ×1.0 → 满仓目标 = $348.30**（伟大+无麻烦 → ×1.0，非"不适用"）。
> 安全边际 join A(现价) + D(合理价) 算, 见 output_a.md A.3。

## D.2b DCF 交叉验

> 与 D.2 EPS 模型并列。详见 `docs/dcf.md`。
> MSFT 属高 CapEx 公司（FCF < NI）→ DCF 揭示 EPS 模型高估（`dcf.md` GOOG/NVDA/MSFT pattern）。

```
r = 9% (伟大 6/7)
g = 13% (from Task C)
g > r → Gordon 公式失效 → 封顶 P/FCF₀ = 30x
```

| 口径 | base ($/sh) | P/FCF₀ | DCF/sh | vs EPS 合理价 |
|------|-------------|--------|--------|---------------|
| DCF FCF−SBC | $7.32 | 30x (封顶, g>r) | $222.40 | −36.2% |
| DCF FCF | $8.99 | 30x (封顶, g>r) | $272.27 | −21.8% |

```
FCF (TTM) = $66.99B
SBC (TTM) = $12.41B
FCF−SBC = $54.58B
Shares = 7.453B
FCF/sh = $8.99
(FCF-SBC)/sh = $7.32
net_cash = $76.65B − $56.83B = +$19.83B (净现金)
net_cash/sh = +$2.66
回购 $22.27B > SBC $12.41B → 净缩股 → FCF 为主口径
```

> ⚠ **旧 output net_cash 误用 $128.81B（非"Total Debt"字段）→ 算出净债 −$51.97B → DCF 偏低 ~$10/sh**。修正：`bs_quarterly.csv` Total Debt = $56.83B（= Current Debt $9.23B + LT Debt $47.60B），Cash+短投 = $76.65B → **净现金 +$19.83B**（与 output_b B.4 一致: 净现金 ~$21B）。
>
> **g > r 致 DCF 定量不可靠**: g=13% > r=9%, Gordon 公式分母为负 → 封顶 30x → 乘数被截断。
> **但方向正确（高估）**: FCF/sh $8.99 << EPS $16.20 → FCF 仅 NI 的 50%（CapEx $116B AI 数据中心吞噬 63% OCF）。DCF FCF-SBC $222.40 << EPS 合理价 $348.30。同 GOOG/NVDA 高 CapEx 模式: EPS 模型对高 CapEx 公司高估。

gap 分析:
- gap 1 (EPS→DCF FCF−SBC): $222.40 − $348.30 = **−$125.90** → ① PE 公式 21.5x vs 30x 封顶 ② FCF $8.99 vs EPS $16.20（FCF = NI 55%, CapEx 吞噬）
- gap 2 (DCF FCF−SBC→DCF FCF): $272.27 − $222.40 = **+$49.87** → SBC 差异（$12.41B/7.453B × 30 = $1.664 × 30 = $49.92 ✓）
- gap 3 (EPS→DCF FCF): $272.27 − $348.30 = **−$76.03** → gap1 + gap2 叠加
- **判断: DCF 揭示高估** — 高 CapEx 致 FCF << NI → EPS 模型高估（同 GOOG/NVDA）。但 g>r 封顶 → 定量不可靠; 方向正确。

三口径体系:
```
$222.40 (DCF FCF−SBC, 中性) < $272.27 (DCF FCF, 主口径) < $348.30 (EPS 模型, 高估上界)
```
> 满仓目标仍用 EPS 模型（最保守口径 × 折扣系数 = $348.30 × 1.0 = $348.30）。DCF FCF $272.27 作为"合理价区间"参考——即便用 DCF FCF 口径，现价 $499.99 仍 > $272.27 → 安全边际 −83.6% → 买贵了。

## D.3 敏感性表

| 前瞻 g | 合理 PE | 合理价 (EPS $16.20) | 满仓目标（×1.0） |
|--------|---------|---------------------|---------|
| 10.6%（Rev 3yr CAGR） | 19.1x | $309.42 | $309.42 |
| **13%（基准）** | **21.5x** | **$348.30** | **$348.30** |
| 15%（EPS 3yr CAGR） | 23.5x | $380.70 | $380.70 |

> 即便 g=15% → $381, 仍远低于现价 $500。
> 伟大 + 无麻烦 → ×1.0 → 满仓目标 = 合理价。

## D.4 护栏检查

- [✓] 回购不进 g: g=13% 用业务增长（营收+Azure）, 不含缩股驱动 EPS 增长
- [✓] g 质量: FCF−SBC = +$54.58B > 0（但 CapEx $116B 吞噬 FCF, 黄灯）
- [✓] 高增长封顶: g=13% < 22%, PE=21.5x 不封顶
- [✓] DCF 交叉验: g>r 封顶 → 定量不可靠; DCF 揭示高 CapEx 致 FCF << NI（方向: 高估）
- [✓] 三重保守: EPS min($16.20 v3.1) + g 保守(13%) + 折扣 ×1.0（伟大+无麻烦，合理价本身即边际）

## D.5 综合判定

```
质量判定：伟大（6/7: GM 67.9% + NM 40.3% + FCF−SBC $54.58B + 真缩股 +
ROE 34.0% + 护城河极宽[Azure+39%+Office切换成本+规模]；
瑕疵: FCF yield <5%[见 A, CapEx $116B AI吞噬], 净现金 ~$20B）
× 麻烦无（无困境, AI capex 是增长投资, Azure 强劲, 近 ATH）
→ 伟大 + 无麻烦 → 折扣系数 ×1.0（`discount_coefficient.md` 主表无麻烦列）
→ 满仓目标 = 合理价 × 1.0 = $348.30
```

归类: **买贵了** — 现价 $499.99 > 合理价 $348.30 → 安全边际 −43.6%；伟大公司但 P/E 27.9x >> 框架 21.5x; 无好价格、无困境买点。三要素仅占"好公司"一项。DCF FCF $272.27 口径更贵 → 安全边际 −83.6%。
