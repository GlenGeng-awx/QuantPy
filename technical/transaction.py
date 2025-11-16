import plotly.graph_objects as go
from transaction_book import TRANSACTION_BOOK


class Transaction:
    def __init__(self, stock_name: str):
        self.transactions = []
        for transaction in TRANSACTION_BOOK:
            if transaction[2] == stock_name:
                self.transactions.append(transaction)

    def build_graph(self, fig: go.Figure, enable=False):
        dates, prices = [], []

        for transaction_date, expiration_date, stock_name, strike_prices in self.transactions:
            for strike_price in strike_prices:
                dates.extend([transaction_date, expiration_date, None])
                prices.extend([strike_price, strike_price, None])

        fig.add_trace(
            go.Scatter(
                name='transactions', x=dates, y=prices,
                mode='lines', line=dict(width=1, color='blue', dash='dot'),
                visible=None if enable else 'legendonly',
            )
        )
