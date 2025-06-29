import pandas as pd
import plotly.graph_objects as go
import json
from util import get_idx_by_date
from guru.train import interpolate_context, get_15d_10pst_up, get_15d_10pst_down


def target_dates(stock_df: pd.DataFrame):
    return {stock_df['Date'].iloc[i] for i in range(-4, 0)}


def predict(stock_df: pd.DataFrame, fig: go.Figure, stock_name: str, context: dict) -> bool:
    up_pst, _ = get_15d_10pst_up(stock_df)
    down_pst, _ = get_15d_10pst_down(stock_df)
    context = interpolate_context(stock_df, context)

    title = f'{fig.layout.title.text}, up: {up_pst:.2%}, down: {down_pst:.2%}'
    fig.update_layout(title=title)

    hit = False
    with open(f'tmp/{stock_name}.txt', 'r') as fd:
        for line in fd:
            keys, tag = line.strip().split('\t')
            keys = json.loads(keys)

            dates = set.intersection(*(context[key] for key in keys if key in context))

            if not dates.intersection(target_dates(stock_df)):
                continue

            hit = True
            print(f'Found a hit for {stock_name} with keys {keys} and tag {tag}')

            indices = [get_idx_by_date(stock_df, date) for date in dates]
            fig.add_trace(
                go.Scatter(
                    name='<br>'.join(keys + [tag]),
                    x=[stock_df.loc[idx]['Date'] for idx in indices],
                    y=[stock_df.loc[idx]['close'] for idx in indices],
                    mode='markers',
                    marker=dict(size=5, color='red'),
                ),
            )

    return hit
