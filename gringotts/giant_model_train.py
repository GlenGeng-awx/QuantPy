import pandas as pd
from datetime import datetime
from multiprocessing import Queue

from features import FEATURE_BUF
from gringotts import FORECAST_STEP, MARGIN, HIT_THRESHOLD
from gringotts.tiny_model import TinyModel
from gringotts.giant_model_helper import default_switch


def get_train_context(stock_df: pd.DataFrame, evaluators: list[dict]) -> dict:
    context = {}
    close = stock_df['close']

    for idx in stock_df.index:
        context[idx] = {}

        # for filter
        for feature in FEATURE_BUF:
            key = feature.KEY
            context[idx][key] = stock_df[key].loc[idx - feature.RECALL_DAYS + 1:idx].any()

        # for evaluator
        for evaluator in evaluators:
            forecast_step = evaluator[FORECAST_STEP]
            margin = evaluator[MARGIN]

            if idx + forecast_step not in close:
                continue

            max_close = close.loc[idx:idx + forecast_step].max()
            min_close = close.loc[idx:idx + forecast_step].min()

            context[idx][forecast_step] = {
                margin: {
                    'long': close[idx] * (1 + margin) < close[idx + forecast_step] and min_close > close[idx] * 0.97,
                    'short': close[idx] * (1 - margin) > close[idx + forecast_step] and max_close < close[idx] * 1.03,
                }
            }

    return context


# at leaf, do filter and evaluation
# at non-leaf, just do filter and decide to go or not go
# conf mode is training
def _model_searcher(stock_df: pd.DataFrame, conf: dict, worker_tag: str,
                    prefix: list[bool], left_len: int,
                    input_indices: list[int], train_ctx: dict) -> tuple[list[TinyModel], list[TinyModel]]:
    if left_len == 0:
        assert len(prefix) == len(FEATURE_BUF)

        model = TinyModel(stock_df, conf, prefix, input_indices, len(prefix) - 1, train_ctx)
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

        model = TinyModel(stock_df, conf, hint_switch, input_indices, len(prefix) - 1, train_ctx)
        model.phase1()

        min_hit_threshold = min(evaluator_conf[HIT_THRESHOLD] for evaluator_conf in conf['evaluators'])
        if len(model.filter.output_indices) < min_hit_threshold:
            return [], []

        long_models, short_models = [], []

        true_part = _model_searcher(stock_df, conf,
                                    worker_tag, prefix + [True], left_len - 1,
                                    model.filter.output_indices, train_ctx)
        long_models.extend(true_part[0])
        short_models.extend(true_part[1])

        false_part = _model_searcher(stock_df, conf,
                                     worker_tag, prefix + [False], left_len - 1,
                                     model.filter.output_indices, train_ctx)
        long_models.extend(false_part[0])
        short_models.extend(false_part[1])

        return long_models, short_models


# prepare to kick off _model_searcher
def giant_model_worker(stock_df: pd.DataFrame, stock_name: str, conf: dict, input_indices: list[int],
                       worker_id: int, prefixes: list[list[bool]], left_len, queue: Queue):
    worker_tag = f'{stock_name} - worker {worker_id}'
    prefix = prefixes[worker_id]
    print(f'{worker_tag} with {prefix} started at {datetime.now().time()}')

    start_time = datetime.now()
    train_ctx = get_train_context(stock_df, conf['evaluators'])

    long_models, short_models = _model_searcher(stock_df, conf, worker_tag, prefix, left_len, input_indices, train_ctx)
    queue.put((long_models, short_models))

    end_time = datetime.now()
    time_cost = (end_time - start_time).total_seconds()
    print(f'{worker_tag} with {prefix} finished at {end_time.time()}, cost {time_cost}s, '
          f'return {len(long_models)} long models and {len(short_models)} short models')
