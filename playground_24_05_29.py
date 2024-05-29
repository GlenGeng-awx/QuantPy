from period_analysis import *

PERIOD = 100


def compare_local_max_3rd(df1: pd.DataFrame, df2: pd.DataFrame) -> bool:
    return df1['local_max_3rd'].equals(df2.iloc[:-1]['local_max_3rd'])


def compare_local_max_2nd(df1: pd.DataFrame, df2: pd.DataFrame) -> bool:
    return df1[df1['local_max_2nd'] & df1['range_max_n']].equals(
        df2.iloc[:-1][df2['local_max_2nd'] & df2['range_max_n']])


def compare_local_min_3rd(df1: pd.DataFrame, df2: pd.DataFrame) -> bool:
    return df1['local_min_3rd'].equals(df2.iloc[:-1]['local_min_3rd'])


def compare_local_min_2nd(df1: pd.DataFrame, df2: pd.DataFrame) -> bool:
    return df1[df1['local_min_2nd'] & df1['range_min_n']].equals(
        df2.iloc[:-1][df2['local_min_2nd'] & df2['range_min_n']])


def compare(df1: pd.DataFrame, df2: pd.DataFrame, stock_name, date: str) -> bool:
    assert df1.shape[0] == df2.shape[0] - 1

    flag = False

    if not compare_local_max_3rd(df1, df2):
        print(stock_name, 'hit local_max_3rd at', date)
        flag = True

    if not compare_local_max_2nd(df1, df2):
        print(stock_name, 'hit local_max_2nd at', date)
        flag = True

    if not compare_local_min_3rd(df1, df2):
        print(stock_name, 'hit local_min_3rd at', date)
        flag = True

    if not compare_local_min_2nd(df1, df2):
        print(stock_name, 'hit local_min_2nd at', date)
        flag = True

    return flag


def predict_period(stock_name, stock_data: pd.DataFrame) -> list:
    hit_dates = []
    stock_data = stock_data[stock_data['Date'] > '2021-01-01']

    for idx in range(stock_data.shape[0] - PERIOD - 1):
        stock_df1 = stock_data.iloc[idx:idx + PERIOD]
        pa1 = PeriodAnalysis(stock_name, stock_df1)
        pa1.analyze()

        stock_df2 = stock_data.iloc[idx:idx + PERIOD + 1]
        pa2 = PeriodAnalysis(stock_name, stock_df2)
        pa2.analyze()

        curr_date = stock_data.iloc[idx + PERIOD]['Date']

        if compare(pa1.stock_df.copy(), pa2.stock_df.copy(), stock_name, curr_date):
            hit_dates.append(curr_date)

    return hit_dates

# predict_dates = predict_period(stock_name, stock_data)
# pa.add_vline([predict_date for predict_date in predict_dates if start_date < predict_date < end_date])
