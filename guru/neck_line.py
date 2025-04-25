from base_engine import BaseEngine

MARGIN = 0.01
OFFSET = -1


def hit(base_engine: BaseEngine) -> str:
    stock_df = base_engine.stock_df

    high = stock_df.iloc[OFFSET]['high']
    low = stock_df.iloc[OFFSET]['low']
    close = stock_df.iloc[OFFSET]['close']

    for neck_line in base_engine.line.neck_lines:
        date, price = neck_line[0][OFFSET], neck_line[1][OFFSET]

        if date != stock_df.iloc[OFFSET]['Date']:
            print(f"ignore neck_line: ({date}, {price})")
            continue

        if price * (1 - MARGIN) < high < price * (1 + MARGIN) \
                or price * (1 - MARGIN) < low < price * (1 + MARGIN) \
                or price * (1 - MARGIN) < close < price * (1 + MARGIN):
            return f"x neck_line {price:.2f}"

    return ''
