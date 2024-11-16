import pandas as pd


def eval_long(*args) -> list[str]:
    return [
        fix_days(*args),
        fix_days_with_hard_loss(*args),
    ]


def fix_days(stock_df: pd.DataFrame, indices: list, name: str) -> str:
    sz = 20
    total_pnl = 0
    hit_num = 0

    for idx in indices:
        if idx + sz in stock_df.index:
            pnl = stock_df.loc[idx + sz]['close'] / stock_df.loc[idx]['close'] - 1
            print(f'long -> {name} from {stock_df.loc[idx]["Date"]} to {stock_df.loc[idx + sz]["Date"]}, '
                  f'{sz}d, pnl: {pnl:.2%}')

            total_pnl += pnl
            hit_num += 1

    return f'{hit_num}, {total_pnl:.2%}'


def fix_days_with_hard_loss(stock_df: pd.DataFrame, indices: list, name: str) -> str:
    sz = 20
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
                print(f'long -> {name} from {stock_df.loc[idx]["Date"]} to {stock_df.loc[idx + fail_fast]["Date"]}, '
                      f'{fail_fast}d, pnl: {pnl:.2%}')
            else:
                pnl = stock_df.loc[idx + sz]['close'] / stock_df.loc[idx]['close'] - 1
                print(f'long -> {name} from {stock_df.loc[idx]["Date"]} to {stock_df.loc[idx + sz]["Date"]}, '
                      f'{sz}d, pnl: {pnl:.2%}')

            total_pnl += pnl
            hit_num += 1

    return f'{hit_num}, {total_pnl:.2%}'
