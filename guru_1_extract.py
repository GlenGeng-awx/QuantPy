from d1_preload import preload
from util import get_idx_by_date
from features import FEATURE_BUF


def extract(stock_name, to_date, recall_days, features_per_day) -> dict:
    base_engine = preload(stock_name)
    stock_df, fig = base_engine.stock_df, base_engine.fig
    fig.show()

    to_idx = get_idx_by_date(stock_df, to_date)
    stats = {}

    for idx in range(to_idx - recall_days + 1, to_idx + 1):
        stat = {}

        for feature in FEATURE_BUF:
            key = feature.KEY
            if stock_df.loc[idx][key]:
                condition = stock_df[key]
                stat[key] = len(stock_df[condition])

        stat = dict(sorted(stat.items(), key=lambda x: x[1])[:features_per_day])
        stats[idx] = stat

    return stats


if __name__ == '__main__':
    import json
    from conf import *

    stock_name = COIN
    to_date = '2024-11-01'
    recall_days = 2
    features_per_day = 10

    stats = extract(stock_name, to_date, recall_days, features_per_day)
    print(json.dumps(stats, indent=4))
