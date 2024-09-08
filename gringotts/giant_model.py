import copy
from datetime import datetime
from multiprocessing import Process, Queue

import pandas as pd
import plotly.graph_objects as go

from features import FEATURE_BUF
from gringotts.tiny_model import TinyModel


def enumerate_switches(size: int) -> list[list[bool]]:
    if size == 0:
        return [[]]

    switches_part1 = enumerate_switches(size - 1)
    switches_part2 = copy.deepcopy(switches_part1)

    for switch in switches_part1:
        switch.append(False)

    for switch in switches_part2:
        switch.append(True)

    return switches_part1 + switches_part2


def serialize_models(stock_name: str, long_models: list[TinyModel], short_models: list[TinyModel]):
    with open(f'train/{stock_name}.txt', 'w') as f:
        for model in long_models:
            f.write(f'long\t{model.abbr}\t{model.successful_long_rate}% {len(model.indices)}\n')

        for model in short_models:
            f.write(f'short\t{model.abbr}\t{model.successful_short_rate}% {len(model.indices)}\n')


def deserialize_models(stock_name: str) -> tuple[list[list[bool]], list[list[bool]]]:
    long_switches, short_switches = [], []

    with open(f'train/{stock_name}.txt', 'r') as f:
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


def giant_model_worker(stock_df: pd.DataFrame, stock_name: str,
                       worker_id: int, switches: list[list[bool]], queue: Queue):
    worker_tag = f'{stock_name} worker {worker_id}'
    long_models = []
    short_models = []

    for i, switch in enumerate(switches):
        model = TinyModel(stock_df, switch)
        model.run()

        if model.successful_long_rate >= 80 and len(model.indices) >= 2:
            print(f'{worker_tag} {i + 1}/{len(switches)} --> long '
                  f'{model.successful_long_rate}% among {len(model.indices)} with {model.name}')
            long_models.append(model)

        if model.successful_short_rate >= 80 and len(model.indices) >= 2:
            print(f'{worker_tag} {i + 1}/{len(switches)} --> short '
                  f'{model.successful_short_rate}% among {len(model.indices)} with {model.name}')
            short_models.append(model)

        if (i + 1) % 10_000 == 0:
            print(f'{worker_tag} {i + 1}/{len(switches)} --> progress {datetime.now().time()}')
            # break

    queue.put((long_models, short_models))
    print(f'{worker_tag} finished at {datetime.now().time()}, '
          f'return {len(long_models)} long models and {len(short_models)} short models')


class GiantModel:
    def __init__(self, stock_df: pd.DataFrame, stock_name: str, mode: str = 'train'):
        self.stock_df = stock_df
        self.stock_name = stock_name
        self.mode = mode

        self.long_models = []
        self.short_models = []

    def run(self):
        if self.mode == 'train':
            self._train()
        else:
            self._predict()

    def _train(self):
        switches = enumerate_switches(len(FEATURE_BUF))

        worker_num = 16
        assert len(switches) % worker_num == 0
        batch_size = len(switches) // worker_num

        queue = Queue()
        procs = []

        for i in range(worker_num):
            start = i * batch_size
            end = (i + 1) * batch_size
            proc = Process(target=giant_model_worker,
                           args=(self.stock_df, self.stock_name, i, switches[start:end], queue))
            proc.start()
            procs.append(proc)

        # for proc in procs:
        #     print(f'waiting for {proc.pid} to join')
        #     proc.join()

        for _ in procs:
            long_models, short_models = queue.get()
            print(f'got {len(long_models)} long models and {len(short_models)} short models')
            self.long_models.extend(long_models)
            self.short_models.extend(short_models)

        self.long_models = shrink_models(self.long_models)
        self.short_models = shrink_models(self.short_models)

        serialize_models(self.stock_name, self.long_models, self.short_models)

    def _predict(self):
        long_switches, short_switches = deserialize_models(self.stock_name)

        for switch in long_switches:
            model = TinyModel(self.stock_df, switch)
            model.run()
            self.long_models.append(model)

        for switch in short_switches:
            model = TinyModel(self.stock_df, switch)
            model.run()
            self.short_models.append(model)

    def build_graph(self, fig: go.Figure):
        show_models(self.stock_df, fig, self.long_models, 'orange')
        show_models(self.stock_df, fig, self.short_models, 'blue')
