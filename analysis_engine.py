from util import load_data
from technical.min_max_analysis_and_display import MinMaxAnalysis
from technical.wave_analysis_and_display import WaveAnalysis


class AnalysisEngine:
    def __init__(self, stock_name, from_date, to_date, interval='1d'):
        self.stock_name = stock_name
        self.from_date = from_date
        self.to_date = to_date
        self.interval = interval

        self.stock_df = None

        self.min_max_analysis = None
        self.wave_analysis = None
        self.price_box_analysis = None

    def analyze(self):
        stock_data = load_data(self.stock_name, self.interval)

        condition = (stock_data['Date'] > self.from_date) & (stock_data['Date'] < self.to_date)
        stock_df = stock_data[condition]

        self.min_max_analysis = MinMaxAnalysis(self.stock_name, self.interval, stock_df)
        self.min_max_analysis.analyze()

        self.stock_df = self.min_max_analysis.stock_df

        self.wave_analysis = WaveAnalysis(self.stock_df)
        self.wave_analysis.analyze()

