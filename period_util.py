import yfinance as yf
import pandas as pd
import os
from datetime import datetime
from period_conf import *

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.float_format', '{:.0f}'.format)


def local_max(data: pd.DataFrame, column='high') -> set:
    hit_dates = set()

    for idx in range(1, data.shape[0] - 1):
        if (data.iloc[idx][column] > data.iloc[idx - 1][column]
                and data.iloc[idx][column] > data.iloc[idx + 1][column]):
            hit_dates.add(data.iloc[idx]["Date"])

    return hit_dates


def local_max_quasi(data: pd.DataFrame, column='high') -> set:
    hit_dates = set()

    for idx in range(1, data.shape[0]):
        if data.iloc[idx][column] > data.iloc[idx - 1][column]:
            hit_dates.add(data.iloc[idx]["Date"])

    return hit_dates


def local_min(data: pd.DataFrame, column='low') -> set:
    hit_dates = set()

    for idx in range(1, data.shape[0] - 1):
        if (data.iloc[idx][column] < data.iloc[idx - 1][column]
                and data.iloc[idx][column] < data.iloc[idx + 1][column]):
            hit_dates.add(data.iloc[idx]["Date"])

    return hit_dates


def local_min_quasi(data: pd.DataFrame, column='low') -> set:
    hit_dates = set()

    for idx in range(1, data.shape[0]):
        if data.iloc[idx][column] < data.iloc[idx - 1][column]:
            hit_dates.add(data.iloc[idx]["Date"])

    return hit_dates


def range_max(data: pd.DataFrame, step=5) -> set:
    hit_dates = set()

    for idx in range(step, data.shape[0] - step):
        if data.iloc[idx]["high"] == data.iloc[idx - step:idx + step]["high"].max():
            hit_dates.add(data.iloc[idx]["Date"])

    return hit_dates


def range_min(data: pd.DataFrame, step=5) -> set:
    hit_dates = set()

    for idx in range(step, data.shape[0] - step):
        if data.iloc[idx]["low"] == data.iloc[idx - step:idx + step]["low"].min():
            hit_dates.add(data.iloc[idx]["Date"])

    return hit_dates


def load_data(symbol):
    file_name = f'./data/{symbol}.csv'

    if not os.path.exists(file_name):
        print(f'load {symbol} from network')
        ticker = yf.Ticker(symbol)

        df = ticker.history(start="2015-01-01", end="2024-12-31")
        df.columns = df.columns.str.lower()

        df.to_csv(file_name)

    return pd.read_csv(file_name)


def calculate_next_n_workday(from_date, n):
    date_range = pd.bdate_range(start=from_date, periods=n+1)
    return date_range[-1].strftime("%Y-%m-%d")


def shrink_date_str(date_str) -> str:
    # like "2024-06-06 00:00:00-05:00" -> "2024-06-06"
    return date_str.split()[0]

