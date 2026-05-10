"""
Usage:
    python3 -m fundamental.edgar.download            # download raw XBRL data
    python3 -m fundamental.edgar.download AAPL       # download raw XBRL data for one stock

    python3 -m fundamental.edgar.generate            # print all statements for all stocks
    python3 -m fundamental.edgar.generate AAPL       # print all statements for one stock

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

Known data quality issues:

1. Dual currency units (ADR companies):
   EarningsPerShareDiluted may have both CNY/shares and USD/shares units.
   Must select USD/shares to match USD stock price.

2. Per-ordinary-share vs per-ADS EPS (ADR companies):
   USD/shares values are per ordinary share, not per ADS.
   Must multiply by ADS ratio (e.g. BABA×8, JD×2, PDD×4) to match stock price.
   ADS ratios are configured in conf.py:ADS_RATIO.

3. Stock splits (e.g. GOOG 1:20 in 2022):
   Same period may have both pre-split and post-split values from different filings.
   Take latest-filed value, then divide by split ratio if filed before the split.
   Split ratios configured in conf.py:STOCK_SPLITS with a cutoff_month per split.
   Some companies (e.g. NFLX) don't adjust XBRL data in post-split 10-Q filings,
   so cutoff_month may be later than the actual split date.

4. Sparse quarterly data (Chinese ADRs like BABA, JD, PDD):
   Many foreign private issuers file 20-F (annual) only, with no 6-K quarterly.
   TTM EPS cannot be computed; fall back to static FY-based P/E with (static) label.

5. fp field may be None:
   Some entries have fp=None. Guard with (e.get('fp') or '').startswith('Q').

6. YTD vs single-quarter EPS in 10-Q:
   A single 10-Q filing contains both YTD cumulative EPS (longer period)
   and single-quarter EPS (shorter period). Identify YTD by earliest start date.
   TTM = current_YTD - prior_year_same_period_YTD + prior_FY_EPS.

7. 10-K includes non-annual periods:
   A 10-K filing contains Q4 single-quarter and comparison periods alongside
   the full-year data. Filter by period length >= 300 days for annual values.
"""
