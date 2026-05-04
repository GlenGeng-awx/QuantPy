import os
import sys
import json
from fundamental.format import DATA_DIR
from fundamental.income_statement import format_income
from fundamental.balance_sheet import format_bs
from fundamental.cash_flow import format_cashflow


def generate(stock_name):
    source = os.path.join(DATA_DIR, '{}.json'.format(stock_name))
    if not os.path.exists(source):
        print('  skip {}: no source data'.format(stock_name))
        return

    data = {
        'income': format_income(stock_name),
        'balance_sheet': format_bs(stock_name),
        'cash_flow': format_cashflow(stock_name),
    }

    output = os.path.join(DATA_DIR, '{}_statements.json'.format(stock_name))
    with open(output, 'w') as f:
        json.dump(data, f, indent=2)

    print('{}: done'.format(stock_name))


def main():
    if len(sys.argv) > 1:
        for stock_name in sys.argv[1:]:
            generate(stock_name.upper())
    else:
        from conf import ALL
        for stock_name in ALL:
            generate(stock_name)


if __name__ == '__main__':
    main()
