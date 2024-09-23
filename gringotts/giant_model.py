from datetime import datetime
from multiprocessing import Process, Queue

import pandas as pd
import plotly.graph_objects as go

from util import get_indices_of_period
from features import FEATURE_BUF
from gringotts import MODE, MASK, RECALL_STEP, FORECAST_STEP, MARGIN, HIT_THRESHOLD, FROM_DATE, TO_DATE
from gringotts.tiny_model import TinyModel
from gringotts.giant_model_helper import (enumerate_switches, default_switch,
                                          serialize_models, deserialize_models,
                                          shrink_models, show_models)


# at leaf, do filter and evaluation
# at non-leaf, just do filter and decide to go or not go
# conf mode is training
def _model_searcher(stock_df: pd.DataFrame, conf: dict, worker_tag: str,
                    prefix: list[bool], left_len: int,
                    input_indices: list[int]) -> tuple[list[TinyModel], list[TinyModel]]:
    if left_len == 0:
        assert len(prefix) == len(FEATURE_BUF)

        model = TinyModel(stock_df, conf, prefix, input_indices, len(prefix) - 1)
        model.phase1()
        model.phase2()  # time-consuming task

        long_models, short_models = [], []

        if model.pass_long() or model.pass_short():
            # print(f'{worker_tag} --> {model.name()}')
            pass

        if model.pass_long():
            long_models.append(model)

        if model.pass_short():
            short_models.append(model)

        return long_models, short_models

    else:
        hint_switch = prefix + default_switch(left_len)
        assert len(hint_switch) == len(FEATURE_BUF)

        model = TinyModel(stock_df, conf, hint_switch, input_indices, len(prefix) - 1)
        model.phase1()

        min_hit_threshold = min(evaluator_conf[HIT_THRESHOLD] for evaluator_conf in conf['evaluators'])
        if len(model.filter.output_indices) < min_hit_threshold:
            return [], []

        long_models, short_models = [], []

        true_part = _model_searcher(stock_df, conf, worker_tag,
                                    prefix + [True], left_len - 1, model.filter.output_indices)
        long_models.extend(true_part[0])
        short_models.extend(true_part[1])

        false_part = _model_searcher(stock_df, conf, worker_tag,
                                     prefix + [False], left_len - 1, model.filter.output_indices)
        long_models.extend(false_part[0])
        short_models.extend(false_part[1])

        return long_models, short_models


# prepare to kick off _model_searcher
def giant_model_worker(stock_df: pd.DataFrame, stock_name: str, conf: dict, input_indices: list[int],
                       worker_id: int, prefixes: list[list[bool]], left_len, queue: Queue):
    worker_tag = f'{stock_name} recall {conf[RECALL_STEP]}d - worker {worker_id}'
    prefix = prefixes[worker_id]
    print(f'{worker_tag} with {prefix} started at {datetime.now().time()}')

    start_time = datetime.now()

    long_models, short_models = _model_searcher(stock_df, conf, worker_tag, prefix, left_len, input_indices)
    queue.put((long_models, short_models))

    end_time = datetime.now()
    time_cost = (end_time - start_time).total_seconds()
    print(f'{worker_tag} with {prefix} finished at {end_time.time()}, cost {time_cost}s, '
          f'return {len(long_models)} long models and {len(short_models)} short models')


# during train, for one recall step, handle multiple coarse evaluators in a multiprocess way
# during predict, for one recall step, handle one fine evaluator deserializing from file
class GiantModel:
    def __init__(self, stock_df: pd.DataFrame, stock_name: str, conf: dict):
        self.stock_df = stock_df
        self.stock_name = stock_name
        self.conf = conf

        from_idx, to_idx = get_indices_of_period(stock_df, conf[FROM_DATE], conf[TO_DATE])
        self.input_indices = stock_df.loc[from_idx:to_idx].index.tolist()

        self.long_models = []
        self.short_models = []

    def run(self):
        if self.conf[MODE] == 'train':
            self._train()
        else:
            self._predict()

    def _train(self):
        mask = self.conf[MASK]
        switches = enumerate_switches(mask)

        queue = Queue()
        procs = []

        for worker_id in range(2 ** mask):
            proc = Process(
                target=giant_model_worker,
                args=(self.stock_df, self.stock_name, self.conf, self.input_indices,
                      worker_id, switches, len(FEATURE_BUF) - mask, queue))
            proc.start()
            procs.append(proc)

        for _ in procs:
            long_models, short_models = queue.get()
            # print(f'got {len(long_models)} long models and {len(short_models)} short models')
            self.long_models.extend(long_models)
            self.short_models.extend(short_models)

        self.long_models = shrink_models(self.long_models)
        self.short_models = shrink_models(self.short_models)

        # to train dir
        serialize_models(self.stock_name, self.conf, self.long_models, self.short_models)

    def _predict(self):
        long_switches, short_switches = deserialize_models(self.stock_name, self.conf)

        for switch in long_switches:
            model = TinyModel(self.stock_df, self.conf, switch, self.input_indices)
            model.phase1()
            model.phase2()
            self.long_models.append(model)

        for switch in short_switches:
            model = TinyModel(self.stock_df, self.conf, switch, self.input_indices)
            model.phase1()
            model.phase2()
            self.short_models.append(model)

        # to predict dir
        serialize_models(self.stock_name, self.conf, self.long_models, self.short_models)

    def need_attention(self) -> bool:
        return any(model.filter.output_indices for model in self.long_models + self.short_models)

    def build_graph(self, fig: go.Figure, enable=False):
        origin_title = fig.layout.title.text

        strategy_name = f'{self.conf[MODE]} << recall {self.conf[RECALL_STEP]}d >> '
        strategy_name += f'[{self.conf[FROM_DATE]}, {self.conf[TO_DATE]}] '

        if self.conf[MODE] == 'predict':
            strategy_name += f'(forecast {self.conf[FORECAST_STEP]}d, ' + \
                             f'{self.conf[MARGIN] * 100:.1f}%, {self.conf[HIT_THRESHOLD]})'

        fig.update_layout(title=f'{origin_title}<br>{strategy_name}')

        fig.add_vline(x=self.conf[FROM_DATE], line_dash="dash", line_width=0.5, line_color='red', row=1)
        fig.add_vline(x=self.conf[TO_DATE], line_dash="dash", line_width=0.5, line_color='red', row=1)

        show_models(self.stock_df, fig, self.long_models, 'orange', 7, enable)
        show_models(self.stock_df, fig, self.short_models, 'black', 5, enable)
