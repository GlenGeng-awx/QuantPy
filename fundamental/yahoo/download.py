import os
import sys
import yfinance as yf
from conf import ALL, CN_INDEX, US_INDEX

DATA_DIR = 'financial_data/yahoo'
SKIP = set(CN_INDEX + US_INDEX)

STATEMENTS = [
    ('income_annual', 'financials'),
    ('income_quarterly', 'quarterly_financials'),
    ('bs_annual', 'balance_sheet'),
    ('bs_quarterly', 'quarterly_balance_sheet'),
    ('cf_annual', 'cashflow'),
    ('cf_quarterly', 'quarterly_cashflow'),
]


def download(stock_name):
    if stock_name in SKIP:
        return

    ticker = yf.Ticker(stock_name)
    stock_dir = os.path.join(DATA_DIR, stock_name)
    os.makedirs(stock_dir, exist_ok=True)

    try:
        for filename, attr in STATEMENTS:
            df = getattr(ticker, attr)
            if df is not None and not df.empty:
                df.to_csv(os.path.join(stock_dir, '{}.csv'.format(filename)))
    except Exception as e:
        print('  skip {}: {}'.format(stock_name, e))
        return

    income = ticker.financials
    if income is None or income.empty:
        print('  skip {}: no data'.format(stock_name))
        return

    a_periods = len(income.columns)
    q_periods = len(ticker.quarterly_financials.columns) if ticker.quarterly_financials is not None else 0
    print('{}: {} annual, {} quarterly'.format(stock_name, a_periods, q_periods))


def main():
    os.makedirs(DATA_DIR, exist_ok=True)

    if len(sys.argv) > 1:
        for stock_name in sys.argv[1:]:
            download(stock_name.upper())
    else:
        for stock_name in ALL:
            download(stock_name)


if __name__ == '__main__':
    main()
