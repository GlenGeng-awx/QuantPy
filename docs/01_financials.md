# Task 1: 财务健康 + 正常化 EPS

> **产出**: SCORECARD + 正常化 EPS + per-share 估值输入 + BS 生存力门 + 总结。
> 
> **依赖**: `financial_data/` 下全部 CSV (本地, 免费, 财报后更新)。
>
> 判断"这是不是一家好公司" + 算出"干净的盈利 EPS"。
> 
> 规则只产数据; 合理价口径/DCF base 选择见 §5.2/§5.3。
>
> **output_1.md 结构 = 本文档节序 (§1.1→§1.2→§1.3→§1.4→§1.5); 各 § 节的表格式即 output 格式, 不另设模板。**

## §1.1 SCORECARD 九宫格

```bash
python3 -m fundamental.health STOCK    # 自动跑九宫格
```

output 格式:

| 维度 | 3yr | TTM | 5Q |
|------|------|-----|-----|
| Income | (score) | (score) | (score) |
| CF | (score) | (score) | (score) |
| BS | (score) | (score) | (score) |

### 背离检验

SCORECARD 是报案人不是评委。机械信号 vs 原始财报的 gap = 错杀/陷阱藏身处。只列低分维度 (< 100)。

| 维度 | SCORECARD 说 | 原始财报 | 方向 |
|------|-------------|---------|------|
| (低分维度) | (机械信号) | (实际情况) | (枚举) |

方向枚举:

| 方向 | 含义 |
|------|------|
| 错杀 | 机械低分 vs 实际好 |
| 损伤 | 真实恶化 |
| 陷阱 | 机械低分 = 实际差 |
| 已定价 | 市场已反映 |
| 已恢复 | 3yr 低 + TTM/5Q 高 |
| 需追查 | 待 Task 3 |

### 定量损伤评估

3yr 高分 + TTM/5Q 低分 = 损伤信号; 3yr 低分 + TTM/5Q 高分 = 已恢复。列所有非 100 维度。

| 低分维度 | 跌幅 | 受影响指标 | 持续 | → Fisher 15 追查 |
|----------|------|-----------|------|-----------------|
| (维度) | -NNpp 或 已恢复 | (具体指标 + 数值) | NQ 或 NYr | #(条目) |

- 跌幅 = 3yr→TTM 和 3yr→5Q 中跌幅更大者 (单位: pp)
- 持续 = NQ (季度数) 或 NYr (年数), 损伤已持续多久
- 已恢复行标"已恢复"替代跌幅数值
- 定量只报损伤程度; "一次性 vs 结构性" 判断交 Fisher 15 麻烦维度 (§3.2)

---

## §1.2 财务详情

### 4 年趋势表

文件: income_annual.csv + cf_annual.csv。列0=最新年, 列N=最旧年。⚠ PRINT header 验证 year_gap (col0_year - colN_year = 3; 不足 3yr → 用 2yr, 注明)。

output 格式:

| 指标 | FY{N-3} | FY{N-2} | FY{N-1} | FY{N} | 趋势 |
|------|---------|---------|---------|-------|------|
| Revenue | ... | ... | ... | ... | ↑/↓/稳定 |
| Rev YoY | — | ... | ... | ... | accelerating/decelerating/volatile |
| GM% | ... | ... | ... | ... | ↑/↓ |
| OpInc | ... | ... | ... | ... | ↑/↓ |
| NM% | ... | ... | ... | ... | ↑/↓ |
| OCF | ... | ... | ... | ... | ↑/↓ |
| FCF | ... | ... | ... | ... | ↑/↓ |
| SBC | ... | ... | ... | ... | % Rev |

