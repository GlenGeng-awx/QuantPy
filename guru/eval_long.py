import pandas as pd

SZ = 15


def eval_long(*args) -> list[(str, int, float)]:
    return [
        fix_days(*args),
        fix_days_with_hard_loss(*args),
    ]


def fix_days(stock_df: pd.DataFrame, indices: list) -> (str, int, float):
    sz = SZ
    total_pnl = 0
    hit_num = 0

    for idx in indices:
        if idx + sz in stock_df.index:
            pnl = stock_df.loc[idx + sz]['close'] / stock_df.loc[idx]['close'] - 1

            total_pnl += pnl
            hit_num += 1

    return f'{hit_num}, {total_pnl:.2%}, long fix', hit_num, total_pnl


def fix_days_with_hard_loss(stock_df: pd.DataFrame, indices: list) -> (str, int, float):
    sz = SZ
    hard_loss = 0.03

    total_pnl = 0
    hit_num = 0

    for idx in indices:
        if idx + sz in stock_df.index:
            fail_fast = None

            for i in range(2, sz):
                if stock_df.loc[idx + i]['close'] <= stock_df.loc[idx]['close'] * (1 - hard_loss):
                    fail_fast = i
                    break

            if fail_fast is not None:
                pnl = stock_df.loc[idx + fail_fast]['close'] / stock_df.loc[idx]['close'] - 1
            else:
                pnl = stock_df.loc[idx + sz]['close'] / stock_df.loc[idx]['close'] - 1

            total_pnl += pnl
            hit_num += 1

    return f'{hit_num}, {total_pnl:.2%}, long hard', hit_num, total_pnl
