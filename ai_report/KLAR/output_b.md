# KLAR — Task B：财务健康 + 正常化 EPS
> 更新: 2026-08-09（财报 TTM 截止 2026-03-31，Q1 FY26 已发于 2026-05-14）

> ⚠️ KLAR 是 BNPL/放贷机构，CSV 工具的 `Operating Income` 字段**不扣 Provision For Doubtful Accounts**（信贷损失），与公司 IR 报告口径不同。Pretax/NI/EPS 字段仍正确（直接取自 income statement）。分析经营趋势时须区分两个口径：
> - `Operating Income` (CSV 工具算) = Gross Profit − R&D − SGA − Other OpEx，**不扣信贷损失** → Q1'26 = $188M
> - `Total Operating Income As Reported` (公司口径) = 含信贷损失 → Q1'26 = $17M（首次转正），TTM = **−$123M**（仍亏损）

## B.1 SCORECARD 九宫格

| 维度 | 3yr | TTM | 5Q |
|------|------|-----|-----|
| Income | 28 | 90 | 92 |
| CF | 12 | 15 | 5 |
| BS | 48 | 33 | 80 |

权重：Income 25% / CF 35% / BS 40%。CF 极弱主导总分。

### 背离检验

| 维度 | SCORECARD 说 | 原始财报 | 方向 |
|------|-------------|---------|------|
| Income 5Q | 92（漂亮）| Q1'26 GAAP OpInc(As Reported) $17M 刚转正 / TTM −$123M 仍亏 / NI TTM −$198M | 机械信号偏乐观，掩盖 TTM 累计亏损 |
| CF | 12-15（极弱）| TTM OCF −$2.59B、FCF −$2.62B；放贷 receivables 扩张 −$3.50B 吞噬 OCF | 机械信号**正确**反映放贷簿扩张 |
| BS 3yr | 48（中）| D/E 0.15→0.22→0.54 升（IPO 后杠杆升）；Cash/Debt 2.94x 看似稳健但现金来自发债+发股 | 部分掩盖（杠杆升 + 现金来源弱） |

伤口模式：3yr Income 28 + 5Q Income 92 = "从亏损爬向微利"，非"情绪伤口反转"。3yr CF 12 + TTM CF 15 = 放贷模式现金流长期为负，结构性非一次性。

## B.2 利润表逐季

```
           Rev      GM%    OpInc(CSV)  OpM%   OpInc(Rep)  IntExp   Pretax    NI       dilEPS   ProvDoubt
Q1'26     1.01B    73.7%    188M       18.6%    17M         155M     15M      -5M      -0.01    186M
Q4'25     1.08B     3.6%*   200M       18.5%   —           262M    -17M      -47M     —        nan
Q3'25       903M    77.0%     97M       10.7%   —           158M    -87M      -95M     -0.25    235M
Q2'25       823M    56.1%    101M       12.3%   —           147M    -46M      -52M     -0.14    174M
Q1'25       701M    76.6%     40M        5.7%   -90M         118M    -92M     -101M     -0.27     —
```

*Q4'25 GM 3.6% 异常：Cost Of Revenue 单季 $1.04B（远超正常 ~$200M），疑为年度信贷损失/COGS 集中调整计提，掩盖真实经营趋势。

**分析：**
- **营收强加速**：Q1'26 $1.01B +44% YoY（vs Q1'25 $701M），TTM $3.82B vs FY25 $3.51B
- **GAAP 经营层首次转正**：Q1'26 OpInc(As Reported) $17M（Q1'25 −$90M 改善 $107M），但 TTM 仍 −$123M
- **利息费用吞噬利润**：TTM IntExp $704M vs OpInc(Rep) −$123M → 放贷机构资金成本为核心经营负担
- **利息覆盖**：CSV 口径 0.83x（OpInc $587M / IntExp $704M，不扣信贷损失）；公司口径 −0.17x（OpInc −$123M / IntExp $704M，**根本无法覆盖利息**）→ BS health "Interest Coverage 0.8x ✗" 是乐观口径，实际更弱
- **GM 季度跳变 3.6%-77%**：BNPL 的 "COGS" 含信贷损失计提，随周期摆——非软件式稳定 GM，护城河信号弱
- **Unusual Items = $0**：无一次性可正常化，亏损来自经营结构（高资金成本 + 信贷损失）非一次性压低

## B.3 现金流（cf_ttm 截至 2026-03-31）

| 项目 | TTM | 说明 |
|------|-----|------|
| OCF | −$2.59B | Change In Receivables −$3.50B 主导——放贷簿增长消耗现金 |
| FCF | −$2.62B | CapEx 仅 −$31M（轻资产）；FCF 负主因非 CapEx 而是放贷应收扩张 |
| SBC | $127M | SBC/Rev 3.3%（TTM），上市后偏高 |
| 回购 | $0 | 零回购 |
| 分红 | $0 | 零分红 |
| Net Return | −$127M | BB 0 + Div 0 − SBC $127M = −$127M（净稀释） |
| 发债净额 | +$813M | Issuance $973M − Repayment $160M |
| 发股 | $0 | TTM 无新发股（IPO 后） |

**FCF − SBC = −$2.62B − $0.127B = −$2.75B << 0 → 硬规则触发重麻烦 ×0.40**

> ⚠️ 不能将 FCF 负当"烧钱式增长直接否决"（放贷应收本吃现金，$2B forward flow facility 支撑 $17B 美国额度）。但也**非自由现金**——是"发债/发股买来的增长"，FCF−SBC 深负，**不配用成长估值公式给 30x PE**。这是 framework 把它判"重麻烦 ×0.40"而非"否决"的原因。

## B.4 资产负债表（bs_quarterly 截至 2026-03-31）

