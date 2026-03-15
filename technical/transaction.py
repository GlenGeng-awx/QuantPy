import plotly.graph_objects as go
from transaction_book import TRANSACTION_BOOK
from transaction_book_analyze import build_transaction, Option


class Transaction:
    def __init__(self, stock_name: str):
        transactions = [build_transaction(transaction) for transaction in TRANSACTION_BOOK]
        self.options = [txn for txn in transactions if txn.stock_name == stock_name and isinstance(txn, Option)]

    def build_graph(self, fig: go.Figure, enable=False):
        dates, prices = [], []

        for option in self.options:
            end_date = option.close_date if option.close_date else option.expire_date
            dates.extend([option.open_date, end_date, None])
            prices.extend([option.strike_price, option.strike_price, None])

        fig.add_trace(
            go.Scatter(
                name='transactions', x=dates, y=prices,
                mode='lines', line=dict(width=1.5, color='black', dash='dot'),
                visible=None if enable else 'legendonly',
            )
        )
