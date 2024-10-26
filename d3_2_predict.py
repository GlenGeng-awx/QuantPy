import pandas as pd
import plotly.graph_objects as go

from d1_1_preload import preload
from d3_0_giant_model_proxy import get_predict_confs, run_giant_models


def predict(stock_name: str, stock_df: pd.DataFrame, to_date: str):
    predict_confs = get_predict_confs(stock_name, stock_df, to_date)
    return run_giant_models(stock_name, stock_df, predict_confs)


if __name__ == '__main__':
    from conf import *

    for _stock_name in ALL:
        _base_engine = preload(_stock_name)
        _stock_df, _fig = _base_engine.stock_df, _base_engine.fig

        giant_models_p = predict(_stock_name, _stock_df, BIG_DATE)

        for giant_model_p in giant_models_p:
            if not giant_model_p.need_attention():
                continue
            fig = go.Figure(_fig)
            giant_model_p.build_graph(fig, enable=True)
            fig.show()
