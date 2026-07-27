# 缩进规则：0 空格 = 主 subtotal，2 空格 = line item 或中间汇总，4 空格 = 子项
# ⚠ 2 空格项可能是汇总（非 line item），靠算验证，不能靠缩进判断
#    典型：Operating Expense = R&D + SGA + Restructuring + 其他（汇总，非 line item）

INCOME_FIELDS = [
    '  Total Revenue',
    '  Cost Of Revenue',
    'Gross Profit',                  # = Revenue − COGS
    '',
    '  Research And Development',
    '  Selling General And Administration',
    '    Selling And Marketing Expense',
    '    General And Administrative Expense',
    '  Restructuring And Mergern Acquisition',
    '  Operating Expense',           # ← 汇总：R&D + SGA + Restructuring + 其他；非 line item
    'Operating Income',              # = Gross Profit − Operating Expense
    '',
    '  Interest Expense',
    '  Other Income Expense',
    '    Gain On Sale Of Security',
    'Pretax Income',                 # = Operating Income − Interest + Other Income
    '  Tax Provision',
    'Net Income',                    # = Pretax − Tax
    '',
    '  Total Unusual Items',         # ← line item（非汇总），工具标记的一次性项
    'Normalized Income',             # = NI − Unusual（近似）
    '',
    '  Basic EPS',
    '  Diluted EPS',
    '  Basic Average Shares',
    '  Diluted Average Shares',
    '',
    'EBITDA',                        # = Operating Income + D&A（近似）
    '  Reconciled Depreciation',
]

BS_FIELDS = [
    '  Cash And Cash Equivalents',
    '  Other Short Term Investments',
    'Cash Cash Equivalents And Short Term Investments',  # = Cash + Other ST Inv
    '  Restricted Cash',
    '  Accounts Receivable',
    '  Inventory',
    '  Other Current Assets',
    'Current Assets',                 # = 上面所有流动资产
    '',
    '  Net PPE',
    '  Goodwill',
    '  Other Intangible Assets',
    'Goodwill And Other Intangible Assets',  # = Goodwill + Other Intangibles
    '  Long Term Equity Investment',
    '  Other Non Current Assets',
    'Total Non Current Assets',       # = 上面所有非流动资产
    '',
    'Total Assets',                   # = Current + Non-Current
    '',
    '  Accounts Payable',
    '  Current Debt',
    '  Current Deferred Revenue',
    '  Other Current Liabilities',
    'Current Liabilities',            # = 上面所有流动负债
    '',
    '  Long Term Debt',
    '  Capital Lease Obligations',
    '  Other Non Current Liabilities',
    'Total Non Current Liabilities Net Minority Interest',
    '',
    'Total Liabilities Net Minority Interest',  # = Current + Non-Current Liabilities
    '  Total Debt',                   # ← 汇总：Current Debt + Long Term Debt + Capital Lease；非 line item
    '',
    '  Common Stock',
    '  Additional Paid In Capital',
    '  Treasury Stock',
    '  Retained Earnings',
    '  Gains Losses Not Affecting Retained Earnings',
    '  Ordinary Shares Number',
    'Stockholders Equity',            # = 上面所有权益项
    '',
    'Total Equity Gross Minority Interest',  # = Stockholders Equity + Minority Interest
    '',
    'Working Capital',                # = Current Assets − Current Liabilities
]

CF_FIELDS = [
    '  Net Income From Continuing Operations',
    '  Depreciation And Amortization',
    '  Stock Based Compensation',
    '  Deferred Tax',
    '  Change In Receivables',
    '  Change In Inventory',
    '  Change In Payables And Accrued Expense',
    '  Change In Prepaid Assets',
    '  Change In Other Working Capital',   # ← 常为大额（如 ORCL Q4 +$4.4B），不能漏
    '  Change In Working Capital',         # ← 汇总：上面所有 WC 变动；非 line item
    'Operating Cash Flow',                 # = NI + D&A + SBC + 各项变动调整
    '',
    '  Capital Expenditure',
    '  Net Business Purchase And Sale',
    '  Purchase Of Investment',
    '  Sale Of Investment',
    'Investing Cash Flow',            # = 上面所有投资项
    '',
    '  Issuance Of Debt',
    '  Repayment Of Debt',
    '  Common Stock Issuance',
    '  Repurchase Of Capital Stock',
    '  Common Stock Dividend Paid',
    'Financing Cash Flow',            # = 上面所有融资项
    '',
    'Changes In Cash',                # = OCF + Investing CF + Financing CF
    'Free Cash Flow',                 # = OCF − CapEx
    '',
    '  Interest Paid Supplemental Data',
    '  Income Tax Paid Supplemental Data',
]
