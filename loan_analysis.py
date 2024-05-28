import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.float_format', '{:.0f}'.format)


def calculate_loan(total_amount, month_num, loan_rate):
    principle = total_amount / month_num

    items = []
    left_amount = total_amount

    for i in range(month_num):
        interest = left_amount * loan_rate / 12
        left_amount -= principle
        items.append(interest + principle)

    return pd.Series(items)


df = pd.DataFrame()

# calculate loss 373
df['373_4.1'] = calculate_loan(3_730_000, 240, 0.041)
df['373_3.85'] = calculate_loan(3_730_000, 240, 0.0385)
df['373_3.5'] = calculate_loan(3_730_000, 240, 0.035)

loss_373 = []
for index, row in df.iterrows():
    if index < 12:
        loss_373.append(row['373_4.1'] - row['373_3.5'])
    else:
        loss_373.append(row['373_3.85'] - row['373_3.5'])

df['loss_373'] = pd.Series(loss_373)

# calculate loss 100
df['100_3.1'] = calculate_loan(1_000_000, 240, 0.031)
df['100_2.85'] = calculate_loan(1_000_000, 240, 0.0285)

loss_100 = []
for index, row in df.iterrows():
    if index < 12:
        loss_100.append(row['100_3.1'] - row['100_2.85'])
    else:
        loss_100.append(0)

df['loss_100'] = pd.Series(loss_100)

print(df)
print(df['loss_373'].sum(), df['loss_100'].sum())
