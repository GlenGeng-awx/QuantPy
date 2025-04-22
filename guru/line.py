from base_engine import BaseEngine

MARGIN = 0.01


def hit(base_engine: BaseEngine) -> str:
    stock_df = base_engine.stock_df
    high = stock_df.iloc[-1]['high']
    low = stock_df.iloc[-1]['low']

    lines = base_engine.line.primary_lines + base_engine.line.secondary_lines

    for line in lines:
        date, price = line[0][-1], line[1][-1]

        if date != stock_df.iloc[-1]['Date']:
            print(f"ignore line: ({date}, {price})")
            continue

        if price * (1 - MARGIN) < high < price * (1 + MARGIN) \
                or price * (1 - MARGIN) < low < price * (1 + MARGIN):
            return f"x line {price:.2f}"

    return ''
