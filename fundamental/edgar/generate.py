import os
import sys
from fundamental.edgar.format import DATA_DIR, print_statement
from fundamental.edgar.templates import format_income, format_bs, format_cashflow


def print_stock(stock_name):
    source = os.path.join(DATA_DIR, '{}.json'.format(stock_name))
    if not os.path.exists(source):
        print('  skip {}: no source data'.format(stock_name))
        return

    income = format_income(stock_name)
    print_statement('INCOME STATEMENT (Annual)', income['annual'])
    print_statement('INCOME STATEMENT (Quarterly)', income['quarterly'])

    bs = format_bs(stock_name)
    print_statement('BALANCE SHEET (Annual)', bs['annual'])
    print_statement('BALANCE SHEET (Quarterly)', bs['quarterly'])

    cf = format_cashflow(stock_name)
    print_statement('CASHFLOW (Annual)', cf['annual'])
    print_statement('CASHFLOW (Quarterly)', cf['quarterly'])


def main():
    if len(sys.argv) > 1:
        for stock_name in sys.argv[1:]:
            print_stock(stock_name.upper())
    else:
        from conf import ALL
        for stock_name in ALL:
            print_stock(stock_name)


if __name__ == '__main__':
    main()
