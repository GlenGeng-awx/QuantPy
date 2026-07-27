# 股票分批表

> 来源：`conf.py` 的 `ALL`（90 只 = 78 股票 + 12 非股票标的）。
> 按行业分组，方便同业对比（Task A 第二步需要同业倍数）。
> 小批次 = 该行业在我们 universe 里就这些，非人为拆分。

## 总览

| 批次 | 行业 | 数量 | 标的 |
|------|------|------|------|
| B1 | Mega-cap Tech | 8 | AAPL MSFT NVDA GOOG AMZN TSLA META SPCX |
| B2 | Semiconductor | 7 | TSM AVGO ASML AMD QCOM INTC MU |
| B3 | Software & SaaS | 10 | ADBE CRM ORCL PLTR SNOW ZM OKTA TTD SNAP PINS |
| B4 | Internet & Platform | 8 | NFLX UBER SHOP SPOT COIN CRCL CPNG SE |
| B5 | Fintech & Payments | 9 | MA V PYPL EBAY NU HOOD AFRM KLAR XYZ |
| B6 | Banks | 4 | JPM BAC GS MS |
| B7 | Energy | 2 | XOM CVX |
| B8 | Consumer & Industrial | 9 | WMT PG KO MCD DIS BA HPQ DELL ERIC |
| B9 | Medical | 7 | LLY NVO JNJ MRK PFE GILD BNTX |
| B10 | Auto (EV) | 4 | RIVN NIO LI XPEV |
| B11 | China & HK | 10 | BABA PDD JD TCOM BIDU BEKE BILI FUTU TME 0700.HK |

## 标记说明

| 标记 | 含义 | 估值影响 |
|------|------|----------|
| 银行 | 银行/数字银行 | 不用 EPS 框架，用 P/B |
| 周期 | 盈利随商品/周期摆动（半导体/能源/加密/券商/生物科技） | P/E 分位会反读，用中周期正常化 P/E + P/B |
| 多币种 | ADR：股价币种 ≠ 财报币种 | EV/EBITDA 等比率屏幕值失真，手算 |
| VIE | 中概股可变利益实体结构 | 治理风险，查备案 |

---

## B1 — Mega-cap Tech（8）

| Ticker | 公司 | 标记 |
|--------|------|------|
| AAPL | Apple | |
| MSFT | Microsoft | |
| NVDA | NVIDIA | 周期 |
| GOOG | Alphabet | 双层股权 |
| AMZN | Amazon | |
| TSLA | Tesla | |
| META | Meta Platforms | 双层股权 |
| SPCX | Space Exploration | |

## B2 — Semiconductor（7）

| Ticker | 公司 | 标记 |
|--------|------|------|
| TSM | TSMC | 周期,多币种 |
| AVGO | Broadcom | 周期 |
| ASML | ASML | 周期,多币种 |
| AMD | AMD | 周期 |
| QCOM | Qualcomm | 周期 |
| INTC | Intel | 周期 |
| MU | Micron | 周期 |

## B3 — Software & SaaS（10）

| Ticker | 公司 | 标记 |
|--------|------|------|
| ADBE | Adobe | |
| CRM | Salesforce | |
| ORCL | Oracle | |
| PLTR | Palantir | |
| SNOW | Snowflake | |
| ZM | Zoom | |
| OKTA | Okta | |
| TTD | The Trade Desk | |
| SNAP | Snap | |
| PINS | Pinterest | |

## B4 — Internet & Platform（8）

| Ticker | 公司 | 标记 |
|--------|------|------|
| NFLX | Netflix | |
| UBER | Uber | |
| SHOP | Shopify | 多币种(USD/CAD) |
| SPOT | Spotify | 多币种(USD/EUR) |
| COIN | Coinbase | 周期 |
| CRCL | Circle | |
| CPNG | Coupang | 多币种(USD/KRW) |
| SE | Sea (Shopee) | 多币种(USD/SGD) |

## B5 — Fintech & Payments（9）

| Ticker | 公司 | 标记 |
|--------|------|------|
| MA | Mastercard | |
| V | Visa | |
| PYPL | PayPal | |
| EBAY | eBay | |
| NU | Nu Holdings | 银行 |
| HOOD | Robinhood | 周期 |
| AFRM | Affirm | |
| KLAR | Klarna | |
| XYZ | Block | |

## B6 — Banks（4）

| Ticker | 公司 | 标记 |
|--------|------|------|
| JPM | JPMorgan | 银行 |
| BAC | Bank of America | 银行 |
| GS | Goldman Sachs | 银行 |
| MS | Morgan Stanley | 银行 |

## B7 — Energy（2）

| Ticker | 公司 | 标记 |
|--------|------|------|
| XOM | Exxon Mobil | 周期 |
| CVX | Chevron | 周期 |

## B8 — Consumer & Industrial（9）

| Ticker | 公司 | 标记 |
|--------|------|------|
| WMT | Walmart | |
| PG | Procter & Gamble | |
| KO | Coca-Cola | |
| MCD | McDonald's | |
| DIS | Disney | |
| BA | Boeing | |
| HPQ | HP Inc | |
| DELL | Dell Technologies | |
| ERIC | Ericsson | 多币种(USD/SEK) |

## B9 — Medical（7）

| Ticker | 公司 | 标记 |
|--------|------|------|
| LLY | Eli Lilly | |
| NVO | Novo Nordisk | 多币种(USD/DKK) |
| JNJ | Johnson & Johnson | |
| MRK | Merck | |
| PFE | Pfizer | |
| GILD | Gilead Sciences | |
| BNTX | BioNTech | 周期,多币种(USD/EUR) |

## B10 — Auto / EV（4）

| Ticker | 公司 | 标记 |
|--------|------|------|
| RIVN | Rivian | |
| NIO | NIO | 多币种(USD/CNY) |
| LI | Li Auto | 多币种(USD/CNY) |
| XPEV | XPeng | 多币种(USD/CNY) |

## B11 — China & HK（10）

| Ticker | 公司 | 标记 |
|--------|------|------|
| BABA | Alibaba | 多币种(USD/CNY),VIE |
| PDD | PDD Holdings | 多币种(USD/CNY),VIE |
| JD | JD.com | 多币种(USD/CNY),VIE |
| TCOM | Trip.com | 多币种(USD/CNY),VIE |
| BIDU | Baidu | 多币种(USD/CNY),VIE |
| BEKE | KE Holdings | 多币种(USD/CNY),VIE |
| BILI | Bilibili | 多币种(USD/CNY),VIE |
| FUTU | Futu Holdings | 多币种(USD/HKD) |
| TME | Tencent Music | 多币种(USD/CNY),VIE |
| 0700.HK | Tencent | 多币种(HKD/CNY) |

---

## 非股票标的（12）

> 框架外或特殊处理：ETF 用指数级估值温度，商品/BTC 无现金流不产合理价。

| Ticker | 名称 | 类别 |
|--------|------|------|
| 510300.SS | 沪深300 ETF | CN 指数 |
| 510880.SS | 上证红利 ETF | CN 指数(红利) |
| 588000.SS | 科创50 ETF | CN 指数(成长) |
| 159915.SZ | 创业板 ETF | CN 指数(成长) |
| 518680.SS | 黄金 ETF (SH) | 商品 |
| GLD | SPDR Gold | 商品 |
| SLV | iShares Silver | 商品 |
| BTC-USD | Bitcoin | 加密货币 |
| QQQ | Nasdaq 100 | US 指数 |
| VOO | S&P 500 | US 指数 |
| SOXX | 半导体 ETF | US 指数(周期) |
| KWEB | 中概互联网 ETF | US 指数 |
