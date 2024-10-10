from playground import prepare, INDEX_NAMES, STOCK_NAMES_TIER_0, STOCK_NAMES_TIER_1

recall_days = 5

for stock_name in STOCK_NAMES_TIER_1:
    base_engine = prepare(stock_name)
    stock_df, fig, line = base_engine.stock_df, base_engine.fig, base_engine.line

    hit = False

    for idx in stock_df.index[-recall_days:]:
        date = stock_df.loc[idx]['Date']
        close = stock_df.loc[idx]['close']

        for (dates, prices) in line.primary_lines + line.secondary_lines:
            d = dict(zip(dates, prices))
            if date in d and close * 0.97 < d[date] < close * 1.03:
                print(f'{stock_name} hit at {date}, close={close}, line={d[date]}')
                hit = True

    if hit:
        fig.show()
