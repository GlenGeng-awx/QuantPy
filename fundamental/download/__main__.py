import os
import sys
import json
import yfinance as yf
from conf import ALL
from fundamental.data import STATEMENT_DIR, PRICE_DIR, SKIP

STATEMENTS = [
    ('income_annual', 'financials'),
    ('income_quarterly', 'quarterly_financials'),
    ('income_ttm', 'ttm_financials'),
    ('bs_annual', 'balance_sheet'),
    ('bs_quarterly', 'quarterly_balance_sheet'),
    ('cf_annual', 'cashflow'),
    ('cf_quarterly', 'quarterly_cashflow'),
    ('cf_ttm', 'ttm_cashflow'),
]

def download_statements(stock_name, ticker):
    stock_dir = os.path.join(STATEMENT_DIR, stock_name)
    os.makedirs(stock_dir, exist_ok=True)
    for filename, attr in STATEMENTS:
        df = getattr(ticker, attr)
        if df is not None and not df.empty:
            df.to_csv(os.path.join(stock_dir, '{}.csv'.format(filename)))


def download_info(stock_name, ticker):
    stock_dir = os.path.join(STATEMENT_DIR, stock_name)
    os.makedirs(stock_dir, exist_ok=True)
    info = ticker.info
    if info:
        with open(os.path.join(stock_dir, 'info.json'), 'w') as f:
            json.dump(info, f, indent=2)


def download_price(stock_name, ticker):
    path = os.path.join(PRICE_DIR, '{}_1d.csv'.format(stock_name))
    df = ticker.history(start='2015-01-01', end='2030-01-01', interval='1d')
    if df is not None and not df.empty:
        df.index.name = 'Date'
        df.columns = df.columns.str.lower()
        df.to_csv(path)


def download(stock_name):
    print(stock_name)
    ticker = yf.Ticker(stock_name)

    try:
        download_price(stock_name, ticker)
        if stock_name in SKIP:
            return
        download_statements(stock_name, ticker)
        download_info(stock_name, ticker)
    except Exception as e:
        print('  skip {}: {}'.format(stock_name, e))


def main():
    if len(sys.argv) > 1:
        for stock_name in sys.argv[1:]:
            download(stock_name.upper())
    else:
        for stock_name in ALL:
            download(stock_name)


if __name__ == '__main__':
    main()
