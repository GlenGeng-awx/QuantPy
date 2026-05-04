import sys
from fundamental.format import load_facts, extract_annual, extract_quarterly, print_statement

TEMPLATE = [
    ('Revenue', ['RevenueFromContractWithCustomerExcludingAssessedTax', 'Revenues', 'SalesRevenueNet',
                 'SalesRevenueGoodsNet', 'RevenuesNetOfInterestExpense', 'InterestAndDividendIncomeOperating']),
    ('Cost Of Revenue', ['CostOfGoodsAndServicesSold', 'CostOfRevenue', 'CostOfGoodsSold']),
    ('Gross Profit', ['GrossProfit']),
    ('Operating Expenses', []),
    ('  R&D', ['ResearchAndDevelopmentExpense']),
    ('  SG&A', ['SellingGeneralAndAdministrativeExpense']),
    ('  Total Operating Expenses', ['OperatingExpenses', 'CostsAndExpenses', 'NoninterestExpense']),
    ('Operating Income', [
        'OperatingIncomeLoss',
        'IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest',
    ]),
    ('Interest Expense', ['InterestExpense', 'InterestExpenseDebt']),
    ('Other Income / (Expense)', ['NonoperatingIncomeExpense', 'OtherNonoperatingIncomeExpense']),
    ('Pretax Income', [
        'IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest',
        'IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments',
    ]),
    ('Income Tax', ['IncomeTaxExpenseBenefit']),
    ('Net Income', ['NetIncomeLoss', 'ProfitLoss', 'NetIncomeLossAvailableToCommonStockholdersBasic']),
    ('EPS Basic', ['EarningsPerShareBasic']),
    ('EPS Diluted', ['EarningsPerShareDiluted']),
    ('Shares Basic', ['WeightedAverageNumberOfSharesOutstandingBasic']),
    ('Shares Diluted', ['WeightedAverageNumberOfDilutedSharesOutstanding']),
    ('D&A', ['DepreciationDepletionAndAmortization', 'DepreciationAndAmortization', 'Depreciation']),
    ('SBC', ['ShareBasedCompensation', 'AllocatedShareBasedCompensationExpense']),
]

PIT_FIELDS = {
    'EarningsPerShareBasic', 'EarningsPerShareDiluted',
    'WeightedAverageNumberOfSharesOutstandingBasic', 'WeightedAverageNumberOfDilutedSharesOutstanding',
}


def format_income(stock_name):
    us_gaap = load_facts(stock_name)
    annual = extract_annual(us_gaap, TEMPLATE)
    quarterly = extract_quarterly(us_gaap, TEMPLATE, is_period_data=True, pit_fields=PIT_FIELDS)
    return {'annual': annual, 'quarterly': quarterly}


def main():
    stock_name = sys.argv[1].upper()
    data = format_income(stock_name)
    print_statement('INCOME STATEMENT (Annual)', data['annual'])
    print_statement('INCOME STATEMENT (Quarterly)', data['quarterly'])


if __name__ == '__main__':
    main()
