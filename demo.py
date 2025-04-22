from preload import default_periods, preload
from guru import hit
from conf import *

for stock_name in ALL:
    from_date, to_date, interval = default_periods()[0]

    base_engine = preload(stock_name, from_date, to_date, interval)
    stock_df, fig = base_engine.stock_df, base_engine.fig

    tags = hit(base_engine)
    if not tags:
        continue

    fig.update_layout(
        title=fig.layout.title.text + f'<br>{tags}'
    )
    fig.show()
