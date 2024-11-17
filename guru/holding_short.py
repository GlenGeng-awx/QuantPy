import pandas as pd


def eval_short(*args) -> list[(str, int, float)]:
    return [
        fix_days(*args),
        fix_days_with_hard_loss(*args),
    ]


def fix_days(stock_df: pd.DataFrame, indices: list, name: str) -> (str, int, float):
    sz = 20
    total_pnl = 0
    hit_num = 0

    for idx in indices:
        if idx + sz in stock_df.index:
            pnl = 1 - stock_df.loc[idx + sz]['close'] / stock_df.loc[idx]['close']
            print(f'short -> {name} from {stock_df.loc[idx]["Date"]} to {stock_df.loc[idx + sz]["Date"]}, '
                  f'{sz}d, pnl: {pnl:.2%}')

            total_pnl += pnl
            hit_num += 1

    return f'{hit_num}, {total_pnl:.2%}, fix', hit_num, total_pnl


def fix_days_with_hard_loss(stock_df: pd.DataFrame, indices: list, name: str) -> (str, int, float):
    sz = 20
    hard_loss = 0.03

    total_pnl = 0
    hit_num = 0

    for idx in indices:
        if idx + sz in stock_df.index:
            fail_fast = None

            for i in range(2, sz):
                if stock_df.loc[idx + i]['close'] >= stock_df.loc[idx]['close'] * (1 + hard_loss):
                    fail_fast = i
                    break

            if fail_fast is not None:
                pnl = 1 - stock_df.loc[idx + fail_fast]['close'] / stock_df.loc[idx]['close']
                print(f'short -> {name} from {stock_df.loc[idx]["Date"]} to {stock_df.loc[idx + fail_fast]["Date"]}, '
                      f'{fail_fast}d, pnl: {pnl:.2%}')
            else:
                pnl = 1 - stock_df.loc[idx + sz]['close'] / stock_df.loc[idx]['close']
                print(f'short -> {name} from {stock_df.loc[idx]["Date"]} to {stock_df.loc[idx + sz]["Date"]}, '
                      f'{sz}d, pnl: {pnl:.2%}')

            total_pnl += pnl
            hit_num += 1

    return f'{hit_num}, {total_pnl:.2%}, hard', hit_num, total_pnl
