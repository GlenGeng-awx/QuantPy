from base_engine import BaseEngine

MARGIN = 0.01
OFFSET = -1


def hit(base_engine: BaseEngine) -> str:
    stock_df = base_engine.stock_df

    high = stock_df.iloc[OFFSET]['high']
    low = stock_df.iloc[OFFSET]['low']
    close = stock_df.iloc[OFFSET]['close']

    lines = base_engine.line.primary_lines + base_engine.line.secondary_lines

    for line in lines:
        date, price = line[0][OFFSET], line[1][OFFSET]

        if date != stock_df.iloc[OFFSET]['Date']:
            print(f"ignore line: ({date}, {price})")
            continue

        if price * (1 - MARGIN) < high < price * (1 + MARGIN) \
                or price * (1 - MARGIN) < low < price * (1 + MARGIN) \
                or price * (1 - MARGIN) < close < price * (1 + MARGIN):
            return f"x line {price:.2f}"

    return ''
