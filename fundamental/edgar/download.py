import os
import json
import time
import requests
from conf import ALL, CN_INDEX, US_INDEX

DATA_DIR = 'financial_data/edgar'
SEC_HEADERS = {'User-Agent': 'john@example.com'}


def load_cik_map():
    response = requests.get('https://www.sec.gov/files/company_tickers.json', headers=SEC_HEADERS)
    tickers = response.json()
    cik_map = {}
    for entry in tickers.values():
        ticker = entry['ticker']
        cik = entry['cik_str']
        cik_map[ticker] = str(cik).zfill(10)
    return cik_map


def download(stock_name, cik):
    url = 'https://data.sec.gov/api/xbrl/companyfacts/CIK{}.json'.format(cik)
    response = requests.get(url, headers=SEC_HEADERS)
    if response.status_code != 200:
        print('  skip {}: HTTP {}'.format(stock_name, response.status_code))
        return False

    data = response.json()
    us_gaap = data.get('facts', {}).get('us-gaap', {})

    key_fields = {'Revenues', 'NetIncomeLoss', 'Assets', 'ProfitLoss'}
    if not (key_fields & set(us_gaap.keys())):
        print('  skip {}: no us-gaap key fields'.format(stock_name))
        return False

    path = os.path.join(DATA_DIR, '{}.json'.format(stock_name))
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)

    return True


def main():
    os.makedirs(DATA_DIR, exist_ok=True)

    print('loading CIK map...')
    cik_map = load_cik_map()

    skip = set(CN_INDEX + US_INDEX)
    for stock_name in ALL:
        if stock_name in skip:
            continue
        ticker = stock_name.split('.')[0]
        cik = cik_map.get(ticker) or cik_map.get(stock_name)
        if not cik:
            print('  skip {}: no CIK'.format(stock_name))
            continue

        ok = download(stock_name, cik)
        if ok:
            print('{}: done'.format(stock_name))

        time.sleep(0.1)


if __name__ == '__main__':
    main()
