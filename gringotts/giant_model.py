from datetime import datetime
from multiprocessing import Process, Queue

import pandas as pd
import plotly.graph_objects as go

from features import FEATURE_BUF
import gringotts
from gringotts.tiny_model import TinyModel
from gringotts.giant_model_helper import (enumerate_switches, default_switch,
                                          serialize_models, deserialize_models,
                                          shrink_models, show_models)


def _model_searcher(stock_df: pd.DataFrame, worker_tag: str,
                    prefix: list[bool], left_len: int,
                    input_indices: list[int]) -> tuple[list[TinyModel], list[TinyModel]]:
    if left_len == 0:
        assert len(prefix) == len(FEATURE_BUF)

        success_rate = gringotts.SUCCESSFUL_RATE
        hit_threshold = gringotts.HIT_THRESHOLD

        model = TinyModel(stock_df, prefix, input_indices, len(prefix) - 1)
        model.run()

        long_models, short_models = [], []

        if model.successful_long_rate >= success_rate and len(model.output_indices) >= hit_threshold:
            print(f'{worker_tag} --> long {model.successful_long_rate}% '
                  f'among {len(model.output_indices)} with {model.name}')
            long_models.append(model)

        if model.successful_short_rate >= success_rate and len(model.output_indices) >= hit_threshold:
            print(f'{worker_tag} --> short {model.successful_short_rate}% '
                  f'among {len(model.output_indices)} with {model.name}')
            short_models.append(model)

        return long_models, short_models

    else:
        hint_switch = prefix + default_switch(left_len)
        assert len(hint_switch) == len(FEATURE_BUF)

        model = TinyModel(stock_df, hint_switch, input_indices, len(prefix) - 1)
        model.run()

        if len(model.output_indices) < gringotts.HIT_THRESHOLD:
            # print(f'{worker_tag} prune {2 ** left_len} models for {prefix}')
            return [], []

        long_models, short_models = [], []

        true_part = _model_searcher(stock_df,worker_tag, prefix + [True], left_len - 1, model.output_indices)
        long_models.extend(true_part[0])
        short_models.extend(true_part[1])

        false_part = _model_searcher(stock_df, worker_tag, prefix + [False], left_len - 1, model.output_indices)
        long_models.extend(false_part[0])
        short_models.extend(false_part[1])

        return long_models, short_models


def giant_model_worker(stock_df: pd.DataFrame, stock_name: str, worker_id: int,
                       prefixes: list[list[bool]], left_len, queue: Queue):
    worker_tag = f'{stock_name} worker {worker_id}'
    prefix = prefixes[worker_id]
    print(f'{worker_tag} with {prefix} started at {datetime.now().time()}')

    start_time = datetime.now()

    long_models, short_models = _model_searcher(stock_df, worker_tag, prefix, left_len, stock_df.index.tolist())
    queue.put((long_models, short_models))

    end_time = datetime.now()
    time_cost = (end_time - start_time).total_seconds()
    print(f'{worker_tag} with {prefix} finished at {end_time.time()}, cost {time_cost}s, '
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
        mask = gringotts.MASK
        switches = enumerate_switches(mask)

        queue = Queue()
        procs = []

        for worker_id in range(2 ** mask):
            proc = Process(
                target=giant_model_worker,
                args=(self.stock_df, self.stock_name, worker_id, switches, len(FEATURE_BUF) - mask, queue))
            proc.start()
            procs.append(proc)

        for _ in procs:
            long_models, short_models = queue.get()
            # print(f'got {len(long_models)} long models and {len(short_models)} short models')
            self.long_models.extend(long_models)
            self.short_models.extend(short_models)

        self.long_models = shrink_models(self.long_models)
        self.short_models = shrink_models(self.short_models)

        serialize_models(self.stock_name, self.long_models, self.short_models)

    def _predict(self):
        long_switches, short_switches = deserialize_models(self.stock_name)

        for switch in long_switches:
            model = TinyModel(self.stock_df, switch, self.stock_df.index.tolist())
            model.run()
            self.long_models.append(model)

        for switch in short_switches:
            model = TinyModel(self.stock_df, switch, self.stock_df.index.tolist())
            model.run()
            self.short_models.append(model)

    def build_graph(self, fig: go.Figure, enable=False):
        show_models(self.stock_df, fig, self.long_models, 'orange', 9, enable)
        show_models(self.stock_df, fig, self.short_models, 'black', 7, enable)
