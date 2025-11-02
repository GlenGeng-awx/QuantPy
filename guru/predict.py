import pandas as pd
import plotly.graph_objects as go
import json
from util import get_idx_by_date
from guru.train import interpolate_context, get_file_name
from guru_wizard import get_train_mode
import re


# 4: 4
# 5: 5, 4
# 6: 6, 5
# 7: 7, 6, 5
# 8: 8, 7, 6
# 9: 9, 8, 7
# 10: 90%, 80%, 70%
def pick_line(line, predict_mode) -> bool:
    match = re.search(r'total (\d+), hit (\d+)', line)
    total, hit = map(int, match.groups())

    _months, _total, _hit = re.findall(r'\d+', predict_mode)
    _total, _hit = int(_total), int(_hit)

    if (_total, _hit) in [
        (4, 4),
        (5, 5), (5, 4),
        (6, 6), (6, 5),
        (7, 7), (7, 6), (7, 5),
        (8, 8), (8, 7), (8, 6),
        (9, 9), (9, 8), (9, 7),
    ]:
        return total == _total and hit == _hit

    if (_total, _hit) == (10, 9):
        return total >= 10 and hit / total >= 0.9

    if (_total, _hit) == (10, 8):
        return total >= 10 and 0.9 > hit / total >= 0.8

    if (_total, _hit) == (10, 7):
        return total >= 10 and 0.8 > hit / total >= 0.7

    return False


def target_dates(stock_df: pd.DataFrame):
    return {stock_df['Date'].iloc[i] for i in range(-1, 0)}


# for efficiency, context is already interpolated
def predict(stock_df: pd.DataFrame, fig, stock_name: str, context: dict,
            predict_mode: str, model_name: str) -> bool:
    train_mode = get_train_mode(predict_mode)
    file_name = get_file_name(stock_name, stock_df, train_mode, model_name)

    hit = False
    with open(file_name, 'r') as fd:
        for line in fd:
            if not pick_line(line, predict_mode):
                continue

            keys, tag = line.strip().split('\t')
            keys = json.loads(keys)

            dates = set.intersection(*(context[key] for key in keys if key in context))

            if not dates.intersection(target_dates(stock_df)):
                continue

            hit = True
            print(f'Found a hit for {stock_name} {model_name} with keys {keys} and tag {tag}')

            if fig is None:
                continue

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
