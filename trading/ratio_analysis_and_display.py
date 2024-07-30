import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta

from conf import *
from trading.ratio_record import RATIO_RECORDS

ratio_382 = 0.382  # 0.618 ** 2
ratio_500 = 0.500
ratio_618 = 0.618
ratio_786 = 0.786  # sqrt(0.618)

ratio_1000 = 1.000
ratio_1236 = 1.236  # 0.618 * 2
ratio_1382 = 1.382  # 1 + 0.618 ** 2
ratio_1618 = 1.618
ratio_2000 = 2.000
ratio_2618 = 2.618


def wave2_forcast(wave_from, wave_1, stock_name: str = None):
    net = abs(wave_from - wave_1)
    print(f"wave2_forcast for {stock_name}: [from={wave_from}, 1={wave_1}, net={net:.2f}]")

    result = {}

    for ratio in [ratio_382, ratio_500, ratio_618, ratio_786, ratio_1000, ratio_1236, ratio_1382]:
        if wave_from < wave_1:
            key = f'down_{ratio}'
            forcast = wave_1 - net * ratio
        else:  # wave_from > wave_1
            key = f'up_{ratio}'
            forcast = wave_1 + net * ratio

        result[key] = forcast
        print(f"\t{key}\t=\t{forcast:.2f}")

    return result


def wave3_forcast(wave_from, wave_1, wave_2, stock_name: str = None):
    net = abs(wave_from - wave_1)
    print(f"wave3_forcast for {stock_name} [from={wave_from}, 1={wave_1}, 2={wave_2}, net={net:.2f}]")

    result = {}

    for ratio in [ratio_1000, ratio_1236, ratio_1382, ratio_1618, ratio_2000, ratio_2618]:
        if wave_from < wave_1:
            key = f'up_{ratio:.3f}'
            forcast = wave_2 + net * ratio
        else:  # wave_from > wave_1
            key = f'down_{ratio:.3f}'
            forcast = wave_2 - net * ratio

        result[key] = forcast
        print(f"\t{key}\t=\t{forcast:.2f}")

    return result


def wave2_recon(wave_from, wave_1, wave_2, stock_name: str = None):
    net = abs(wave_from - wave_1)
    retrace = abs(wave_1 - wave_2)
    ratio = retrace / net * 100

    print(f"wave2_recon for {stock_name}: [from={wave_from}, 1={wave_1}, 2={wave_2}]")
    print(f"\tnet\t\t=\t{net:.2f}\n\tretrace\t=\t{retrace:.2f}\n\tratio\t=\t{ratio:.2f}%\n")


def wave3_recon(wave_from, wave_1, wave_2, wave_3, stock_name: str = None):
    wave2_recon(wave_from, wave_1, wave_2, stock_name)

    net = abs(wave_from - wave_1)
    forward = abs(wave_2 - wave_3)
    ratio = forward / net * 100

    print(f"wave3_recon for {stock_name}, [from={wave_from}, 1={wave_1}, 2={wave_2}, 3={wave_3}]")
    print(f"\tnet\t\t=\t{net:.2f}\n\tforward\t=\t{forward:.2f}\n\tratio\t=\t{ratio:.2f}%\n")


class RatioForcastDisplay:
    def __init__(self, fig: go.Figure, stock_df: pd.DataFrame, stock_name: str, visible: bool = False):
        self.fig = fig
        self.stock_name = stock_name
        self.visible = visible

        today = stock_df.iloc[-1]['Date']
        today = datetime.strptime(today.split()[0], '%Y-%m-%d')
        self.x1 = (today - timedelta(days=21)).strftime('%Y-%m-%d')
        self.x2 = (today + timedelta(days=14)).strftime('%Y-%m-%d')

    def add_scatter(self, name: str, result: dict):
        # print(f"add_scatter for {name} with {result}")
        x = []
        y = []

        for forcast in result.values():
            x.extend([self.x1, self.x2, None])
            y.extend([forcast, forcast, None])

        self.fig.add_trace(
            go.Scatter(
                name=name,
                x=x,
                y=y,
                mode='lines',
                visible='legendonly' if not self.visible else None,
            ),
            row=1, col=1,
        )

    def build_graph(self):
        records = RATIO_RECORDS.get(self.stock_name, {})

        for wave_from, wave_1 in records.get("wave2_forcast", []):
            name = f'wave2_forcast_{wave_from}_{wave_1}'
            result = wave2_forcast(wave_from, wave_1, self.stock_name)
            self.add_scatter(name, result)

        for wave_from, wave_1, wave_2 in records.get("wave3_forcast", []):
            name = f'wave3_forcast_{wave_from}_{wave_1}_{wave_2}'
            result = wave3_forcast(wave_from, wave_1, wave_2, self.stock_name)
            self.add_scatter(name, result)


if __name__ == '__main__':
    stock_name = HK_0700
    records = RATIO_RECORDS[stock_name]

    for item in records.get("wave2_forcast", []):
        wave2_forcast(*item, stock_name)

    for item in records.get("wave3_forcast", []):
        wave3_forcast(*item, stock_name)

    for item in records.get("wave2_recon", []):
        wave2_recon(*item, stock_name)

    for item in records.get("wave3_recon", []):
        wave3_recon(*item, stock_name)
