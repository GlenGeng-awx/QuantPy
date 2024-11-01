import pandas as pd
from util import load_data, get_idx_by_date, shrink_date_str
from conf import IXIC
from features.common import STEP

KEY = 'baseline incr 1d'
VAL = 57 * STEP
RECALL_DAYS = 1


def baseline_incr_n_days(stock_df: pd.DataFrame, n: int, output_key: str):
    baseline = load_data(IXIC, '1d')
    joint = pd.merge(stock_df, baseline, on='Date', how='left')

    # print(stock_df.head())
    # print(baseline.head())
    # print(joint.head())

    price = joint['close_y']
    indices = []

    for idx in price.index[n:]:
        if all(price[idx - i] > price[idx - i - 1] for i in range(n)):
            indices.append(
                get_idx_by_date(
                    stock_df,
                    shrink_date_str(
                        joint.loc[idx]['Date']
                    )
                )
            )

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[output_key] = s.reindex(stock_df.index, fill_value=False)


def execute(stock_df: pd.DataFrame, **kwargs):
    baseline_incr_n_days(stock_df, 1, KEY)
