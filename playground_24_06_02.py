from period_analysis import *

stock_name = 'TSLA'
stock_data = load_data(stock_name)

stock_df = stock_data[(stock_data['Date'] > '2020-01-01') & (stock_data['Date'] < '2024-07-31')]

pa = PeriodAnalysis(stock_name, stock_df)
pa.analyze()

local_min_box = set()

# (from_idx, from_date, from_low, to_idx, to_date, to_high, length, delta, pst, mid)
removed_box = set()
for idx in range(1, len(pa.up_box) - 1):
    prev_box = pa.up_box[idx - 1]
    curr_box = pa.up_box[idx]

    if curr_box[5] < prev_box[5]:
        removed_box.add(curr_box)

# print(f'up trend count: {len(up_trend_box)}')

# s1 = pd.Series([length for (_, _, _, _, _, _, length, _, pst, _) in pa.up_box])
# print(f'length mean: {s1.mean()} std: {s1.std()} max: {s1.max()} min: {s1.min()}')
#
# s2 = pd.Series([pst for (_, _, _, _, _, _, length, _, pst, _) in pa.up_box])
# print(f'up pst mean: {s2.mean()} std: {s2.std()} max: {s2.max()} min: {s2.min()}')

pa.build_graph()

for box in (set(pa.up_box) - removed_box):
    _, from_date, _, _, to_date, _, _, _, _, _ = box
    pa.add_vline([from_date], color='red')
    pa.add_vline([to_date], color='green')

pa.fig.show()
