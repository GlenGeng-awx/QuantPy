import copy

import pandas as pd
import plotly.graph_objects as go
from gringotts.tiny_model import TinyModel


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
