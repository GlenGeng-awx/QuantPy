import json
import pandas as pd
from datetime import datetime


def parse_request(event: dict) -> dict:
    return event['payload']['response']['BatchAccountOperation']['request']


def parse_results(event: dict) -> list:
    return event['payload']['response']['BatchAccountOperation']['results']


def parse_create_account_op(op):
    create_account_op = op['operation']['CreateAccount']

    account_id = create_account_op['account_id']
    currency = create_account_op['asset_class']['asset_class']['Cash']['currency']
    metadata = create_account_op['metadata']

    return account_id, currency, metadata


def parse_adjust_balance_result(result):
    adjust_balance_result = result['result']['AdjustBalanceResult']

    prev_account = adjust_balance_result['account_change']['prev_account']
    curr_account = adjust_balance_result['account_change']['curr_account']

    prev_balance = prev_account['balance']['available']
    curr_balance = curr_account['balance']['available']

    adjust_balance_op = adjust_balance_result['adjust_balance']

    account_id = adjust_balance_op['account_id']
    currency = adjust_balance_op['currency']
    amount = adjust_balance_op['amount']

    return account_id, currency, amount, prev_balance, curr_balance


def parse_row(row: pd.Series):
    sequence_number, event, create_time_in_ms = row['sequence_number'], row['event'], row['create_time']

    event = json.loads(event)
    date = datetime.fromtimestamp(int(create_time_in_ms) / 1000).strftime('%Y-%m-%d')

    request = parse_request(event)
    account_operations = request['account_operations']
    drill_down = [real_op for account_operation in account_operations for real_op in account_operation['operation']]

    return sequence_number, date, drill_down, account_operations, event


df = pd.read_csv('/Users/glen.geng//Downloads/INFRASUP-10579.csv')

# scan
for _, row in df.iterrows():
    sequence_number, date, drill_down, _, _ = parse_row(row)

    if drill_down != ['AdjustBalance', 'AdjustBalance']:
        print(f"{sequence_number} at {date} -> {', '.join(drill_down)}")

# build account map
account_map = {}

for _, row in df.iterrows():
    sequence_number, date, drill_down, account_operations, _ = parse_row(row)

    if all([op == 'CreateAccount' for op in drill_down]):
        print(f"{sequence_number} at {date} -> {', '.join(drill_down)}")

        for account_operation in account_operations:
            account_id, currency, metadata = parse_create_account_op(account_operation)
            print(f'CreateAccount -> {account_id}, {currency}, {metadata}')
            account_map[account_id] = metadata

# parse report
for _, row in df.iterrows():
    sequence_number, date, drill_down, _, event = parse_row(row)

    if all([op == 'AdjustBalance' for op in drill_down]) and len(drill_down) > 2:
        print(f"{sequence_number} at {date} -> {', '.join(drill_down)}")

        results = parse_results(event)
        for result in results:
            account_id, currency, amount, prev_balance, curr_balance = parse_adjust_balance_result(result)

            if float(amount) == 0:
                continue
            print(f'AdjustBalance -> {account_map[account_id]} adjust {amount}, from {prev_balance} to {curr_balance}')
