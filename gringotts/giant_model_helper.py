import copy

import pandas as pd
import plotly.graph_objects as go

from features import FEATURE_BUF
from gringotts.tiny_model import TinyModel
from gringotts import RECALL_STEP, MARGIN


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


def serialize_models(stock_name: str, conf: dict,
                     long_models: list[TinyModel], short_models: list[TinyModel]):
    filename = f'train/{stock_name}_{conf[RECALL_STEP]}_{conf[MARGIN]}.txt'
    with open(filename, 'w') as f:
        for model in long_models:
            f.write(f'long\t{model.abbr}\t{model.successful_long_rate}% {model.valid_trade_num}\n')

        for model in short_models:
            f.write(f'short\t{model.abbr}\t{model.successful_short_rate}% {model.valid_trade_num}\n')


def deserialize_models(stock_name: str, conf: dict) -> tuple[list[list[bool]], list[list[bool]]]:
    long_switches, short_switches = [], []

    filename = f'train/{stock_name}_{conf[RECALL_STEP]}_{conf[MARGIN]}.txt'
    with open(filename, 'r') as f:
        for line in f:
            switch = [False] * len(FEATURE_BUF)

            fields = line.split('\t')
            parts = fields[1].split(',')

            for part in parts:
                switch[int(part)] = True

            if fields[0] == 'long':
                long_switches.append(switch)
            elif fields[0] == 'short':
                short_switches.append(switch)

    return long_switches, short_switches


def shrink_models(models: list[TinyModel]) -> list[TinyModel]:
    # shrink models with same indices, keep the one with shorter name
    results = {}

    for model in models:
        model_key = tuple(model.output_indices)

        if model_key not in results:
            results[model_key] = model
        else:
            if len(model.name) < len(results[model_key].name):
                results[model_key] = model

    results = list(results.values())
    results.sort(key=lambda m: m.valid_trade_num, reverse=True)
    return results


def show_models(stock_df: pd.DataFrame, fig: go.Figure,
                models: list[TinyModel], color: str, size: int = 8, enable=False):
    for model in models:
        indices = model.output_indices
        dates = stock_df.loc[indices]['Date']
        close = stock_df.loc[indices]['close']

        if color == 'orange':
            model_name = (f'{model.abbr}<br>{model.valid_trade_num:02}|{int(model.successful_long_rate)}%|'
                          f'+{model.expect_long_margin:.2f}%|-{model.expect_short_margin:.2f}%')
        else:
            model_name = (f'{model.abbr}<br>{model.valid_trade_num:02}|{int(model.successful_short_rate)}%|'
                          f'+{model.expect_short_margin:.2f}%|-{model.expect_long_margin:.2f}%')

        fig.add_trace(
            go.Scatter(
                name=f'{model_name}',
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
