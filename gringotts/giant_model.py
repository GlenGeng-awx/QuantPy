import json

from gringotts.tiny_model import enumerate_switches, TinyModel, BUY_SWITCHES, SELL_SWITCHES
from gringotts.real_runner import RealRunner

BUY_SWITCHES_SIZE = len(BUY_SWITCHES)
SELL_SWITCHES_SIZE = len(SELL_SWITCHES)

# SEARCH_TOP = 50
# DISPLAY_TOP = 20
SEARCH_TOP = 2
DISPLAY_TOP = 2


def calculate_giant_model(stock_df, fd):
    # prune space: strategy that could trigger buy
    all_buy_switches = enumerate_switches(BUY_SWITCHES_SIZE)
    default_sell_switches = [False, True, False, False, True, False, False, False, False]

    pruned_buy_switches = []

    for buy_switches in all_buy_switches:
        runner = RealRunner(stock_df=stock_df,
                            strategy=TinyModel,
                            buy_switches=buy_switches,
                            sell_switches=default_sell_switches)
        stat = runner.book.get_stat()

        if stat['buy_count'] > 0:
            pruned_buy_switches.append((buy_switches, stat['revenue_pst'], stat['buy_count'], stat))

    pruned_buy_switches.sort(key=lambda x: (x[1], x[2]), reverse=True)

    for idx, (buy_switches, _, _, stat) in enumerate(pruned_buy_switches):
        fd.write(f'prune tiny model {idx}\t{json.dumps(stat)}\tbuy;{buy_switches};default_sell\n')

    # further search top ones
    all_sell_switches = enumerate_switches(SELL_SWITCHES_SIZE)

    for x, (buy_switches, _, _, stat) in enumerate(pruned_buy_switches[:SEARCH_TOP + 1]):
        baseline = (buy_switches, default_sell_switches, 0, 0, stat)

        results = []

        for sell_switches in all_sell_switches:
            runner = RealRunner(stock_df=stock_df,
                                strategy=TinyModel,
                                buy_switches=buy_switches,
                                sell_switches=sell_switches)
            stat = runner.book.get_stat()

            results.append((buy_switches, sell_switches, stat['revenue_pst'], stat['buy_count'], stat))

        results.sort(key=lambda x: (x[2], x[3]), reverse=True)
        results.insert(0, baseline)

        for y, (_, sell_switches, _, _, stat) in enumerate(results[:DISPLAY_TOP + 1]):
            fd.write(f'search tiny model {x}-{y}\t{json.dumps(stat)} --> buy {buy_switches}, sell {sell_switches}\n')
