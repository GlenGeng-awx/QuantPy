import plotly.graph_objects as go
from util import *


def add_candlestick(fig: go.Figure, data: pd.DataFrame):
    fig.add_trace(
        go.Candlestick(
            x=data['Date'],
            close=data['close'],
            open=data['open'],
            high=data['high'],
            low=data['low'],
            name="Candlesticks",
            increasing_line_color='red',
            decreasing_line_color='green',
            line=dict(width=0.5)
        )
    )


def add_column(data: pd.DataFrame, to_be_added_key: str, to_be_added_value: pd.Series):
    data[to_be_added_key] = data.apply(
        lambda row: to_be_added_value.isin([row['Date']]).any(),
        axis=1
    )


def add_scatter(fig: go.Figure, data: pd.DataFrame, key: str, value: str, color: str, size: int):
    fig.add_trace(
        go.Scatter(
            x=data[data[key]]['Date'],
            y=data[data[key]][value],
            mode='markers',
            marker=dict(
                color=color,
                size=size
            )
        )
    )


def add_up_box(fig, data: pd.DataFrame, from_idx, to_idx):
    from_date = data.loc[from_idx]['Date']
    from_low = data.loc[from_idx]['low']

    to_date = data.loc[to_idx]['Date']
    to_high = data.loc[to_idx]['high']

    delta = to_high - from_low
    pst = 100 * delta / from_low

    fig.add_shape(
        type="rect",
        x0=from_date, y0=from_low, x1=to_date, y1=to_high,
        line=dict(
            color="Red",
            width=1,
            dash="dot",
        ),
        label=dict(
            text=f'{to_idx - from_idx}D <br> {delta:.2f}$ <br> +{pst:.2f}%',
            textposition="bottom center"
        ),
    )

    mid = (from_low + to_high) / 2

    fig.add_shape(
        type="line",
        x0=from_date, y0=mid, x1=to_date, y1=mid,
        line=dict(
            color="Red",
            width=0.5,
            dash="dot",
        )
    )


def add_down_box(fig, data: pd.DataFrame, from_idx, to_idx):
    from_date = data.loc[from_idx]['Date']
    from_high = data.loc[from_idx]['high']

    to_date = data.loc[to_idx]['Date']
    to_low = data.loc[to_idx]['low']

    delta = from_high - to_low
    pst = 100 * delta / from_high

    fig.add_shape(
        type="rect",
        x0=from_date, y0=from_high, x1=to_date, y1=to_low,
        line=dict(
            color="Green",
            width=1,
            dash="dot",
        ),
        label=dict(
            text=f'-{pst:.2f}% <br> {delta:.2f}$ <br> {to_idx - from_idx}D',
            textposition="top center"
        ),
    )

    mid = (from_high + to_low) / 2

    fig.add_shape(
        type="line",
        x0=from_date, y0=mid, x1=to_date, y1=mid,
        line=dict(
            color="Green",
            width=0.5,
            dash="dot",
        )
    )


def up_analysis(fig, stock_data: pd.DataFrame):
    triggered_idx = []

    for idx, row in stock_data.iterrows():
        if row['local_min_3rd'] or (row['local_min_2nd'] and row['range_min_n']):
            triggered_idx.append(idx)

    triggered_idx.append(stock_data.index[-1])
    print(f"triggered up -> {triggered_idx}")

    for i in range(len(triggered_idx) - 1):
        start_idx, end_idx = triggered_idx[i], triggered_idx[i + 1]
        print(f'up -> {stock_data.loc[start_idx]["Date"]} ~ {stock_data.loc[end_idx]["Date"]}')

        highest_idx = start_idx
        for idx in range(start_idx + 1, end_idx):
            if stock_data.loc[idx]['high'] > stock_data.loc[highest_idx]['high']:
                highest_idx = idx

        if highest_idx - start_idx <= 9:
            continue
        add_up_box(fig, stock_data, start_idx, highest_idx)


