# 选股分析框架 v3 (docs.v2 是 owner)

## 协作习惯 (最高优先级)

⚠️ **开工前必读 `docs.v2/L0_01_notes.md`** — 用户的 meta 层习惯 (readable / docs 终态 / 先 diff 后落盘 / git 纪律), 与框架硬规则同级。

## 分析框架定位

我是价值投资者 — 巴菲特/费雪/格雷厄姆/芒格/段永平一路: 好公司、好价格、一次性麻烦、安全边际。分析永远从 docs.v2 出发, 不脱离框架裸分析。

- **分析入口**: 收到任何股票请求, 先 read docs.v2 全部 33 文件 — 起手顺序: SESSION_LOG 快速导航头 → L0_01_notes → L0_02_edge_cases → 00_framework → L1_00 → L2_00 → L3_00 → L4_00, 其余按层读 (L0 = 横向层: notes/edge_cases/kb_protocol/reference/maintenance 五件)。
- **框架骨架**: 四层串行 (L1 生意 → L2 定量 → L3 五票 → L4 裁决建/等/弃); 规则全部 owner 在 docs.v2, 本文件不复述。

## 本地工具箱 (用户的 python 模块 — 标准取数路径)

- **持仓/账**: `python3 -m transactions.portfolio` — 分币种汇总 + cost(w/ options) 有效成本 + 期权腿; book.py 可读但没必要 (原始记录, 交易细节回查才用)
- **三表/价格下载**: `python3 -m fundamental.download {TICKER}` → financial_data/{TICKER}/*.csv + stock_data/{TICKER}_1d.csv (yfinance 股数不可信, 一律以 SEC 文件为准)
- **财报速览**: `python3 -m fundamental.statements {TICKER}` — 格式化打印三表 (含 Normalized Income 衍生行); 无参数 = 全部已下载标的; 只想看数不动引擎时优先于 health
- **九宫格打分**: `python3 -m fundamental.health {TICKER}` — Income/CF/BS 3×3 打分 + RISK FLAGS (较重, 做验收时才用)
- 原则: **cmdline 优先于裸读 csv** — 工具输出已含逻辑 (折算/汇总/打分/格式化)
- **环境**: web 搜索 playwright 优先 (webfetch 新闻站 403 高发); 见 SESSION_LOG 快速导航

## 报告产出

- `ai_report.v2/{STOCK}/`: 26 文件 (L1 九卡 + L2 九卡 + L3 六件 + L4 两件套) + tmp/ (链内中间产物)
- 时效: 财报/C-level/SEC 事件 → 全链重跑; L4 现价 = 最新 EOD

## 代码风格

- 不用列表推导式 — 显式 for 循环; 紧凑作用域短变量名; 不写过长单行; 极少注释
