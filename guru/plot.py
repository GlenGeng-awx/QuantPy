import pandas as pd
import plotly.graph_objects as go


def summarize(stock_df: pd.DataFrame) -> str:
    close = stock_df['close']
    sz = 15

    box_psts = []

    for idx in stock_df.index[-200:]:
        max_close = close.loc[idx - sz + 1:idx].max()
        min_close = close.loc[idx - sz + 1:idx].min()
        box_pst = (max_close - min_close) / min_close
        box_psts.append(box_pst)

    box_psts.sort()
    box_10 = box_psts[int(len(box_psts) * 0.1)]
    box_20 = box_psts[int(len(box_psts) * 0.2)]
    box_50 = box_psts[int(len(box_psts) * 0.5)]
    box_90 = box_psts[int(len(box_psts) * 0.9)]

    summary = f'box 10p: {box_10:.2%}, box 20p: {box_20:.2%}, box 50p: {box_50:.2%}, box 90p: {box_90:.2%}'
    return summary


def plot(stock_df: pd.DataFrame, fig: go.Figure, context: dict,
         row=2, display_last_n_days=None) -> dict:
    for i, (key, dates) in enumerate(context.items()):
        fig.add_trace(
            go.Scatter(
                name=key,
                x=dates,
                y=[1 * (i + 1)] * len(dates),  # Dummy y values for plotting
                mode='markers', marker=dict(size=4),
            ),
            row=row, col=1
        )

    if display_last_n_days is not None:
        fig.add_vline(
            x=stock_df['Date'].iloc[-display_last_n_days],
            line=dict(color='black', width=0.5, dash='dash'),
            row=row, col=1
        )

    summary = summarize(stock_df)
    fig.update_layout(title=f"{fig.layout.title.text}<br>{' ' * 20}{summary}")
    return context
