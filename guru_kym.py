import json
import pandas as pd
from base_engine import BaseEngine
from preload_conf import *
from conf import *
from util import shrink_date_str, get_idx_by_date

kym_report = {}

dates = [
    '2025-07-14', '2025-07-15', '2025-07-16', '2025-07-17', '2025-07-18',
    '2025-07-21', '2025-07-22', '2025-07-23', '2025-07-24', '2025-07-25',
    '2025-07-28', '2025-07-29', '2025-07-30', '2025-07-31', '2025-08-01',

    '2025-08-04', '2025-08-05', '2025-08-06', '2025-08-07', '2025-08-08',
    '2025-08-11', '2025-08-12', '2025-08-13', '2025-08-14', '2025-08-15',
    '2025-08-18', '2025-08-19', '2025-08-20', '2025-08-21', '2025-08-22',
    '2025-08-25',
]

# load predictions
with open("_predict", "r") as f:
    prediction = json.load(f)

for stock_name in ALL:
    kym_report[stock_name] = {}

    (from_date, to_date, interval), args = period_1y(), args_1y_guru()

    base_engine = BaseEngine(stock_name, from_date, to_date, interval)
    base_engine.build_graph(**args)

    # load context
    stock_df, context = base_engine.stock_df, base_engine.context

    for date in dates:
        idx = get_idx_by_date(stock_df, date)
        close = stock_df['close'].loc[idx]
        min_close = stock_df['close'].loc[idx:idx + 15].min()
        max_close = stock_df['close'].loc[idx:idx + 15].max()

        # predict
        cell = 'X' if date in prediction[stock_name] else '_'

        # up
        for key in ['will spike', 'will shoot up']:
            hits = [shrink_date_str(d) for d in context.get(key, [])]
            cell += 'U' if date in hits else '_'

        cell += 'U' if max_close / close - 1 > 0.1 else '_'

        # down
        for key in ['will crash', 'will shoot down']:
            hits = [shrink_date_str(d) for d in context.get(key, [])]
            cell += 'D' if date in hits else '_'

        cell += 'D' if 1 - min_close / close > 0.1 else '_'

        kym_report[stock_name][date] = cell

kym_df = pd.DataFrame(kym_report).T


def is_x(_cell):
    return 'X' in _cell


def is_just_x(_cell):
    return 'X______' in _cell


correct_rates = []
for date in kym_df.columns:
    count_all = kym_df[date].apply(is_x).sum()
    count_fail = kym_df[date].apply(is_just_x).sum()

    correct_rate = (1 - count_fail / count_all) if count_all > 0 else None
    correct_rates.append(f'{correct_rate:.2f}/{count_all}')

kym_df.loc['correct_rates'] = correct_rates

print(kym_df)
