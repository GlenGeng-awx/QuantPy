import pandas as pd
from util import shrink_date_str, get_idx_by_date


# return 400/200/100 period in the format of [(from_date, to_date)]
def get_train_periods(stock_df: pd.DataFrame, to_date: str) -> list[tuple]:
    to_idx = get_idx_by_date(stock_df, to_date)

    periods = []

    for sz in [400, 200, 100]:
        from_idx = to_idx - sz
        from_date = shrink_date_str(stock_df.loc[from_idx]['Date'])
        periods.append((from_date, to_date))

    return periods


# return 400/200/100 period in the format of [(from_date, today)]
def get_predict_periods(stock_df: pd.DataFrame, to_date: str) -> list[tuple]:
    train_periods = get_train_periods(stock_df, to_date)
    today = shrink_date_str(stock_df.iloc[-1]['Date'])

    predict_periods = [(train_from_date, today) for (train_from_date, _) in train_periods]
    return predict_periods


# last 5d/1d
def get_predict_partial_period(stock_df: pd.DataFrame) -> tuple:
    last_5d = shrink_date_str(stock_df.iloc[-5]['Date'])
    last_4d = shrink_date_str(stock_df.iloc[-4]['Date'])
    return last_5d, last_4d


if __name__ == '__main__':
    from conf import PDD, BIG_DATE
    from d1_1_preload import preload

    _base_engine = preload(PDD)
    _stock_df = _base_engine.stock_df

    _train_periods = get_train_periods(_stock_df, BIG_DATE)
    _predict_periods = get_predict_periods(_stock_df, BIG_DATE)
    _predict_partial_period = get_predict_partial_period(_stock_df)

    print(_train_periods)
    print(_predict_periods)
    print(_predict_partial_period)
