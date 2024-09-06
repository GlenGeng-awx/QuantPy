from gringotts.real_runner import RealRunner
from gringotts.fake_runner import FakeRunner

from .s1_9 import S1U9
from .s1_10 import S1U10
from .s1_10_1 import S1U10V1
from .s1_11 import S1U11
from .s1_11_1 import S1U11V1
from .s1_12 import S1U12
from .s1_12_1 import S1U12V1

# STRATEGIES = [S1U9, S1U10, S1U11, S1U11V1, S1U12, S1U12V1]
STRATEGIES = [S1U10V1]


def calculate_baseline(stock_df, fd):
    for strategy in STRATEGIES:
        runner = RealRunner(stock_df=stock_df, strategy=strategy)

        strategy_name = runner.strategy.name
        stat_text = runner.book.get_stat_text()

        fd.write(f'baseline\t{strategy_name}\t{stat_text}\n')


def display_baseline(stock_df, fig):
    for strategy in STRATEGIES:
        FakeRunner(stock_df=stock_df, strategy=strategy).show(fig)
        # RealRunner(stock_df=stock_df, strategy=strategy).show(fig)
