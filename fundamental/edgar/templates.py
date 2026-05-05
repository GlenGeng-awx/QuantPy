from fundamental.edgar.format import load_facts, extract_annual, extract_quarterly

INCOME_TEMPLATE = [
    ('Revenue', ['RevenueFromContractWithCustomerExcludingAssessedTax', 'Revenues', 'SalesRevenueNet',
                 'SalesRevenueGoodsNet', 'RevenuesNetOfInterestExpense', 'InterestAndDividendIncomeOperating']),
    ('Cost Of Revenue', ['CostOfGoodsAndServicesSold', 'CostOfRevenue', 'CostOfGoodsSold']),
    ('Gross Profit', ['GrossProfit']),
    ('Operating Expenses', []),
    ('  SG&A', ['SellingGeneralAndAdministrativeExpense']),
    ('  S&M', ['SellingAndMarketingExpense']),
    ('  G&A', ['GeneralAndAdministrativeExpense']),
    ('  R&D', ['ResearchAndDevelopmentExpense',
               'ResearchAndDevelopmentExpenseSoftwareExcludingAcquiredInProcessCost']),
    ('  Total Operating Expenses', ['OperatingExpenses', 'NoninterestExpense']),
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

BALANCE_SHEET_TEMPLATE = [
    ('ASSETS', []),
    ('  Cash', ['CashAndCashEquivalentsAtCarryingValue',
                'CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents']),
    ('  Short-Term Investments', ['ShortTermInvestments', 'MarketableSecuritiesCurrent',
                                  'AvailableForSaleSecuritiesDebtSecuritiesCurrent']),
    ('  Accounts Receivable', ['AccountsReceivableNetCurrent']),
    ('  Inventory', ['InventoryNet']),
    ('  Other Current Assets', ['OtherAssetsCurrent', 'PrepaidExpenseAndOtherAssetsCurrent']),
    ('Total Current Assets', ['AssetsCurrent']),
    ('  PP&E', ['PropertyPlantAndEquipmentNet',
                'PropertyPlantAndEquipmentAndFinanceLeaseRightOfUseAssetAfterAccumulatedDepreciationAndAmortization']),
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
    ('  Unearned Revenue', ['ContractWithCustomerLiabilityCurrent', 'DeferredRevenueCurrent']),
    ('  Other Current Liabilities', ['OtherLiabilitiesCurrent', 'AccruedLiabilitiesCurrent']),
    ('Total Current Liabilities', ['LiabilitiesCurrent']),
    ('  Long-Term Debt', ['LongTermDebtNoncurrent', 'LongTermDebt',
                          'DebtLongtermAndShorttermCombinedAmount']),
    ('  Other Non-Current Liabilities', ['OtherLiabilitiesNoncurrent']),
    ('Total Non-Current Liabilities', ['LiabilitiesNoncurrent']),
    ('TOTAL LIABILITIES', ['Liabilities']),
    ('', []),
    ('EQUITY', []),
    ('  Common Stock', ['CommonStocksIncludingAdditionalPaidInCapital', 'CommonStockValue']),
    ('  Additional Paid-In Capital', ['AdditionalPaidInCapital', 'AdditionalPaidInCapitalCommonStock']),
    ('  Treasury Stock', ['TreasuryStockValue', 'TreasuryStockCommonValue']),
    ('  Retained Earnings', ['RetainedEarningsAccumulatedDeficit']),
    ('  AOCI', ['AccumulatedOtherComprehensiveIncomeLossNetOfTax']),
    ('TOTAL EQUITY',
     ['StockholdersEquity', 'StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest']),
    ('TOTAL LIABILITIES + EQUITY', ['LiabilitiesAndStockholdersEquity']),
]

CASH_FLOW_TEMPLATE = [
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


# --- computed fields ---

def _fill_diff(rows, periods, target_label, a_label, b_label):
    target_row = next((r for r in rows if r['label'] == target_label), None)
    a_row = next((r for r in rows if r['label'] == a_label), None)
    b_row = next((r for r in rows if r['label'] == b_label), None)

    if not all([target_row, a_row, b_row]):
        return

    for period in periods:
        if target_row.get(period) is not None:
            continue
        a = a_row.get(period)
        b = b_row.get(period)
        if a is not None and b is not None:
            target_row[period] = a - b


def fill_income_computed(rows, periods):
    _fill_diff(rows, periods, 'Gross Profit', 'Revenue', 'Cost Of Revenue')


def fill_bs_computed(rows, periods):
    _fill_diff(rows, periods, 'TOTAL LIABILITIES', 'TOTAL ASSETS', 'TOTAL EQUITY')


# --- format functions ---

def format_income(stock_name):
    us_gaap = load_facts(stock_name)
    annual = extract_annual(us_gaap, INCOME_TEMPLATE)
    quarterly = extract_quarterly(us_gaap, INCOME_TEMPLATE, is_period_data=True, pit_fields=PIT_FIELDS)

    fill_income_computed(annual['rows'], annual['periods'])
    fill_income_computed(quarterly['rows'], quarterly['periods'])

    return {'annual': annual, 'quarterly': quarterly}


def format_bs(stock_name):
    us_gaap = load_facts(stock_name)
    annual = extract_annual(us_gaap, BALANCE_SHEET_TEMPLATE)
    quarterly = extract_quarterly(us_gaap, BALANCE_SHEET_TEMPLATE, is_period_data=False)

    fill_bs_computed(annual['rows'], annual['periods'])
    fill_bs_computed(quarterly['rows'], quarterly['periods'])

    return {'annual': annual, 'quarterly': quarterly}


def format_cashflow(stock_name):
    us_gaap = load_facts(stock_name)
    annual = extract_annual(us_gaap, CASH_FLOW_TEMPLATE)
    quarterly = extract_quarterly(us_gaap, CASH_FLOW_TEMPLATE, is_period_data=True)
    return {'annual': annual, 'quarterly': quarterly}
