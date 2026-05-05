import sys
from fundamental.yahoo.format import load_csv, print_statement
from fundamental.yahoo.templates import INCOME_FIELDS, BS_FIELDS, CF_FIELDS


def print_stock(stock_name):
    print_statement('INCOME STATEMENT (Annual)',
                    load_csv(stock_name, 'income_annual'), INCOME_FIELDS)
    print_statement('INCOME STATEMENT (Quarterly)',
                    load_csv(stock_name, 'income_quarterly'), INCOME_FIELDS)
    print_statement('BALANCE SHEET (Annual)',
                    load_csv(stock_name, 'bs_annual'), BS_FIELDS)
    print_statement('BALANCE SHEET (Quarterly)',
                    load_csv(stock_name, 'bs_quarterly'), BS_FIELDS)
    print_statement('CASHFLOW (Annual)',
                    load_csv(stock_name, 'cf_annual'), CF_FIELDS)
    print_statement('CASHFLOW (Quarterly)',
                    load_csv(stock_name, 'cf_quarterly'), CF_FIELDS)


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
