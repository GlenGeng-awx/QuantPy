import pandas as pd
from .k_01 import get_resistance_levels_in_last_n_days

KEY = 'up thru r level, <br>retrace, bounds back'
COLOR = 'red'


def execute(stock_df: pd.DataFrame, **kwargs):
    close = stock_df['close']

    indices = set()
    for idx in close.index:
        r_levels = get_resistance_levels_in_last_n_days(stock_df, idx, 60)

        for r_level in r_levels:
            step1 = False
            step2 = False

            # up thru r level in last 10 days
            for n in range(1, 10):
                if close[idx - n - 1] < r_level < close[idx - n]:
                    step1 = True

            # retrace and bounce back
            if close[idx - 1] < close[idx] and close[idx - 1] < close[idx - 2] \
                    and close[idx - 1] > r_level:
                step2 = True

            if step1 and step2:
                indices.add(idx)

    s = pd.Series([True] * len(indices), index=list(indices))
    stock_df[KEY] = s.reindex(stock_df.index, fill_value=False)
