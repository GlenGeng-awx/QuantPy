from util import load_data
from min_max_analysis import MinMaxAnalysis
from price_min_max_forest_analysis import PriceMinMaxForestAnalysis
from price_support_resistance_analysis import PriceSupportResistanceAnalysis
from price_box_analysis import PriceBoxAnalysis


class AnalysisEngine:
    def __init__(self, stock_name, from_date, to_date):
        self.stock_name = stock_name
        self.from_date = from_date
        self.to_date = to_date

        self.stock_df = None

        self.min_max_analysis = None
        self.price_min_max_forest_analysis = None
        self.price_support_resistance_analysis = None
        self.price_box_analysis = None

    def analyze(self):
        stock_data = load_data(self.stock_name)

        condition = (stock_data['Date'] > self.from_date) & (stock_data['Date'] < self.to_date)
        self.stock_df = stock_data[condition]

        self.min_max_analysis = MinMaxAnalysis(self.stock_name, self.stock_df)
        self.min_max_analysis.analyze()
        self.stock_df = self.min_max_analysis.stock_df

        self.price_min_max_forest_analysis = PriceMinMaxForestAnalysis(self.stock_df)
        self.price_min_max_forest_analysis.analyze()

        self.price_support_resistance_analysis = PriceSupportResistanceAnalysis(self.stock_df)
        self.price_support_resistance_analysis.analyze()

        self.price_box_analysis = PriceBoxAnalysis(self.stock_df)
        self.price_box_analysis.analyze()




