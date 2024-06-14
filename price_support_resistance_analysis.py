from conf import *
from util import *


def is_support_level(row: pd.Series):
    return row[local_min_price_3rd] or (row[local_min_price_2nd] and row[range_min_price_30])


def is_resistance_level(row: pd.Series):
    return row[local_max_price_3rd] or (row[local_max_price_2nd] and row[range_max_price_30])


class PriceSupportResistanceAnalysis:
    def __init__(self, stock_df: pd.DataFrame):
        self.stock_df = stock_df
        self.support_resistance_level = []

    def analyze(self):
        for idx, row in self.stock_df.iterrows():
            if is_support_level(row):
                self.support_resistance_level.append(row['low'])
            if is_resistance_level(row):
                self.support_resistance_level.append(row['high'])
