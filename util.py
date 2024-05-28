import yfinance as yf
import pandas as pd
import os


def local_max(data: pd.DataFrame) -> pd.DataFrame:
    hit_dates = set()

    for idx in range(1, data.shape[0] - 1):
        if (data.iloc[idx]["high"] > data.iloc[idx - 1]["high"]
                and data.iloc[idx]["high"] > data.iloc[idx + 1]["high"]):
            hit_dates.add(data.iloc[idx]["Date"])

    hit_rows = data[data["Date"].isin(hit_dates)]
    print(f'shape of local max: {hit_rows.shape}')
    return hit_rows


def local_min(data: pd.DataFrame) -> pd.DataFrame:
    hit_dates = set()

    for idx in range(1, data.shape[0] - 1):
        if (data.iloc[idx]["low"] < data.iloc[idx - 1]["low"]
                and data.iloc[idx]["low"] < data.iloc[idx + 1]["low"]):
            hit_dates.add(data.iloc[idx]["Date"])

    hit_rows = data[data["Date"].isin(hit_dates)]
    print(f'shape of lcoal min: {hit_rows.shape}')
    return hit_rows


def range_max(data: pd.DataFrame, step=5) -> pd.DataFrame:
    hit_dates = set()

    for idx in range(step, data.shape[0] - step):
        if data.iloc[idx]["high"] == data.iloc[idx - step:idx + step]["high"].max():
            hit_dates.add(data.iloc[idx]["Date"])

    hit_rows = data[data["Date"].isin(hit_dates)]
    print(f'shape of range max: {hit_rows.shape}')
    return hit_rows


def range_min(data: pd.DataFrame, step=5) -> pd.DataFrame:
    hit_dates = set()

    for idx in range(step, data.shape[0] - step):
        if data.iloc[idx]["low"] == data.iloc[idx - step:idx + step]["low"].min():
            hit_dates.add(data.iloc[idx]["Date"])

    hit_rows = data[data["Date"].isin(hit_dates)]
    print(f'shape of range min: {hit_rows.shape}')
    return hit_rows


def load_data(symbol):
    file_name = f'./data/{symbol}.csv'

    if not os.path.exists(file_name):
        print(f'load {symbol} from network')
        ticker = yf.Ticker(symbol)

        df = ticker.history(start="2015-01-01", end="2024-05-31")
        df.columns = df.columns.str.lower()

        df.to_csv(file_name)

    return pd.read_csv(file_name)