> 喂入 Task 2 (g: Revenue CAGR) + Task 3 (Fisher #5/#6/#10/#13)

### 利润表逐季

文件: income_quarterly.csv, 列0=最新季。近 5 季。

output 格式:

| Q | Rev($B) | GM% | OpInc($B) | OpM% | EPS |
|---|---------|-----|-----------|------|-----|
| (季度) | ... | ... | ... | ... | ... |

看: GM 连续下滑 → 定价权恶化; SGA 突跳 → 收购; 税率异常 → 需正常化; OpM 转负 → 经营亏损

### 现金流

文件: cf_ttm.csv。用 TTM 数据。

output 格式:

| 项目 | TTM | 说明 |
|------|-----|------|
| OCF | $val | OCF/NI >1 = 利润含金量高 |
| FCF | $val | FCF 金额 (yield 在 Task 4) |
| SBC | $val | FCF−SBC = 真实现金创造; % Rev |
| FCF-SBC | $val | 负 → ×0.40 硬规则 (§3.2) |
| 回购 | $val | vs SBC: >> → ⑧FCF base; ≤ → ⑦FCF-SBC base |
| 股息 | $val | 总返还 = 回购 + 股息 vs FCF |
| CapEx | $val | /OCF: >30% → 超级周期 (§5.2/§5.4) |
| D&A | $val | vs CapEx: D&A > CapEx → FCF > NI (轻资产) |
| 收购 | $val | Purchase of Business (如有) |

> SBC 字段缺失 = 非科技公司 (WMT/MCD/KO): SBC=$0, FCF−SBC=FCF。
> ⚠ SBC 非现金机制 (FCF 不含 SBC, FCF-SBC 只扣一次, 防双扣) → 见 §5.4。

### 资产负债表

文件: bs_quarterly.csv, 列0=最新季。

output 格式:

| 项目 | 值 | 说明 |
|------|-----|------|
| Cash + ST Inv | $val | Cash Cash Equivalents And Short Term Investments |
| Total Debt | $val | 含租赁; 拆分 LT + Current + Leases |
| Net Cash | $val | Cash + ST Inv − Total Debt; 负 = 净债 |
| D/E | $val | Total Debt / Equity |
| 利息覆盖 | $val | OpInc / Interest Expense; >5x ✓ / 2-5x ⚠ / ≤2x ✗ |
| Goodwill | $val | GW / Total Assets; 跳升 = 收购 |
| Inventory | $val | vs Rev 变化 (+/- pp); 缺 = 轻资产 |
| AR | $val | vs Rev 变化; AR 增快 = 渠道压货 |
| CapEx/OCF | $val% | >30% → 超级周期 |
| Current Ratio | $val | <1 ⚠ (排除递延收入后 adj) |

> 权益: Stockholders Equity 负 = 长期回购超净利 (如 ADBE/QCOM)

---

## §1.3 正常化 EPS

### 原理

正常化 EPS = min(GAAP EPS, 工具 EPS, v3.1 EPS)。三个口径各有盲区, 取最低 = 最保守。

| 口径 | 来源 | 能抓 | 盲区 |
|------|------|------|------|
| GAAP EPS | `Diluted EPS` | 无 (原始) | 不剔一次性 |
| 工具 EPS | `Normalized Income / Shares` | 正式归类 Unusual | 漏 OtherInc MTM |
| v3.1 EPS | detector 计算 | OtherInc MTM + 更多 | 可能过度剔/误剔 |

output 格式:

| 口径 | EPS | 来源 |
|------|-----|------|
| GAAP | $val | Diluted EPS (income_ttm) |
| 工具 | $val | Normalized Income / shares |
| v3.1 | $val | detectors: (列出触发项) |
| **FINAL** | **$val** | **min(GAAP, 工具, v3.1)** |

### v3.1 detectors (8 个)

| # | Detector | 信心 | 自动剔? | 看 |
|---|----------|------|--------|-----|
| 2a | OtherInc → 投资 MTM | 高 | ✅ | 季度波动率 >2x 或正负摆动 |
| 2b | Restructuring | 中 | ❌ 只标记 | 费用非收益, 不剥离 (常连续多年) |
| 2c | TaxAnomaly | 中 | ✅ | Step1: TTM 税率<0%→21%法定; Step2: vs 历史均值 |
| 2d | OpIncDrop | 低 | ❌ 只标记 | 需外部确认 |
| 2e | GMDrop | 中 | ✅ | 3yr均值GM% - TTM > 5pp |
| 2f | RDSpike | 中 | ✅ | TTM R&D% - 3yr均值 > 3pp |
| 2g | SGASpike | 低 | ❌ 只标记 | SGA 增长原因多 |
| 2h | Discontinued | 高 | ✅ | NI_total ≠ NI_continuing |

### v3.1 计算

```
只剔 high + medium 信心 detector:
  amount > 0 (收益) → 剥离 (降低 NI)
  amount < 0 (损失) → 不加回 (保持 GAAP, 保守)

v3.1 税前 = Pretax - sum(max(0, pre-tax detectors))
v3.1 NI = v3.1 税前 × (1 - 正常税率) - sum(after-tax detectors)
v3.1 EPS = v3.1 NI / 稀释股数
```

### 恢复 EPS (EPS 负值时)

```
当 GAAP EPS ≤ 0 → min() 均为负 → PE 无意义
→ 恢复 EPS = (Pretax + 一次性费用加回 − 一次性收益剥离) × (1 - 正常税率) / 股数
→ 标注"恢复 EPS", 与正常化 EPS 区分
→ 若恢复 EPS 仍 ≤ 0 → 标注"经营亏损不可恢复", EPS 模型 N/A (估值能力判断 §6.1)
```

### 已知问题

1. 银行不适用 (Operating Income=$0, 用 P/B)
2. OtherInc 过度剔 (投资控股型: TSM/0700.HK) → SOTP 补偿
3. 半年报假阳性 (中概季度 CSV 为零 → vol 虚高) → 标"假阳性"
4. v3.1 > GAAP (负税率, 无剥离) → min() 兜底取 GAAP
5. OtherInc 净额陷阱 (gross 收益被 gross 亏损掩盖) → Task 5 手动查 gross
6. TaxAnomaly 不在 unusual items (如 QCOM FY25 税 $7.1B, CPNG FY23 税收益 $776M) → Normalized Income 未剔 → v3.1 检测但可能不抓

### 实装

```bash
python3 docs/normalize_eps.py STOCK
# 或: python3 -c "import sys; sys.path.insert(0,'docs'); from normalize_eps import normalize_eps; print(normalize_eps('STOCK'))"
```

---

## §1.4 估值输入 + BS 生存力 (→ Task 5)

正常化 EPS 和 per-share 估值数据一起算好, Task 5 直接读 (规则/选择在 §5.2/§5.3)。

### per-share 计算规则

- **shares** = TTM diluted average shares (income_ttm.csv `Diluted Average Shares`)
- **net_cash** = bs_quarterly 最新季 `Cash Cash Equivalents And Short Term Investments` − `Total Debt` (含租赁)
- **OpInc/Interest** = income_ttm.csv `Operating Income` / `Interest Expense`

### 估值输入 output 格式:

| 指标 | 值 | 说明 |
|------|-----|------|
| EPS (FINAL) | min(GAAP, 工具, v3.1) | 正常化 EPS (§1.3); 负 → 恢复 EPS |
| FCF/sh | FCF / shares | ⑧ DCF base (回购>SBC, §5.2) |
| FCF-SBC/sh | (FCF - SBC) / shares | ⑦ DCF base (回购≤SBC, §5.2); 负 → ×0.40 |
| net_cash/sh | (Cash+ST Inv − Total Debt) / shares | DCF + net_cash |
| 回购 vs SBC | buyback vs SBC | 决定 DCF base + 合理价口径 (§5.2/§5.3) |
| CapEx/OCF | CapEx / OCF | >30% → 超级周期 (§5.2/§5.4) |
| SBC/Rev | SBC / Revenue | >5% → SBC 重 |
| 股数趋势 | shares 变化 | 下降=真缩股, 上升=稀释 |

### BS 生存力门 output 格式 (§5.1):

| 条件 | 值 | ✓/✗ |
|------|-----|-----|
| 利息覆盖 > 5x | (val) | ✓/✗ |
| FCF-SBC > 0 | (val) | ✓/✗ |
| 净现金 > 0 | (val) | ✓/✗ |

> 豁免: 高净债但利息覆盖 > 10x + FCF-SBC 持续正 (3yr) → 通过
> FCF-SBC < 0 → ×0.40 硬规则 override (不否决, 总是估值, §3.2)

---

## §1.5 总结 (→ Task 2/3/5 快速消费)

3-5 条归纳, 连接数据点, 不复述数字:

| 项 | 内容 |
|----|------|
| 一句话定性 | 好公司 / 周期低谷 / troubled / 能力圈外 |
| 关键 flag | EPS 符号, FCF-SBC 符号, 税异常, margin 方向, CapEx/OCF, 其他 |
| 估值能力预检 | §6.1 Step 1 proxy: 能/价值陷阱/能力圈外 (附条件; g 用 Revenue 趋势作 proxy, 质量用 NM/GM/FCF 粗判, 最终判定在 Task E) |
| Top risk | Task 2/3/5 需关注的最大风险 (1-2 条) |

预检条件 (§6.1 Step 1 的 proxy, 顺序判定命中即停):
- EPS > 0 AND FCF-SBC > 0 → 能
- g > 20% AND FCF-SBC ≤ 0 → 能 (Path B 用 P/S)
- EPS ≤ 0 AND FCF-SBC ≤ 0 AND 质量 ≤5/10 PASS (平庸, 待 Task 3) → 价值陷阱
- 其余 EPS ≤ 0 AND FCF-SBC ≤ 0 → 能力圈外

> Task 1 预检: g 用 Revenue 趋势 (3yr CAGR 或 TTM YoY) 作 proxy; 质量用 NM/GM/FCF 粗判 (精确判定在 Task 3/E)
> Task 1 只产 proxy flag; 最终判定 = Task E Step 1 (§6.1)
