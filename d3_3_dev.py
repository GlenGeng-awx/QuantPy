import pandas as pd
import plotly.graph_objects as go

from gringotts import FORECAST_STEP
from gringotts.giant_model import GiantModel

from d1_1_preload import preload
from d3_0_giant_model_proxy import get_predict_partial_confs, get_dev_confs, run_giant_models


def predict_partial(stock_name: str, stock_df: pd.DataFrame, to_date: str) -> list[GiantModel]:
    predict_partial_confs = get_predict_partial_confs(stock_name, stock_df, to_date)
    return run_giant_models(stock_name, stock_df, predict_partial_confs)


def dev(stock_name: str, stock_df: pd.DataFrame, to_date: str) -> list[GiantModel]:
    dev_confs = get_dev_confs(stock_name, stock_df, to_date)
    return run_giant_models(stock_name, stock_df, dev_confs)


def hit(giant_models: list[GiantModel]) -> bool:
    hit_10d, hit_5d, hit_3d = False, False, False

    for giant_model in giant_models:
        if not giant_model.need_attention():
            continue
        if giant_model.conf[FORECAST_STEP] == 10:
            hit_10d = True
        if giant_model.conf[FORECAST_STEP] == 5:
            hit_5d = True
        if giant_model.conf[FORECAST_STEP] == 3:
            hit_3d = True

    return hit_10d and hit_5d and hit_3d


if __name__ == '__main__':
    from conf import *


    for _stock_name in [AMD, SNAP, MNSO, TME]:
        _base_engine = preload(_stock_name)
        _stock_df, _fig = _base_engine.stock_df, _base_engine.fig

        giant_models_p = predict_partial(_stock_name, _stock_df, BIG_DATE)
        giant_models_d = dev(_stock_name, _stock_df, BIG_DATE)

        if not hit(giant_models_p):
            print(f'{_stock_name} not hit 10d/5d/3d')
            continue

        for giant_model_p, giant_model_d in zip(giant_models_p, giant_models_d):
            if giant_model_p.need_attention():
                fig = go.Figure(_fig)
                giant_model_p.build_graph(fig, enable=True)
                # fig.show()

                fig = go.Figure(_fig)
                giant_model_d.build_graph(fig, enable=True)
                fig.show()
