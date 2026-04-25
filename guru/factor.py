class Factor:
    def __init__(self, key, color, fn):
        """fn: (stock_df: DataFrame) -> list[date], returns dates where the factor triggered"""
        self.KEY = key
        self.COLOR = color
        self.calculate_hits = fn
