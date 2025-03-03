import os
from datetime import datetime

import yfinance as yf
import pandas as pd
import plotly.io as pio

pio.renderers.default = "browser"

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.float_format', '{:.3f}'.format)


def local_max(data: pd.DataFrame, column='close') -> pd.Series:
    hits = []
    indices = []

    for pos in range(1, data.shape[0] - 1):
        if (data.iloc[pos][column] > data.iloc[pos - 1][column]
                and data.iloc[pos][column] >= data.iloc[pos + 1][column]):
            hits.append(True)
            indices.append(data.iloc[pos].name)

    return pd.Series(hits, index=indices)


def local_min(data: pd.DataFrame, column='close') -> pd.Series:
    hits = []
    indices = []

    for pos in range(1, data.shape[0] - 1):
        if (data.iloc[pos][column] < data.iloc[pos - 1][column]
                and data.iloc[pos][column] <= data.iloc[pos + 1][column]):
            hits.append(True)
            indices.append(data.iloc[pos].name)

    return pd.Series(hits, index=indices)


def max_between(data: pd.DataFrame, start_idx, end_idx, column='close') -> int:
    # max price in [start_idx, end_idx]
    # print(f'max_between(start_idx={start_idx}, end_idx={end_idx})')
    return data.loc[start_idx:end_idx][column].idxmax()


def min_between(data: pd.DataFrame, start_idx, end_idx, column='close') -> int:
    # min price in [start_idx, end_idx]
    # print(f'min_between(start_idx={start_idx}, end_idx={end_idx})')
    return data.loc[start_idx:end_idx][column].idxmin()


def load_data(symbol, interval):
    """ interval is 1h, 1d or 1wk """
    file_name = f'./stock_data/{symbol}_{interval}.csv'

    start_date = '2023-01-01' if interval == '1h' else '2015-01-01'
    end_date = datetime(datetime.now().year, 12, 31).strftime('%Y-%m-%d')

    if not os.path.exists(file_name):
        print(f'load {symbol} {interval} from network')
        ticker = yf.Ticker(symbol)

        df = ticker.history(start=start_date, end=end_date, interval=interval)
        df.index.name = 'Date'
        df.columns = df.columns.str.lower()

        df.to_csv(file_name)

    return pd.read_csv(file_name)


def get_next_n_workday(from_date, n):
    date_range = pd.bdate_range(start=from_date, periods=n + 1)
    return date_range[-1].strftime("%Y-%m-%d")


def get_prev_n_workday(from_date, n):
    date_range = pd.bdate_range(end=from_date, periods=n + 1)
    return date_range[0].strftime('%Y-%m-%d')


def shrink_date_str(date_str) -> str:
    # like "2024-06-06 00:00:00-05:00" -> "2024-06-06"
    return date_str.split()[0]


def interval_to_label(interval: str, abbr=False):
    if interval == '1h':
        return 'hours' if not abbr else 'h'
    elif interval == '1d':
        return 'days' if not abbr else 'd'
    elif interval == '1wk':
        return 'weeks' if not abbr else 'w'
    else:
        return 'unknown'


# date is in the format of '2022-01-03'
def get_idx_by_date(stock_df: pd.DataFrame, date: str) -> int:
    # print(f'get_idx_by_date(date={date})')
    dates = stock_df['Date'].apply(shrink_date_str)
    return dates[dates == date].index[0]


# date is in the format of '2022-01-03'
def get_indices_of_period(stock_df: pd.DataFrame, from_date, to_date) -> tuple[int, int]:
    print(f'get_indices_of_period(from_date={from_date}, to_date={to_date})')
    start_idx = get_idx_by_date(stock_df, from_date)
    end_idx = get_idx_by_date(stock_df, to_date)
    return start_idx, end_idx


def touch(file_name: str):
    with open(file_name, 'a'):
        pass


if __name__ == '__main__':
    today = datetime.now().strftime('%Y-%m-%d')
    print(get_next_n_workday(today, 5))
    print(get_prev_n_workday(today, 5))
