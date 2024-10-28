from conf import *
from d1_preload import preload

recall_days = 5

for stock_name in ALL:
    base_engine = preload(stock_name)
    stock_df, fig, line = base_engine.stock_df, base_engine.fig, base_engine.line

    hit = False

    for (dates, prices) in line.primary_lines + line.secondary_lines:
        plots = dict(zip(dates, prices))

        for idx in stock_df.index[-recall_days:]:
            date = stock_df.loc[idx]['Date']
            close = stock_df.loc[idx]['close']

            if date in plots and close * 0.98 < plots[date] < close * 1.02:
                print(f'{stock_name} hit at {date}, close={close}, line={plots[date]}')
                hit = True

    if hit:
        fig.show()
