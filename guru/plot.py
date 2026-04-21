import pandas as pd
import plotly.graph_objects as go


def summarize(stock_df: pd.DataFrame) -> str:
    close = stock_df['close']
    sz = 15

    box_psts = []
    incr_psts = []
    decr_psts = []

    for idx in stock_df.index[-200:]:
        max_close = close.loc[idx - sz + 1:idx].max()
        min_close = close.loc[idx - sz + 1:idx].min()
        box_pst = (max_close - min_close) / min_close
        box_psts.append(box_pst)

        if close[idx] >= close[idx - sz]:
            incr_pst = (close[idx] - close[idx - sz]) / close[idx - sz]
            incr_psts.append(incr_pst)
        else:
            decr_pst = (close[idx - sz] - close[idx]) / close[idx - sz]
            decr_psts.append(decr_pst)

    box_psts.sort()
    box_10 = box_psts[int(len(box_psts) * 0.1)]
    box_20 = box_psts[int(len(box_psts) * 0.2)]

    incr_psts.sort(reverse=True)
    incr_10 = incr_psts[int(len(incr_psts) * 0.1)]
    incr_20 = incr_psts[int(len(incr_psts) * 0.2)]

    decr_psts.sort(reverse=True)
    decr_10 = decr_psts[int(len(decr_psts) * 0.1)]
    decr_20 = decr_psts[int(len(decr_psts) * 0.2)]

    summary = f'box 10/20: {box_10:.2%}/{box_20:.2%}, ' \
              f'spike 10/20: {incr_10:.2%}/{incr_20:.2%}, ' \
              f'crash 10/20: {decr_10:.2%}/{decr_20:.2%}'
    return summary


def _get_color(key: str) -> str:
    from guru import factors
    for f in factors:
        if f.KEY == key:
            return f.COLOR
    return 'black'


# Sort by color (red -> black -> green), then by factor order within each color.
def _sorted_keys(context: dict) -> list:
    from guru import factors
    order = {f.KEY: idx for idx, f in enumerate(factors)}
    color_priority = {'red': 0, 'black': 1, 'green': 2}
    keys = [k for k in context if k in order]
    keys.sort(key=lambda k: (color_priority.get(_get_color(k), 1), order[k]))
    return keys


def plot(stock_df: pd.DataFrame, fig: go.Figure, context: dict, row=2) -> dict:
    for i, key in enumerate(_sorted_keys(context)):
        dates = context[key]
        color = _get_color(key)
        fig.add_trace(
            go.Scatter(
                name=key,
                x=dates,
                y=[1 * (i + 1)] * len(dates),
                mode='markers', marker=dict(size=4, color=color),
            ),
            row=row, col=1
        )

    summary = summarize(stock_df)
    fig.update_layout(title=f"{fig.layout.title.text}<br>{' ' * 20}{summary}")
    return context
