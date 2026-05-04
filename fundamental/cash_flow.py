import sys
from fundamental.format import load_facts, extract_annual, extract_quarterly, print_statement

TEMPLATE = [
    ('OPERATING', []),
    ('  Net Income', ['NetIncomeLoss', 'ProfitLoss']),
    ('  D&A', ['DepreciationDepletionAndAmortization', 'DepreciationAndAmortization', 'Depreciation']),
    ('  SBC', ['ShareBasedCompensation', 'AllocatedShareBasedCompensationExpense']),
    ('  Deferred Tax', ['DeferredIncomeTaxExpenseBenefit', 'DeferredIncomeTaxesAndTaxCredits']),
    ('  Change In Receivables', ['IncreaseDecreaseInAccountsReceivable', 'IncreaseDecreaseInReceivables']),
    ('  Change In Inventory', ['IncreaseDecreaseInInventories']),
    ('  Change In Payables', ['IncreaseDecreaseInAccountsPayable']),
    ('  Other Operating', ['OtherNoncashIncomeExpense']),
    ('Operating Cash Flow', ['NetCashProvidedByUsedInOperatingActivities']),
    ('', []),
    ('INVESTING', []),
    ('  CapEx', ['PaymentsToAcquirePropertyPlantAndEquipment', 'PaymentsToAcquireProductiveAssets']),
    ('  Acquisitions', ['PaymentsToAcquireBusinessesNetOfCashAcquired']),
    ('  Purchase Of Investments',
     ['PaymentsToAcquireAvailableForSaleSecuritiesDebt', 'PaymentsToAcquireInvestments']),
    ('  Sale Of Investments',
     ['ProceedsFromSaleOfAvailableForSaleSecuritiesDebt', 'ProceedsFromSaleAndMaturityOfOtherInvestments',
      'ProceedsFromMaturitiesPrepaymentsAndCallsOfAvailableForSaleSecurities']),
    ('Investing Cash Flow', ['NetCashProvidedByUsedInInvestingActivities']),
    ('', []),
    ('FINANCING', []),
    ('  Debt Issuance', ['ProceedsFromIssuanceOfLongTermDebt', 'ProceedsFromDebtNetOfIssuanceCosts']),
    ('  Debt Repayment', ['RepaymentsOfLongTermDebt', 'RepaymentsOfDebt']),
    ('  Stock Issuance', ['ProceedsFromIssuanceOfCommonStock', 'ProceedsFromSaleOfTreasuryStock']),
    ('  Stock Repurchase', ['PaymentsForRepurchaseOfCommonStock']),
    ('  Dividends', ['PaymentsOfDividends', 'PaymentsOfDividendsCommonStock']),
    ('Financing Cash Flow', ['NetCashProvidedByUsedInFinancingActivities']),
    ('', []),
    ('Net Change In Cash',
     ['CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalentsPeriodIncreaseDecreaseIncludingExchangeRateEffect',
      'CashAndCashEquivalentsPeriodIncreaseDecrease']),
]


def format_cashflow(stock_name):
    us_gaap = load_facts(stock_name)
    annual = extract_annual(us_gaap, TEMPLATE)
    quarterly = extract_quarterly(us_gaap, TEMPLATE, is_period_data=True)
    return {'annual': annual, 'quarterly': quarterly}


def main():
    stock_name = sys.argv[1].upper()
    data = format_cashflow(stock_name)
    print_statement('CASHFLOW (Annual)', data['annual'])
    print_statement('CASHFLOW (Quarterly)', data['quarterly'])


if __name__ == '__main__':
    main()
