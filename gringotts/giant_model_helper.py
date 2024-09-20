import copy

import pandas as pd
import plotly.graph_objects as go

from features import FEATURE_BUF
from gringotts.tiny_model import TinyModel
from gringotts import RECALL_STEP, FORECAST_STEP, MARGIN, HIT_THRESHOLD, MODE


def enumerate_switches(size: int) -> list[list[bool]]:
    if size == 0:
        return [[]]

    switches_part1 = enumerate_switches(size - 1)
    switches_part2 = copy.deepcopy(switches_part1)

    for switch in switches_part1:
        switch.insert(0, False)

    for switch in switches_part2:
        switch.insert(0, True)

    return switches_part1 + switches_part2


def default_switch(size: int) -> list[bool]:
    return [False] * size


# long/short \t switch \t evaluators \t switch name \t indices
def serialize_models(stock_name: str, conf: dict,
                     long_models: list[TinyModel], short_models: list[TinyModel]):
    if conf[MODE] == 'train':
        filename = f'./storage/train/{stock_name}_{conf[RECALL_STEP]}d.txt'
    else:
        filename = f'./storage/predict/{stock_name}_{conf[RECALL_STEP]}d_{conf[MARGIN]:.2f}_{conf[HIT_THRESHOLD]}.txt'

    with open(filename, 'w') as f:
        for model in long_models:
            f.write(f'long\t{model.filter.abbr()}\t{model.name()}\t{model.filter.output_indices}\n')

        for model in short_models:
            f.write(f'short\t{model.filter.abbr()}\t{model.name()}\t{model.filter.output_indices}\n')


def deserialize_models(stock_name: str, conf: dict) -> tuple[list[list[bool]], list[list[bool]]]:
    # which file to go
    recall_step = conf[RECALL_STEP]

    # which evaluator to pick
    forecast_step = conf[FORECAST_STEP]
    margin = conf[MARGIN]
    hit_threshold = conf[HIT_THRESHOLD]

    long_switches, short_switches = [], []

    filename = f'./storage/train/{stock_name}_{recall_step}d.txt'
    with open(filename, 'r') as f:
        for line in f:
            # long '\t' 16,33 '\t' L 5d 1.0% 8|17 82%;L 5d 3.0% 8|17 82% '\t' up thru r level, short red bar \t indices
            fields = line.split('\t')

            direction = fields[0]

            # 16,33
            parts = fields[1].split(',')
            switch = [False] * len(FEATURE_BUF)
            for part in parts:
                switch[int(part)] = True

            hit = False
            evaluators = fields[2].split(';')
            for evaluator in evaluators:
                # L 5d 1.0% 8
                evaluator_conf = evaluator.split('|')[0].split(' ')
                if evaluator_conf[1] == f'{forecast_step}d' \
                        and evaluator_conf[2] == f'{margin * 100:.1f}%' \
                        and evaluator_conf[3] == f'{hit_threshold}':
                    hit = True
                    break

            if not hit:
                continue

            if direction == 'long':
                long_switches.append(switch)
            elif direction == 'short':
                short_switches.append(switch)

    return long_switches, short_switches


def shrink_models(models: list[TinyModel]) -> list[TinyModel]:
    # shrink models with same indices, keep the one with shorter name
    results = {}

    for model in models:
        model_key = tuple(model.filter.output_indices)

        if model_key not in results:
            results[model_key] = model
        else:
            if len(model.filter.abbr()) < len(results[model_key].filter.abbr()):
                results[model_key] = model

    results = list(results.values())
    results.sort(key=lambda m: len(m.filter.output_indices), reverse=True)
    return results


def show_models(stock_df: pd.DataFrame, fig: go.Figure,
                models: list[TinyModel], color: str, size: int = 8, enable=False):
    for model in models:
        indices = model.filter.output_indices
        dates = stock_df.loc[indices]['Date']
        close = stock_df.loc[indices]['close']

        fig.add_trace(
            go.Scatter(
                name=f'{model.label()}',
                x=dates,
                y=close,
                mode='markers',
                marker=dict(size=size, color=color),
                visible=None if enable else 'legendonly',
            )
        )


if __name__ == '__main__':
    for switch in enumerate_switches(4):
        print(switch)
