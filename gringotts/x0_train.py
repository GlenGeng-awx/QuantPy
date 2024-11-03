import pandas as pd
import plotly.graph_objects as go

from gringotts.giant_model import GiantModel
from gringotts.giant_model_proxy import get_train_confs, run_giant_models


def train(stock_name: str, stock_df: pd.DataFrame, to_date: str) -> list[GiantModel]:
    train_confs = get_train_confs(stock_name, stock_df, to_date)
    return run_giant_models(stock_name, stock_df, train_confs)


if __name__ == '__main__':
    from conf import *
    from d1_preload import preload

    import os
    # Set the working directory to QuantPy
    os.chdir('/Users/glen.geng/workspace/QuantPy')

    for _stock_name in ALL:
        _base_engine = preload(_stock_name)
        _stock_df, _fig = _base_engine.stock_df, _base_engine.fig

        giant_models_t = train(_stock_name, _stock_df, BIG_DATE)

        for giant_model_t in giant_models_t:
            fig = go.Figure(_fig)
            giant_model_t.build_graph(fig, enable=True)
            fig.show()
