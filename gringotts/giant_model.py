import copy
from datetime import datetime
import pandas as pd
import plotly.graph_objects as go

from features import FEATURE_BUF


class TinyModel:
    def __init__(self, stock_df: pd.DataFrame, switch: list[bool]):
        self.stock_df = stock_df

        self.switch = switch
        self.abbr = ', '.join([str(i) for i in range(len(switch)) if switch[i]])
        self.name = ', '.join([feature.KEY for i, feature in enumerate(FEATURE_BUF) if switch[i]])

        self.indices = []

        self.successful_long_trades = 0
        self.successful_long_rate = 0

        self.successful_short_trades = 0
        self.successful_short_rate = 0

    def check(self, idx) -> bool:
        for i, feature in enumerate(FEATURE_BUF):
            if self.switch[i] and not self.stock_df[feature.KEY][idx]:
                return False
        return True

    def run(self):
        for idx in self.stock_df.index:
            if self.check(idx):
                self.indices.append(idx)

        # evaluate the model
        valid_trade_num = 0
        step = 5
        close = self.stock_df['close']

        for idx in self.indices:
            if idx + step in close:
                valid_trade_num += 1
            else:
                continue

            if close[idx] < close[idx + step]:
                self.successful_long_trades += 1

            if close[idx] > close[idx + step]:
                self.successful_short_trades += 1

        if valid_trade_num == 0:
            return

        self.successful_long_rate = self.successful_long_trades / valid_trade_num * 100
        self.successful_short_rate = self.successful_short_trades / valid_trade_num * 100


def enumerate_switches(size: int) -> list[list]:
    if size == 0:
        return [[]]

    switches_part1 = enumerate_switches(size - 1)
    switches_part2 = copy.deepcopy(switches_part1)

    for switch in switches_part1:
        switch.append(False)

    for switch in switches_part2:
        switch.append(True)

    return switches_part1 + switches_part2


def shrink_models(models: list[TinyModel]) -> list[TinyModel]:
    # shrink models with same indices, keep the one with shorter name
    results = {}

    for model in models:
        model_key = tuple(model.indices)

        if model_key not in results:
            results[model_key] = model
        else:
            if len(model.name) < len(results[model_key].name):
                results[model_key] = model

    results = list(results.values())
    results.sort(key=lambda m: len(m.indices), reverse=True)
    return results


def show_models(stock_df: pd.DataFrame, fig: go.Figure, models: list[TinyModel], color: str):
    for model in models[:15]:
        indices = model.indices
        dates = stock_df.loc[indices]['Date']
        close = stock_df.loc[indices]['close']

        fig.add_trace(
            go.Scatter(
                name=f'{model.abbr}',
                x=dates,
                y=close,
                mode='markers',
                marker=dict(size=8, color=color),
                visible='legendonly',
            )
        )


class GiantModel:
    def __init__(self, stock_df: pd.DataFrame, stock_name: str):
        self.stock_df = stock_df
        self.stock_name = stock_name

        self.long_models = []
        self.short_models = []

    def run(self):
        switches = enumerate_switches(len(FEATURE_BUF))

        for i, switch in enumerate(switches):
            model = TinyModel(self.stock_df, switch)
            model.run()

            if model.successful_long_rate >= 80 and len(model.indices) >= 2:
                print(f'{self.stock_name} {i + 1}/{len(switches)} --> long\t'
                      f'{model.successful_long_rate}% among {len(model.indices)} with {model.name}')
                self.long_models.append(model)

            if model.successful_short_rate >= 80 and len(model.indices) >= 2:
                print(f'{self.stock_name} {i + 1}/{len(switches)} --> short\t'
                      f'{model.successful_short_rate}% among {len(model.indices)} with {model.name}')
                self.short_models.append(model)

            if (i + 1) % 10_000 == 0:
                print(f'{self.stock_name} {i + 1}/{len(switches)}\t{datetime.now().time()}')
                # break

    def build_graph(self, fig: go.Figure):
        self.long_models = shrink_models(self.long_models)
        self.short_models = shrink_models(self.short_models)

        show_models(self.stock_df, fig, self.long_models, 'orange')
        show_models(self.stock_df, fig, self.short_models, 'blue')


if __name__ == '__main__':
    abbrs = [
        [2, 4, 6],
    ]

    for abbr in abbrs:
        print(abbr, ' / '.join([FEATURE_BUF[i].KEY for i in abbr]))
