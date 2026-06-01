import sys
import pandas as pd
from fundamental.data import load_statement, format_value
from fundamental.statements.templates import INCOME_FIELDS, BS_FIELDS, CF_FIELDS


def print_statement(title, df, fields):
    print('\n===== {} ====='.format(title))
    if df.empty:
        print('  No data')
        return

    periods = [col if col.startswith('TTM') else col[:7] for col in df.columns]
    col_width = 14
    label_width = 52

    header = '{:<{w}}'.format('', w=label_width)
    for period in periods:
        header += '{:>{w}}'.format(period, w=col_width)
    print(header)
    print('-' * len(header))

    for field in fields:
        if not field:
            print()
            continue
        key = field.strip()
        line = '{:<{w}}'.format(field, w=label_width)
        for col in df.columns:
            val = df.loc[key, col] if key in df.index else None
            line += '{:>{w}}'.format(format_value(val), w=col_width)
        print(line)


def merge_ttm(annual, ttm):
    if ttm.empty:
        return annual
    if annual.empty:
        return ttm
    date = ttm.columns[0][:7] if ttm.columns[0] != 'TTM' else 'TTM'
    ttm.columns = ['TTM({})'.format(date)]
    return pd.concat([ttm, annual], axis=1)


def print_stock(stock_name):
    income_annual = merge_ttm(load_statement(stock_name, 'income_annual'),
                              load_statement(stock_name, 'income_ttm'))
    income_quarterly = load_statement(stock_name, 'income_quarterly')
    cf_annual = merge_ttm(load_statement(stock_name, 'cf_annual'),
                          load_statement(stock_name, 'cf_ttm'))
    cf_quarterly = load_statement(stock_name, 'cf_quarterly')
    bs_annual = load_statement(stock_name, 'bs_annual')
    bs_quarterly = load_statement(stock_name, 'bs_quarterly')

    print_statement('{} INCOME (Annual)'.format(stock_name), income_annual, INCOME_FIELDS)
    print_statement('{} INCOME (Quarterly)'.format(stock_name), income_quarterly, INCOME_FIELDS)
    print_statement('{} CASHFLOW (Annual)'.format(stock_name), cf_annual, CF_FIELDS)
    print_statement('{} CASHFLOW (Quarterly)'.format(stock_name), cf_quarterly, CF_FIELDS)
    print_statement('{} BALANCE SHEET (Annual)'.format(stock_name), bs_annual, BS_FIELDS)
    print_statement('{} BALANCE SHEET (Quarterly)'.format(stock_name), bs_quarterly, BS_FIELDS)


def main():
    if len(sys.argv) > 1:
        for stock_name in sys.argv[1:]:
            print_stock(stock_name.upper())
    else:
        from conf import ALL
        from fundamental.data import SKIP
        for stock_name in ALL:
            if stock_name not in SKIP:
                print_stock(stock_name)


if __name__ == '__main__':
    main()