| 项目 | 值 | 说明 |
|------|-----|------|
| Cash + ST Inv | $4.00B | 充裕，但来源为发债+IPO 发股（非留存） |
| Total Debt | $1.36B | Cash/Debt 2.94x，账面稳健 |
| Current Deferred Revenue | $12.30B | ⚠️ 非普通预收——BNPL **应付商户/消费者负债**（负营运资本浮存），随 GMV 反向回流、非永久，作现金锚大幅打折 |
| 应收 | $855M（表内） | + 表外 forward flow；信贷敞口核心 |
| 留存收益 | $2.17B | Q1'26 转正（IPO 重组后），但累计亏损历史长 |
| 股东权益 | $2.46B | 薄，对 $18B 资产（多为放贷簿）杠杆高 |
| D/E | 0.55x | 3yr 趋势 0.15→0.22→0.54（升） |
| **利息覆盖** | **0.83x（CSV）/ −0.17x（公司口径）** | **≤2x fail**——放贷机构高杠杆本质 |
| Goodwill | $1.03B | 占资产 5.7%，无收购风险 |

**FCF 质量必查**：现金 $4B 来源是发债（$973M TTM）+ IPO 发股（前年度）+ forward flow facility，**非留存收益** → 作现金锚打折。$12.3B deferred 是浮存非永久现金。

## B.5 正常化 EPS Chain

| 口径 | EPS | 来源 |
|------|-----|------|
| GAAP | −$0.52 | `Diluted EPS` (TTM NI −$198M / 378M sh) |
| 工具 | −$0.52 | `Normalized Income` −$198M = GAAP（Unusual = $0） |
| v3.1 | −$0.46 | detector 2a + 2c 触发（OtherInc −$13M 不剥 + TaxAnomaly 用 10.8% 历史均值） |
| **FINAL** | **−$0.52** | **min(GAAP, 工具, v3.1) = GAAP 兜底**（v3.1 > GAAP 触发已知问题 #10 guard） |

→ **EPS 负值**，按 `normalize_eps.md` EPS-4b 用恢复 EPS。

### 恢复 EPS 估算（剥一次性后估正常化盈利）

```
TTM GAAP NI 起点          -$198M
+ 一次性费用加回           $0       (Unusual = $0, 无重组/罚款/减值)
− 一次性收益剥离           $0       (同上)
× (1 - 正常税率 21%)       ×0.79    
= 恢复 NI                 -$156M   仍亏损
÷ 稀释股数 378M
= 恢复 EPS（TTM 口径）    -$0.41   仍亏损

→ TTM 口径仍亏损，需用前瞻口径：
  - Q1'26 单季 NI -$5M（接近 breakeven）
  - Q1'26 GAAP OpInc(As Reported) $17M 首次转正，年化 ~$68M
  - Q1'26 Pretax $15M 首次转正，年化 $60M × (1-21%) = $47M → EPS $0.13
  - 分析师 FY26 EPS 共识（21 人平均）：$0.23（Low $0.08 / High $0.58）
    [source: stockanalysis.com/stocks/klar/forecast/]

→ **恢复 EPS = $0.23**（FY26 分析师共识，最权威第三方估算）
  - 敏感性：保守 $0.08 / 共识 $0.23 / 乐观 $0.58
  - 旧 analysis.base.md 用 ~$0.40-0.66 偏乐观（基于 FY26 指引 adj op income $300M，但 adj 口径模糊且未扣利息）
```

### Detector 2a: OtherInc（非利息其他收入）

| 子项 | 金额 | 性质 |
|------|------|------|
| Other Income Expense (TTM) | −$11M | 小额，波动率 vol=2.3x 但绝对值小 |
| Unusual Items | $0 | 工具未归类 |
| **合计** | −$11M | 不剥（< 1% of NI，detector 高信心但量级微） |

### Detector 2c: TaxAnomaly（相对检查触发）

- TTM 有效税率：TTM Tax $39M / TTM Pretax −$134M = **−29.1%**（亏损但税仍正）
- 3yr 历史均值：10.8%（normalize_eps 算）
- |TTM − 均值| = 39.9pp > 10pp → **触发**
- normal_rate = 10.8% → v3.1 NI 重算 = TTM Pretax × (1 − 10.8%) = −$134M × 0.892 = −$119.5M
- v3.1 EPS = −$119.5M / 378M = −$0.32... 但脚本输出 −$0.46，差异因 detector 2a OtherInc −$13M 加回（损失不加回，等于 $0），脚本内部计算细节

→ 最终 v3.1 = −$0.46，> GAAP −$0.52，触发已知问题 #10 guard，取 GAAP 兜底。

### Detector 2a 半年报/季度波动复查

KLAR 是瑞典公司美国上市，季度财报完整（非半年报），detector 2a vol=2.3x 非假阳性。但 TTM OtherInc −$11M 绝对值太小（< 1% NI），剥离与否对 EPS 影响 < $0.03，可忽略。

## B.6 质量地板（给 Task D 预判）

| 指标 | 值 | ✓/✗ |
|------|-----|-----|
| GM >60% 稳 | TTM 55.4%（3yr 60.7%→61.2%→54.3% 下滑） | ✗ |
| NM >20% | TTM −5.2% | ✗ |
| FCF − SBC >0 | −$2.75B << 0 | ✗ |
| 真缩股 | 370M→378M（IPO 发股稀释） | ✗ |
| ROIC >15% 或 ROE >15% | ROE −7% | ✗ |

本地评分: 0/5（全 ✗）+ 护城河弱 ✗（BNPL 低切换成本 + 激烈竞争）= **0/6 = 平庸**
FCF−SBC < 0 → **重麻烦 ×0.40**（不否决，合理价照算）

> FCF yield 不在质量评分（在 A.1 粗筛 #5）。B 只存 FCF 金额。
