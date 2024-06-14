import pandas as pd
from conf import *

max_tasks = [local_max_price_2nd, local_max_price_1st]
min_tasks = [local_min_price_2nd, local_min_price_1st]


class PriceMinMaxForestAnalysis:
    def __init__(self, stock_df: pd.DataFrame):
        self.stock_df = stock_df

        self.max_forest = []
        self.min_forest = []

    def drill_down(self, curr_idx, todo_tasks: list) -> list:
        print(f'drill_down curr_idx={curr_idx}, todo_tasks={todo_tasks}')
        if len(todo_tasks) == 0:
            return []

        todo_task = todo_tasks.pop(0)
        condition = self.stock_df[todo_task]
        curr_df = self.stock_df[condition]

        pos = curr_df.index.get_loc(curr_idx)
        curr_date = curr_df.iloc[pos]['Date']

        left_idx = curr_df.iloc[pos - 1].name
        left_date = curr_df.iloc[pos - 1]['Date']

        right_idx = curr_df.iloc[pos + 1].name
        right_date = curr_df.iloc[pos + 1]['Date']

        print(f'curr_idx={curr_idx}, curr_date={curr_date} --> left_idx={left_idx}, left_date={left_date}')
        print(f'curr_idx={curr_idx}, curr_date={curr_date} --> right_idx={right_idx}, right_date={right_date}')

        edges = [(curr_date, curr_idx, left_date, left_idx), (curr_date, curr_idx, right_date, right_idx)]

        left_tree = self.drill_down(left_idx, todo_tasks.copy())
        right_tree = self.drill_down(right_idx, todo_tasks.copy())

        return edges + left_tree + right_tree

    def analyze(self):
        for idx, row in self.stock_df.iterrows():
            if row[local_max_price_3rd]:
                print(f'hit max idx={idx}, date={row["Date"]}')
                max_tree = self.drill_down(idx, max_tasks.copy())
                print(max_tree)
                self.max_forest += max_tree

        for idx, row in self.stock_df.iterrows():
            if row[local_min_price_3rd]:
                print(f'hit min idx={idx}, date={row["Date"]}')
                min_tree = self.drill_down(idx, min_tasks.copy())
                print(min_tree)
                self.min_forest += min_tree

        print(f'max forest = {self.max_forest}, min forest = {self.min_forest}')
