from base_engine import BaseEngine

MARGIN = 0.01


def hit(base_engine: BaseEngine) -> str:
    stock_df = base_engine.stock_df

    high = stock_df.iloc[-1]['high']
    low = stock_df.iloc[-1]['low']

    for neck_line in base_engine.line.neck_lines:
        date, price = neck_line[0][-1], neck_line[1][-1]

        if date != stock_df.iloc[-1]['Date']:
            print(f"ignore neck_line: ({date}, {price})")
            continue

        if price * (1 - MARGIN) < high < price * (1 + MARGIN) \
                or price * (1 - MARGIN) < low < price * (1 + MARGIN):
            return f"x neck_line {price:.2f}"

    return ''
