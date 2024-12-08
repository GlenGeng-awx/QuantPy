import pandas as pd


# (pnl_tag, total_num, total_pnl, successful_rate)
def eval_long(stock_df: pd.DataFrame,
              indices: list,
              sz: int,
              profit: float,
              hard_loss: float
              ) -> (str, int, float, float):
    total_pnl = 0
    total_num = 0
    pass_num = 0

    for idx in indices:
        if idx + sz not in stock_df.index:
            continue

        pnl = stock_df.loc[idx + sz]['close'] / stock_df.loc[idx]['close'] - 1
        max_loss = 1 - stock_df.loc[idx:idx + sz]['close'].min() / stock_df.loc[idx]['close']

        total_num += 1
        total_pnl += pnl

        if pnl >= profit and max_loss <= hard_loss:
            pass_num += 1

    if total_num == 0:
        return '0, 0.00%, 0%, long', 0, 0, 0

    successful_rate = pass_num / total_num
    return f'{total_num}, {total_pnl:.2%}, {successful_rate:.0%}, long', total_num, total_pnl, successful_rate
