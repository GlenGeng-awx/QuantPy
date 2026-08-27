"""
每日筛选"价格回撤"标的 (cheap v2)。

用法:
    python3 -m fundamental.cheap                   # 默认 stock: 扫 ALL-INDEX 股票
    python3 -m fundamental.cheap --mode=index      # 仅指数(ETF/BTC): ALL∩INDEX
    python3 -m fundamental.cheap ADBE NVDA QQQ     # 显式 ticker (单组, 忽略 --mode)

分组 (--mode):
    stock   ALL-INDEX 股票               (default)
    index   ALL∩INDEX 指数 (ETF/BTC, 如 QQQ/VOO/SLV/GLD/BTC-USD)

合并表 (每组一张):
    Stock | 1Y 2Y 52W c5d c10d c20d | cnt | Elli Neck Line 4th | Close P/E P/S P/B FCF EV/E
    rank(6)+cnt 进排序 (count 降序 + 1Y dd tie-break); TA(4)+估值(6) display。

crash 信号: guru 90pct of rolling 200d, 近 3 交易日命中 → ✓
ETF/BTC: 无 fundamentals → 估值全 '-', 仅 close + 价格信号

模块:
    price.py       6 价格信号 (入场/ranking)
    ta.py          4 TA 命中 (display)
    valuation.py   6 估值 (close/PE/PS/PB/FCF/EV-E, display)
    display.py     print_detail + print_ranking (格式化)
    __main__.py    load_data + evaluate + args/groups + 编排
"""
