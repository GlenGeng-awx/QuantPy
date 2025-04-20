import pandas as pd
import plotly.graph_objects as go


# list of (idx, pst)
def filter_up_gaps(stock_df: pd.DataFrame) -> list:
    close, high, low = stock_df['close'], stock_df['high'], stock_df['low']

    up_gaps = []
    for idx in stock_df.index[1:]:
        if close[idx] > close[idx - 1] and low[idx] > high[idx - 1]:
            pst = (low[idx] - high[idx - 1]) / close[idx - 1]
            up_gaps.append((idx, pst))

    up_gaps.sort(key=lambda x: x[1], reverse=True)
    # print(f'up gaps {up_gaps}')

    reserved = min(stock_df.shape[0] // 100, len(up_gaps) // 5)
    return up_gaps[:reserved]


# list of (idx, pst)
def filter_down_gaps(stock_df: pd.DataFrame) -> list:
    close, high, low = stock_df['close'], stock_df['high'], stock_df['low']

    down_gaps = []
    for idx in stock_df.index[1:]:
        if close[idx] < close[idx - 1] and high[idx] < low[idx - 1]:
            pst = (low[idx - 1] - high[idx]) / close[idx - 1]
            down_gaps.append((idx, pst))

    down_gaps.sort(key=lambda x: x[1], reverse=True)
    # print(f'down gaps {down_gaps}')

    reserved = min(stock_df.shape[0] // 100, len(down_gaps) // 5)
    return down_gaps[:reserved]


class Gap:
    def __init__(self, stock_df: pd.DataFrame, stock_name: str):
        self.stock_df = stock_df
        self.stock_name = stock_name

        self.up_gaps = filter_up_gaps(stock_df)
        self.down_gaps = filter_down_gaps(stock_df)

        print(f'up gaps {stock_name}: {self.up_gaps}')
        print(f'down gaps {stock_name}: {self.down_gaps}')

    def build_graph(self, fig: go.Figure, enable=False):
        date, close = self.stock_df['Date'], self.stock_df['close']
        high, low = self.stock_df['high'], self.stock_df['low']

        up_x, up_y, up_text, hit_up = [], [], [], False
        for idx, pst in self.up_gaps:
            x = date[idx]
            y = low[idx] - (low[idx] - high[idx - 1]) * 0.5
            text = f'{pst:.2%}'

            up_x.append(x)
            up_y.append(y)
            up_text.append(text)

            if idx >= self.stock_df.index[-3]:
                hit_up = True

        down_x, down_y, down_text, hit_down = [], [], [], False
        for idx, pst in self.down_gaps:
            x = date[idx]
            y = high[idx] + (low[idx - 1] - high[idx]) * 0.5
            text = f'{pst:.2%}'

            down_x.append(x)
            down_y.append(y)
            down_text.append(text)

            if idx >= self.stock_df.index[-3]:
                hit_down = True

        fig.add_trace(
            go.Scatter(
                name='up gap',
                x=up_x, y=up_y, text=up_text,
                mode='text', textfont=dict(color="red", size=10),
                visible=None if enable and hit_up else 'legendonly',
            )
        )

        fig.add_trace(
            go.Scatter(
                name='down gap',
                x=down_x, y=down_y, text=down_text,
                mode='text', textfont=dict(color="green", size=10),
                visible=None if enable and hit_down else 'legendonly',
            )
        )
