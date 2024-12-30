import pandas as pd


# (vix_tag, total_num, successful_rate, long_num, short_num)
def eval_vix(stock_df: pd.DataFrame,
             indices: list,
             sz: int,
             long_profit: float,
             short_profit: float,
             hard_loss: float
             ) -> dict:
    total_num, pass_num, long_num, short_num = 0, 0, 0, 0

    for idx in indices:
        if idx + sz not in stock_df.index:
            continue

        total_num += 1

        max_close = stock_df.loc[idx:idx + sz]['close'].max()
        max_long_profit = max_close / stock_df.loc[idx]['close'] - 1

        min_close = stock_df.loc[idx:idx + sz]['close'].min()
        max_short_profit = 1 - min_close / stock_df.loc[idx]['close']

        # check long
        if max_long_profit >= long_profit and max_short_profit <= hard_loss:
            pass_num += 1
            long_num += 1

        # check short
        if max_short_profit >= short_profit and max_long_profit <= hard_loss:
            pass_num += 1
            short_num += 1

    if total_num == 0:
        return {
            'vix_tag': '0, 0.0%, L0, S0',
            'total_num': 0,
            'successful_rate': 0.0,
            'long_num': 0,
            'short_num': 0,
        }
    else:
        successful_rate = pass_num / total_num
        return {
            'vix_tag': f'{total_num}, {successful_rate:.0%}, L{long_num}, S{short_num}',
            'total_num': total_num,
            'successful_rate': successful_rate,
            'long_num': long_num,
            'short_num': short_num,
        }
