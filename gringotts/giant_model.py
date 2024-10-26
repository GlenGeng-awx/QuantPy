import pandas as pd
import plotly.graph_objects as go
from multiprocessing import Process, Queue

from util import get_indices_of_period
from features import FEATURE_BUF
from gringotts import MODE, MASK, FORECAST_STEP, MARGIN, HIT_THRESHOLD, FROM_DATE, TO_DATE
from gringotts.tiny_model import TinyModel
from gringotts.giant_model_helper import enumerate_switches, shrink_models, show_models
from gringotts.giant_model_serde import serialize_models, deserialize_models
from gringotts.giant_model_train import giant_model_worker


# during train, handle multiple coarse evaluators in a multiprocess way
# during predict, handle one fine evaluator deserializing from file
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
            self._predict_or_dev()

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
            self.long_models.extend(long_models)
            self.short_models.extend(short_models)

        self.long_models = shrink_models(self.long_models)
        self.short_models = shrink_models(self.short_models)

        # to train dir
        serialize_models(self.stock_name, self.conf, self.long_models, self.short_models)

    def _predict_or_dev(self):
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

        if self.conf[MODE] == 'predict':
            # to predict dir
            serialize_models(self.stock_name, self.conf, self.long_models, self.short_models)

    def need_attention(self) -> bool:
        return any(model.filter.output_indices for model in self.long_models + self.short_models)

    def build_graph(self, fig: go.Figure, enable=False):
        origin_title = fig.layout.title.text

        strategy_name = f'{self.conf[MODE]} < forecast {self.conf[FORECAST_STEP]}d > '
        strategy_name += f'[{self.conf[FROM_DATE]}, {self.conf[TO_DATE]}] total {len(self.input_indices)} days '

        if self.conf[MODE] != 'train':
            strategy_name += f'({self.conf[MARGIN] * 100:.1f}%, {self.conf[HIT_THRESHOLD]})'

        fig.update_layout(title=f'{origin_title}<br>{strategy_name}')

        fig.add_vline(x=self.conf[FROM_DATE], line_dash="dash", line_width=1, line_color='red', row=1)
        fig.add_vline(x=self.conf[TO_DATE], line_dash="dash", line_width=1, line_color='red', row=1)

        show_models(self.stock_df, fig, self.long_models, 'orange', 7, enable)
        show_models(self.stock_df, fig, self.short_models, 'black', 5, enable)
