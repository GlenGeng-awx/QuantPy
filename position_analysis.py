import plotly.graph_objects as go

from conf import *
from util import load_data, shrink_date_str
from trading_record import TRADING_RECORDS

INITIAL_POSITIONS = {
    TSLA: -4,
    COIN: -1,
    BILI: 10,
}

INITIAL_COSTS = {
    TSLA: -1000,
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
    def __init__(self, fig: go.Figure, stock_name: str, start_date: str, end_date: str):
        self.fig = fig

        self.stock_name = stock_name

        self.start_date = start_date
        self.end_date = end_date

        self.trading_records = TRADING_RECORDS[self.stock_name]

        self.position_map = {}
        self.cost_map = {}
        self.revenue_map = {}

    def calculate_position_and_cost(self):
        position = INITIAL_POSITIONS.get(self.stock_name, 0)
        position_map = {
            '2024-01-01': position
        }

        cost = INITIAL_COSTS.get(self.stock_name, 0)
        cost_map = {
            '2024-01-01': cost
        }

        for date, action, price, volume in reversed(self.trading_records):
            if action == 'buy':
                position += volume
                cost += price * volume
            elif action == 'sell':
                position -= volume
                cost -= price * volume
            elif action == 'short':
                position -= volume
                cost -= price * volume

            # current round of game is over, reset cost to 0
            if position == 0:
                cost = 0

            position_map[date] = position
            cost_map[date] = cost
            print(f"{date} {action} price={price} volume={volume} position={position}")

        self.position_map = position_map
        self.cost_map = cost_map

    def get_position_by_date(self, date):
        return get_value_by_date(self.position_map, date)

    def get_cost_by_date(self, date):
        return get_value_by_date(self.cost_map, date)

    def calculate_revenue(self):
        stock_df = load_data(self.stock_name, '1d')

        condition = (stock_df['Date'] >= self.start_date) & (stock_df['Date'] <= self.end_date)
        stock_df = stock_df[condition]

        revenue_map = {}
        for pos in range(stock_df.shape[0]):
            row = stock_df.iloc[pos]
            date, close = row['Date'], row['close']

            position = self.get_position_by_date(date)
            cost = self.get_cost_by_date(date)

            gross = position * close
            revenue = gross - cost  # for both long and short

            revenue_map[date] = revenue
            print(f"{date} position={position} close={close} gross={gross} cost={cost} revenue={revenue}")

        self.revenue_map = revenue_map

    def build_graph(self):
        revenue_list = list(self.revenue_map.items())
        revenue_list.sort(key=lambda x: x[0])

        self.fig.add_trace(
            go.Scatter(
                name=self.stock_name,
                x=[x for x, _ in revenue_list],
                y=[y for _, y in revenue_list],
                mode='lines + markers',
                line=dict(width=1),
                marker=dict(size=3),
            )
        )

    def analyze(self):
        self.calculate_position_and_cost()
        self.calculate_revenue()
        self.build_graph()


def setup_graph():
    fig = go.Figure()

    fig.update_xaxes(
        rangebreaks=[
            dict(bounds=["sat", "mon"]),  # hide weekends
        ],
    )

    fig.update_layout(
        title="Position Analysis",
        xaxis_title="Date",
        yaxis_title="Revenue",
        hovermode="x unified",
        hoverlabel=dict(namelength=200),
    )

    return fig


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

fig = setup_graph()

for stock in stocks:
    PositionAnalysis(fig, stock, start_date, end_date).analyze()

fig.show()
