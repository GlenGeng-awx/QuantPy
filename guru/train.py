import pandas as pd

from guru import get_index, eval_ops

from guru import (
    guru_1,  # sr level
    guru_2,  # ma
    guru_3,  # shape
    guru_4,  # vol
    guru_5,  # statistic
    guru_6,  # yesterday min max
    guru_7,  # price
    guru_8,  # weekday
    guru_9,  # post
)


def build_train_ctx(stock_df: pd.DataFrame, from_idx, to_idx) -> dict:
    train_ctx = {}

    total_ops = guru_1.operators \
                + guru_2.operators \
                + guru_3.operators \
                + guru_4.operators \
                + guru_5.operators \
                + guru_6.operators \
                + guru_7.operators \
                + guru_8.operators \
                + guru_9.operators

    for op in total_ops:
        hits = set()
        for idx in get_index(stock_df, from_idx, to_idx):
            if op(stock_df, idx):
                hits.add(idx)
        train_ctx[op.__name__] = hits

    return train_ctx


def filter_ops(train_ctx: dict, ops: list) -> list:
    hits = train_ctx[ops[0].__name__]
    for op in ops[1:]:
        hits = hits.intersection(train_ctx[op.__name__])
        if len(hits) <= 1:
            return []
    return sorted(list(hits))


def train_ops(stock_df: pd.DataFrame, stock_name, fd, train_ctx: dict, ops) -> bool:
    indices = filter_ops(train_ctx, ops)
    if not indices:
        return False

    name = ','.join(op.__name__ for op in ops)
    pnl_tag, color = eval_ops(stock_df, stock_name, indices, name)
    if pnl_tag is None:
        return False

    print(f'{stock_name} {name} ---> {pnl_tag}')
    fd.write(f'{name}\t{pnl_tag}\n')
    fd.flush()
    return True


def train(stock_df: pd.DataFrame, stock_name, from_idx, to_idx):
    train_ctx = build_train_ctx(stock_df, from_idx, to_idx)
    print(f'finish build train ctx for {stock_name}')

    with open(f'./tmp/{stock_name}.res', 'w') as fd:
        for op1 in guru_1.operators:
            for op2 in guru_2.operators:
                for op3 in guru_3.operators:
                    for op4 in guru_4.operators:
                        for op5 in guru_5.operators:
                            for op6 in guru_6.operators:
                                for op7 in guru_7.operators:
                                    for op8 in guru_8.operators:
                                        for op9 in guru_9.operators:
                                            train_ops(stock_df,
                                                      stock_name,
                                                      fd,
                                                      train_ctx,
                                                      [op1, op2, op3, op4, op5, op6, op7, op8, op9])
