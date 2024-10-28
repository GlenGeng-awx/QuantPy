import pandas as pd
import plotly.graph_objects as go

from features import FEATURE_BUF
from gringotts.tiny_model import TinyModel
from gringotts import (FORECAST_STEP, MARGIN, HIT_THRESHOLD, MODE, FROM_DATE, TO_DATE,
                       TRAIN_FROM_DATE, TRAIN_TO_DATE, PREDICT_FROM_DATE, PREDICT_TO_DATE)


def get_ser_file(stock_name: str, conf: dict) -> str:
    if conf[MODE] == 'train':
        return f'./tmp/train/{stock_name}_{conf[FROM_DATE]}_{conf[TO_DATE]}.txt'

    if conf[MODE] == 'predict':
        return f'./tmp/predict/{stock_name}_f{conf[FORECAST_STEP]}d' \
               f'_{conf[MARGIN]:.2f}_{conf[HIT_THRESHOLD]}_{conf[FROM_DATE]}_{conf[TO_DATE]}.txt'

    raise ValueError(f'invalid mode: {conf[MODE]}')


def get_de_file(stock_name: str, conf: dict) -> str:
    if conf[MODE] == 'predict':
        # predict use train
        return f'./tmp/train/{stock_name}_{conf[TRAIN_FROM_DATE]}_{conf[TRAIN_TO_DATE]}.txt'

    if conf[MODE] == 'dev':
        # dev use predict
        return f'./tmp/predict/{stock_name}_f{conf[FORECAST_STEP]}d' \
               f'_{conf[MARGIN]:.2f}_{conf[HIT_THRESHOLD]}_{conf[PREDICT_FROM_DATE]}_{conf[PREDICT_TO_DATE]}.txt'

    raise ValueError(f'invalid mode: {conf[MODE]}')


# long/short \t switch \t evaluators \t switch name \t indices
def serialize_models(stock_name: str, conf: dict,
                     long_models: list[TinyModel], short_models: list[TinyModel]):
    filename = get_ser_file(stock_name, conf)
    print(f'serialize to {filename}')

    with open(filename, 'w') as f:
        for model in long_models:
            if not model.filter.output_indices:
                continue
            f.write(f'long\t{",".join(model.filter.abbr())}\t{model.name()}\t{model.filter.output_indices}\n')

        for model in short_models:
            if not model.filter.output_indices:
                continue
            f.write(f'short\t{",".join(model.filter.abbr())}\t{model.name()}\t{model.filter.output_indices}\n')


def deserialize_models(stock_name: str, conf: dict) -> tuple[list[list[bool]], list[list[bool]]]:
    filename = get_de_file(stock_name, conf)
    print(f'deserialize from {filename}')

    # which evaluator to pick
    forecast_step = conf[FORECAST_STEP]
    margin = conf[MARGIN]
    hit_threshold = conf[HIT_THRESHOLD]

    long_switches, short_switches = [], []
    with open(filename, 'r') as f:
        for line in f:
            # long '\t' 16,33 '\t' L 5d 1.0% 8|17 82%;L 5d 3.0% 8|17 82% '\t' up thru r level, short red bar \t indices
            # long '\t' 12,21 '\t' N 5d 4.0% 3<br>00 L 0% S 0%<br>EXP +0.0% -0.0% '\t' rsi above 70, incr 20 pst in last 10d, short green bar '\t' indices
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
                # L 5d 4.0% 3|13 92%
                # N 5d 4.0% 3<br>00 L 0% S 0%<br>EXP +0.0% -0.0%
                sep = '|' if conf[MODE] == 'predict' else '<br>'
                evaluator_conf = evaluator.split(sep)[0].split(' ')

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
