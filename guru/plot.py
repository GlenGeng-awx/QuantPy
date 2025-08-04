import pandas as pd
import plotly.graph_objects as go


def summarize(stock_df: pd.DataFrame) -> str:
    close = stock_df['close']
    sz = 15

    decr_psts, incr_psts = [], []

    for idx in stock_df.index[-200:]:
        if close[idx] >= close[idx - sz]:
            incr_pst = (close[idx] - close[idx - sz]) / close[idx - sz]
            incr_psts.append(incr_pst)
        else:
            decr_pst = (close[idx - sz] - close[idx]) / close[idx - sz]
            decr_psts.append(decr_pst)

    incr_psts.sort()
    incr_days = len(incr_psts)
    incr_10 = incr_psts[int(incr_days * 0.1)]
    incr_50 = incr_psts[int(incr_days * 0.5)]
    incr_90 = incr_psts[int(incr_days * 0.9)]

    decr_psts.sort()
    decr_days = len(decr_psts)
    decr_10 = decr_psts[int(decr_days * 0.1)]
    decr_50 = decr_psts[int(decr_days * 0.5)]
    decr_90 = decr_psts[int(decr_days * 0.9)]

    summary = f'incr {incr_days}d, 10/50/90: {incr_10:.2%}/{incr_50:.2%}/{incr_90:.2%}, ' \
              f'decr {decr_days}d, 10/50/90: {decr_10:.2%}/{decr_50:.2%}/{decr_90:.2%}'
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
