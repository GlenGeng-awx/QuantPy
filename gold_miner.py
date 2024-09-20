import json
from datetime import datetime
from glob import glob

import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from base_engine import BaseEngine
from util import get_prev_n_workday, shrink_date_str
from playground import default_period, STOCK_NAMES_TIER_0, STOCK_NAMES_TIER_1, INDEX_NAMES

SCAN_DAYS = 20


# 20 stocks per graph
def setup_graph(stock_names: list[str]):
    rows = len(stock_names)

    fig = make_subplots(rows=rows, cols=1,
                        row_heights=[0.1] * rows,
                        subplot_titles=stock_names,
                        shared_xaxes=True,
                        vertical_spacing=0.02,
                        )

    fig.update_xaxes(
        rangebreaks=[
            dict(bounds=["sat", "mon"]),  # hide weekends
        ]
    )

    fig.update_layout(
        hovermode="x unified",
        height=150 * rows
    )

    return fig


# scan last 20 days
def calculate_hit_stats(stock_name) -> tuple[int, int, dict]:
    base_engine = BaseEngine(stock_name, *default_period())
    stock_df = base_engine.stock_df

    today = datetime.now().strftime('%Y-%m-%d')
    watermark = get_prev_n_workday(today, SCAN_DAYS)

    total_rule_num = 0
    total_hit_num = 0

    # date -> long/short -> hit_num
    hit_stats = {}

    for date in pd.bdate_range(end=today, periods=SCAN_DAYS + 1):
        date = date.strftime('%Y-%m-%d')
        hit_stats[date] = {'long': 0, 'short': 0}

    for filename in glob(f'./storage/predict/{stock_name}*.txt'):
        with open(filename) as fd:
            for line in fd:
                total_rule_num += 1

                fields = line.strip().split('\t')
                direction = fields[0]
                indices = eval(fields[4])

                for idx in indices:
                    date = shrink_date_str(stock_df.loc[idx]['Date'])
                    if date < watermark:
                        continue

                    total_hit_num += 1
                    hit_stats[date][direction] += 1

    return total_rule_num, total_hit_num, hit_stats


def plot_hit_stats(hit_stats: dict, fig: go.Figure, row: int):
    hit_stats = list(hit_stats.items())
    hit_stats.sort(key=lambda x: x[0])

    dates = [x[0] for x in hit_stats]
    longs = [x[1]['long'] for x in hit_stats]
    shorts = [x[1]['short'] for x in hit_stats]

    fig.add_trace(go.Bar(x=dates, y=longs, name='long', marker_color='red'), row=row, col=1)
    fig.add_trace(go.Bar(x=dates, y=shorts, name='short', marker_color='green'), row=row, col=1)


if __name__ == '__main__':
    all_names = STOCK_NAMES_TIER_0 + STOCK_NAMES_TIER_1

    curr = 0
    step = 20

    while curr < len(all_names):
        print(f'Processing {curr} to {curr + step - 1}')
        sub_names = all_names[curr:curr + step]

        fig = setup_graph(sub_names)

        for row, stock_name in enumerate(sub_names):
            total_rule_num, total_hit_num, hit_stats = calculate_hit_stats(stock_name)
            plot_hit_stats(hit_stats, fig, row + 1)

            print(f'{stock_name} -> total_rule_num: {total_rule_num}')
            print(f'{stock_name} -> total_hit_num: {total_hit_num}')
            print(f'{stock_name} -> hit stats for : {json.dumps(hit_stats, indent=4)}')

        fig.show()
        curr += step
