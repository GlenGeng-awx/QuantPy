import pandas as pd
from glob import glob
from conf import ALL

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.float_format', '{:.3f}'.format)

df = pd.DataFrame()

for filename in glob('./bak/*'):
    # from ./bak/JNJ$2025-02-06$4 to JNJ$2025-02-06$4
    record = filename.split('/')[-1]
    stock_name, to_date, hit_num = record.split('$')

    if to_date not in df.columns:
        df[to_date] = pd.Series(dtype=str)

    df.at[stock_name, to_date] = int(hit_num)

# sort columns by date
df = df.reindex(sorted(df.columns, reverse=True)[:5], axis=1)

# sort rows by stock name
df = df.reindex(ALL, axis=0)

print(df)

candidates = [stock_name for stock_name in df.index if not df.loc[stock_name].dropna().empty]
print(candidates)
