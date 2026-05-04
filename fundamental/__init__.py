"""
SEC EDGAR XBRL data format (companyfacts API):

    {
      "start": "2006-10-01",      # accounting period start (absent for point-in-time data like balance sheet)
      "end": "2007-09-29",        # accounting period end (or point-in-time date)
      "val": 5470000000,
      "accn": "0001193125-09-214859",
      "fy": 2009,                 # fiscal year
      "fp": "FY",                 # fiscal period: FY, Q1, Q2, Q3
      "form": "10-K",             # filing type (see below)
      "filed": "2009-10-27"       # date the filing was posted
    }

Filing types:
    10-K / 10-Q  — annual / quarterly reports for US-domiciled companies
    20-F / 6-K   — annual / quarterly reports for foreign private issuers (e.g. Chinese ADRs)

Each accounting period may appear in multiple filings (e.g. a 10-K restates
prior years for comparison). We take the entry with the latest "filed" date
to get the most up-to-date figure.
"""