def down_analysis(fig, stock_data: pd.DataFrame):
    triggered_idx = []

    for idx, row in stock_data.iterrows():
        if row['local_max_3rd'] or (row['local_max_2nd'] and row['range_max_n']):
            triggered_idx.append(idx)

    triggered_idx.append(stock_data.index[-1])
    print(f"triggered down -> {triggered_idx}")

    for i in range(len(triggered_idx) - 1):
        start_idx, end_idx = triggered_idx[i], triggered_idx[i + 1]
        print(f'down -> {stock_data.loc[start_idx]["Date"]} ~ {stock_data.loc[end_idx]["Date"]}')

        lowest_idx = start_idx
        for idx in range(start_idx + 1, end_idx):
            if stock_data.loc[idx]['low'] < stock_data.loc[lowest_idx]['low']:
                lowest_idx = idx

        if lowest_idx - start_idx <= 9:
            continue
        add_down_box(fig, stock_data, start_idx, lowest_idx)


def period_analysis(symbol, start_date, end_date):
    stock_data = load_data(symbol)
    stock_data = stock_data[(stock_data['Date'] > start_date) & (stock_data['Date'] < end_date)]
    # stock_data['Date'] = pd.to_datetime(stock_data['Date'])

    # calculate
    local_max_1st_rows = local_max(stock_data)
    local_max_2nd_rows = local_max(local_max_1st_rows)
    local_max_3rd_rows = local_max(local_max_2nd_rows)

    range_max_n_rows = range_max(stock_data, 15)

    local_min_1st_rows = local_min(stock_data)
    local_min_2nd_rows = local_min(local_min_1st_rows)
    local_min_3rd_rows = local_min(local_min_2nd_rows)

    range_min_n_rows = range_min(stock_data, 15)

    # merge
    add_column(stock_data, 'local_max_1st', local_max_1st_rows['Date'])
    add_column(stock_data, 'local_max_2nd', local_max_2nd_rows['Date'])
    add_column(stock_data, 'local_max_3rd', local_max_3rd_rows['Date'])
    add_column(stock_data, 'range_max_n', range_max_n_rows['Date'])

    add_column(stock_data, 'local_min_1st', local_min_1st_rows['Date'])
    add_column(stock_data, 'local_min_2nd', local_min_2nd_rows['Date'])
    add_column(stock_data, 'local_min_3rd', local_min_3rd_rows['Date'])
    add_column(stock_data, 'range_min_n', range_min_n_rows['Date'])

    # plot
    fig = go.Figure()
    add_candlestick(fig, stock_data)

    add_scatter(fig, stock_data, 'local_max_1st', 'high', 'red', 2)
    add_scatter(fig, stock_data, 'local_max_2nd', 'high', 'red', 6)
    add_scatter(fig, stock_data, 'local_max_3rd', 'high', 'red', 10)
    add_scatter(fig, stock_data, 'range_max_n', 'high', 'black', 4)

    add_scatter(fig, stock_data, 'local_min_1st', 'low', 'green', 2)
    add_scatter(fig, stock_data, 'local_min_2nd', 'low', 'green', 6)
    add_scatter(fig, stock_data, 'local_min_3rd', 'low', 'green', 10)
    add_scatter(fig, stock_data, 'range_min_n', 'low', 'blue', 4)

    up_analysis(fig, stock_data)
    down_analysis(fig, stock_data)

    fig.update_xaxes(
        rangebreaks=[
            dict(bounds=["sat", "mon"]),  # hide weekends
        ]
    )

    fig.show()

# TSLA MRNA MNSO
SYMBOL = "MRNA"
# fig = make_subplots(rows=3, cols=1)

# period_analysis(SYMBOL, '2024-01-01', '2024-05-31')
period_analysis(SYMBOL, '2023-01-01', '2024-05-31')
# period_analysis(SYMBOL, '2022-01-01', '2024-05-31')
# period_analysis(SYMBOL, '2021-01-01', '2024-05-41')
