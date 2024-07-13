import plotly.graph_objects as go
from plotly.subplots import make_subplots
from itertools import groupby

from conf import *
from util import load_data, calculate_next_n_workday
from trading_record import TRADING_RECORDS
from trading_record_display import TradingRecordDisplay

INITIAL_POSITIONS = {
    COIN: -1,
    BILI: 10,
}

INITIAL_COSTS = {
    COIN: -146,
    BILI: 116,
}


def get_value_by_date(some_map, date):
    """
    date format '2024-06-26'
    """
    dates = list(some_map.keys())
    dates.sort()

    for i in range(1, len(dates)):
        if dates[i] > date:
            return some_map[dates[i - 1]]

    return some_map[dates[-1]]


class PositionAnalysis:
    def __init__(self, stock_name: str, start_date: str, end_date: str):
        self.stock_name = stock_name
        self.start_date = start_date
        self.end_date = end_date

        self.fig = None
        self.stock_df = None

        # [(date, [(date, action, price, volume), ...]), ...]
        self.trading_records = []

        self.position_map = {}
        self.cost_map = {}
        self.revenue_map = {}

    def calculate_trading_records(self):
        trading_records = TRADING_RECORDS[self.stock_name]

        trading_records = [(date, list(group)) for date, group in groupby(trading_records, key=lambda x: x[0])]
        trading_records.sort(key=lambda x: x[0])

        for date, group in trading_records:
            print(f"{date}\t{group}")

        self.trading_records = trading_records

    def calculate_position_and_cost(self):
        position = INITIAL_POSITIONS.get(self.stock_name, 0)
        position_map = {
            '2024-01-01': position
        }

        cost = INITIAL_COSTS.get(self.stock_name, 0)
        cost_map = {
            '2024-01-01': cost
        }

        for date, group in self.trading_records:
            for _, action, price, volume in group:
                if action == 'buy':
                    position += volume
                    cost += price * volume
                elif action == 'sell':
                    position -= volume
                    cost -= price * volume
                elif action == 'short':
                    position -= volume
                    cost -= price * volume
                print(f"{date} {action} price={price} volume={volume} position={position}")

            print(f"---> {date} position={position} cost={cost}")
            position_map[date] = position
            cost_map[date] = cost

            # position of EOD is 0, it is our real profit or loss
            # current round of game is over, reset cost of tomorrow to 0
            if position == 0:
                cost = 0
                next_date = calculate_next_n_workday(date, 1)
                cost_map[next_date] = cost

        self.position_map = position_map
        self.cost_map = cost_map

    def get_position_by_date(self, date):
        return get_value_by_date(self.position_map, date)

    def get_cost_by_date(self, date):
        return get_value_by_date(self.cost_map, date)

    def calculate_revenue(self):
        revenue_map = {}

        for pos in range(self.stock_df.shape[0]):
            row = self.stock_df.iloc[pos]
            date, close = row['Date'], row['close']

            position = self.get_position_by_date(date)
            cost = self.get_cost_by_date(date)

            gross = position * close
            revenue = gross - cost  # for both long and short

            revenue_map[date] = revenue
            print(f"{date} position={position} close={close:.2f} gross={gross:.2f} cost={cost} revenue={revenue:.2f}")

        self.revenue_map = revenue_map

    def setup_graph(self):
        self.fig = make_subplots(rows=3, cols=1,
                                 subplot_titles=("Close", "Revenue", "Position"),
                                 vertical_spacing=0.05,
                                 row_heights=[0.4, 0.3, 0.3],
                                 shared_xaxes=True,
                                 )

        self.fig.update_xaxes(
            rangebreaks=[
                dict(bounds=["sat", "mon"]),  # hide weekends
            ],
        )

        self.fig.update_layout(
            title=f"{self.stock_name} - Position Analysis",
            hovermode="x unified",
            hoverlabel=dict(namelength=200),
            height=1000,
        )

    def build_graph(self):
        self.fig.add_trace(
            go.Scatter(
                name="close_price",
                x=self.stock_df['Date'],
                y=self.stock_df['close'],
                line=dict(width=0.5, color='blue'),
            )
        )

        TradingRecordDisplay(self.fig, self.stock_name, '1d', True).build_graph()

        revenue_list = list(self.revenue_map.items())
        revenue_list.sort(key=lambda x: x[0])

        self.fig.add_trace(
            go.Scatter(
                name='revenue',
                x=[x for x, _ in revenue_list],
                y=[y for _, y in revenue_list],
                mode='lines + markers',
                line=dict(width=1),
                marker=dict(size=3),
            ),
            row=2, col=1,
        )

        self.fig.add_trace(
            go.Scatter(
                name='position',
                x=[date for date, _ in revenue_list],
                y=[self.get_position_by_date(date) for date, _ in revenue_list],
                mode='lines + markers',
                line=dict(width=1),
                marker=dict(size=3),
            ),
            row=3, col=1,
        )

    def analyze(self):
        stock_df = load_data(self.stock_name, '1d')

        condition = (stock_df['Date'] >= self.start_date) & (stock_df['Date'] <= self.end_date)
        self.stock_df = stock_df[condition]

        self.calculate_trading_records()
        self.calculate_position_and_cost()
        self.calculate_revenue()

        self.setup_graph()
        self.build_graph()
        self.fig.show()


stocks = [
    TSLA,
    MRNA,
    XPEV,
    SNOW,
    BEKE,
    BABA,
    IQ,
    COIN,
    JD,
    PLTR,
    RIVN,
    META,
    MNSO,
    ZM,
    BABA,
    EDU,
    BA,
    PDD,
]

start_date = '2024-01-01'
end_date = datetime.now().strftime('%Y-%m-%d')

for stock in stocks:
    PositionAnalysis(stock, start_date, end_date).analyze()
