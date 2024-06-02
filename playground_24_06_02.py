from period_analysis import *

stock_name = 'TSLA'
stock_data = load_data(stock_name)

stock_df = stock_data[(stock_data['Date'] > '2020-01-01') & (stock_data['Date'] < '2024-07-31')]

pa = PeriodAnalysis(stock_name, stock_df)
pa.analyze()


for (_, _, _, _, _, _, length, _, pst, _) in pa.up_box:
    pass

s1 = pd.Series([length for (_, _, _, _, _, _, length, _, pst, _) in pa.up_box])
print(f'length mean: {s1.mean()} std: {s1.std()} max: {s1.max()} min: {s1.min()}')

s2 = pd.Series([pst for (_, _, _, _, _, _, length, _, pst, _) in pa.up_box])
print(f'up pst mean: {s2.mean()} std: {s2.std()} max: {s2.max()} min: {s2.min()}')

pa.build_graph()
pa.fig.show()
