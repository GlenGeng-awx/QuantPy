from period_analysis import *

stock_name = 'COIN'
stock_data = load_data(stock_name)

stock_df = stock_data[(stock_data['Date'] > '2022-05-24') & (stock_data['Date'] < '2023-07-31')]

pa = PeriodAnalysis(stock_name, stock_df)
pa.analyze()

# (from_idx, from_date, from_low, to_idx, to_date, to_high, length, delta, pst, mid)
# df = pd.DataFrame(
#     {
#         'from_date': [from_date for (_, from_date, _, _, _, _, _, _, _, _) in pa.up_box],
#         'to_date': [to_date for (_, _, _, _, to_date, _, _, _, _, _) in pa.up_box],
#         'length': [length for (_, _, _, _, _, _, length, _, _, _) in pa.up_box],
#     }
# )
#
# df.sort_values(by=['length'], ascending=False, inplace=True)
#
# print(df)
pa.build_graph()
#
# filtered_df = df[:int(df.shape[0] * 0.4)]
# for _, row in filtered_df.iterrows():
#     from_date = row['from_date']
#     to_date = row['to_date']
#     pa.add_vline([from_date], color='red', dash=False)
#     pa.add_vline([to_date], color='red', dash=True)

# # (from_idx, from_date, from_low, to_idx, to_date, to_high, length, delta, pst, mid)
# for box in pa.up_box:
#     from_date, to_date, length = box[1], box[4], box[6]
#     if length < 50:
#         continue
#     pa.add_vline([from_date], color='red', dash=False)
#     pa.add_vline([to_date], color='red', dash=True)
#
# # (from_idx, from_date, from_high, to_idx, to_date, to_low, length, delta, pst, mid)
# for box in pa.down_box:
#     from_date, to_date, length = box[1], box[4], box[6]
#     if length < 50:
#         continue
#     pa.add_vline([from_date], color='green', dash=False)
#     pa.add_vline([to_date], color='green', dash=True)


# print(f'up trend count: {len(up_trend_box)}')

# s1 = pd.Series([length for (_, _, _, _, _, _, length, _, pst, _) in pa.up_box])
# print(f'length mean: {s1.mean()} std: {s1.std()} max: {s1.max()} min: {s1.min()}')
#
# s2 = pd.Series([pst for (_, _, _, _, _, _, length, _, pst, _) in pa.up_box])
# print(f'up pst mean: {s2.mean()} std: {s2.std()} max: {s2.max()} min: {s2.min()}')

# pa.build_graph()
#
# for box in (set(pa.up_box) - removed_box):
#     _, from_date, _, _, to_date, _, _, _, _, _ = box
#     pa.add_vline([from_date], color='red')
#     pa.add_vline([to_date], color='green')
#

# for date in pa.stock_df[pa.stock_df['local_max_volume_3rd']]['Date']:
#     pa.fig.add_vline(x=date, line_width=1, line_dash="dash", line_color='red')
#
# for date in pa.stock_df[pa.stock_df['local_min_volume_3rd']]['Date']:
#     pa.fig.add_vline(x=date, line_width=1, line_dash="dash", line_color='green')

pa.fig.show()
