import sys
from fundamental.format import load_facts, extract_annual, extract_quarterly, print_statement

TEMPLATE = [
    ('ASSETS', []),
    ('  Cash', ['CashAndCashEquivalentsAtCarryingValue']),
    ('  Short-Term Investments', ['ShortTermInvestments', 'MarketableSecuritiesCurrent',
                                  'AvailableForSaleSecuritiesDebtSecuritiesCurrent']),
    ('  Accounts Receivable', ['AccountsReceivableNetCurrent']),
    ('  Inventory', ['InventoryNet']),
    ('  Other Current Assets', ['OtherAssetsCurrent', 'PrepaidExpenseAndOtherAssetsCurrent']),
    ('Total Current Assets', ['AssetsCurrent']),
    ('  PP&E', ['PropertyPlantAndEquipmentNet']),
    ('  Goodwill', ['Goodwill']),
    ('  Intangible Assets', ['IntangibleAssetsNetExcludingGoodwill', 'FiniteLivedIntangibleAssetsNet']),
    ('  Long-Term Investments', ['MarketableSecuritiesNoncurrent', 'LongTermInvestments']),
    ('  Other Non-Current Assets', ['OtherAssetsNoncurrent']),
    ('Total Non-Current Assets', ['AssetsNoncurrent', 'NoncurrentAssets']),
    ('TOTAL ASSETS', ['Assets']),
    ('', []),
    ('LIABILITIES', []),
    ('  Accounts Payable', ['AccountsPayableCurrent']),
    ('  Short-Term Debt', ['ShortTermBorrowings', 'CommercialPaper']),
    ('  Current Long-Term Debt', ['LongTermDebtCurrent']),
    ('  Deferred Revenue', ['ContractWithCustomerLiabilityCurrent', 'DeferredRevenueCurrent']),
    ('  Other Current Liabilities', ['OtherLiabilitiesCurrent', 'AccruedLiabilitiesCurrent']),
    ('Total Current Liabilities', ['LiabilitiesCurrent']),
    ('  Long-Term Debt', ['LongTermDebtNoncurrent', 'LongTermDebt']),
    ('  Other Non-Current Liabilities', ['OtherLiabilitiesNoncurrent']),
    ('Total Non-Current Liabilities', ['LiabilitiesNoncurrent']),
    ('TOTAL LIABILITIES', ['Liabilities']),
    ('', []),
    ('EQUITY', []),
    ('  Common Stock', ['CommonStocksIncludingAdditionalPaidInCapital', 'CommonStockValue']),
    ('  Retained Earnings', ['RetainedEarningsAccumulatedDeficit']),
    ('  AOCI', ['AccumulatedOtherComprehensiveIncomeLossNetOfTax']),
    ('TOTAL EQUITY',
     ['StockholdersEquity', 'StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest']),
    ('TOTAL LIABILITIES + EQUITY', ['LiabilitiesAndStockholdersEquity']),
]


def fill_computed_fields(rows, periods):
    # many companies don't report Liabilities tag, compute as Assets - Equity
    assets_row = next((r for r in rows if r['label'] == 'TOTAL ASSETS'), None)
    equity_row = next((r for r in rows if r['label'] == 'TOTAL EQUITY'), None)
    liabilities_row = next((r for r in rows if r['label'] == 'TOTAL LIABILITIES'), None)

    if not all([assets_row, equity_row, liabilities_row]):
        return

    for period in periods:
        if liabilities_row.get(period) is not None:
            continue
        assets = assets_row.get(period)
        equity = equity_row.get(period)
        if assets is not None and equity is not None:
            liabilities_row[period] = assets - equity


def format_bs(stock_name):
    us_gaap = load_facts(stock_name)
    annual = extract_annual(us_gaap, TEMPLATE)
    quarterly = extract_quarterly(us_gaap, TEMPLATE, is_period_data=False)

    fill_computed_fields(annual['rows'], annual['periods'])
    fill_computed_fields(quarterly['rows'], quarterly['periods'])

    return {'annual': annual, 'quarterly': quarterly}


def main():
    stock_name = sys.argv[1].upper()
    data = format_bs(stock_name)
    print_statement('BALANCE SHEET (Annual)', data['annual'])
    print_statement('BALANCE SHEET (Quarterly)', data['quarterly'])


if __name__ == '__main__':
    main()
