import pandas as pd


# calculates: list of (value, idx)
def _pick_rolling_n_pst_reversed(stock_df: pd.DataFrame, candidates: list, tag: str,
                                 n: float = 0.1, rolling_size: int = 200) -> list:
    hits = []

    for i in range(rolling_size, len(candidates)):
        value, idx = candidates[i]
        if value is None:
            continue

        rolling_window = [(_value, _idx) for (_value, _idx) in candidates[i - rolling_size:i] if _value is not None]
        # print(f'tag = {tag}, date = {stock_df["Date"][idx]}, rolling_window = {rolling_window}')

        if rolling_window:
            rolling_window.sort(key=lambda x: x[0], reverse=True)
            threshold_pos = int(len(rolling_window) * n) - 1
            threshold_value = rolling_window[threshold_pos][0]
        else:
            threshold_value = 0.0

        if value >= threshold_value:
            date = stock_df['Date'][idx]
            hits.append(date)
            # print(f'tag = {tag}, date = {date}, value = {value:.2%}, threshold_value = {threshold_value:.2%}')

    return hits


# calculates: list of (value, idx)
def _pick_rolling_n_pst(stock_df: pd.DataFrame, candidates: list, tag: str,
                        n: float = 0.1, rolling_size: int = 200) -> list:
    hits = []

    for i in range(rolling_size, len(candidates)):
        value, idx = candidates[i]
        if value is None:
            continue

        rolling_window = [(_value, _idx) for (_value, _idx) in candidates[i - rolling_size:i] if _value is not None]

        if rolling_window:
            rolling_window.sort(key=lambda x: x[0], reverse=False)
            threshold_pos = int(len(rolling_window) * n) - 1
            threshold_value = rolling_window[threshold_pos][0]
        else:
            threshold_value = 1.0

        if value <= threshold_value:
            date = stock_df['Date'][idx]
            hits.append(date)
            # print(f'tag = {tag}, date = {date}, value = {value:.2%}, threshold_value = {threshold_value:.2%}')

    return hits
