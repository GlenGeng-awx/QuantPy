IXIC = "^IXIC"
SS_000300 = "000300.SS"
SS_000001 = "000001.SS"
GC_F = "GC=F"

GOOG = "GOOG"
AMZN = "AMZN"
PYPL = "PYPL"           # PayPal
AAPL = "AAPL"
NFLX = "NFLX"
MSFT= "MSFT"            # Microsoft
ASML = "ASML"
WMT = "WMT"             # Walmart
JPM = "JPM"             # JPMorgan
XOM = "XOM"             # Exxon Mobil
NVO = "NVO"             # Novo Nordisk
ORCL = "ORCL"           # Oracle
MA = "MA"               # Mastercard
PG = "PG"               # Procter & Gamble
JNJ = "JNJ"             # Johnson & Johnson
LVMUY = "LVMUY"         # LVMH Moët Hennessy Louis Vuitton
KO = "KO"               # Coca-Cola
BAC = "BAC"             # Bank of America
CVX = "CVX"             # Chevron
DELL = "DELL"           # Dell Technologies

TSLA = "TSLA"
RIVN = "RIVN"
LI = "LI"
XPEV = "XPEV"

MRNA = "MRNA"
BNTX = "BNTX"

PDD = "PDD"
COIN = "COIN"
META = "META"
PLTR = "PLTR"
SNOW = "SNOW"

NVDA = "NVDA"
AMD = "AMD"
TSM = "TSM"             # Taiwan Semiconductor Manufacturing Company
BA = "BA"

ZM = "ZM"
SNAP = "SNAP"
EBAY = "EBAY"
IQ = "IQ"

HK_0700 = "0700.HK"     # Tencent
HK_1211 = "1211.HK"     # BYD
BABA = "BABA"
JD = "JD"
BEKE = "BEKE"
MNSO = "MNSO"
BILI = "BILI"
EDU = "EDU"
CPNG = "CPNG"
FUTU = "FUTU"

TTD = "TTD"             # The Trade Desk
NIO = "NIO"
YY = "YY"
MCD = "MCD"             # McDonald's
PFE = "PFE"             # Pfizer
GILD = "GILD"
TCOM = "TCOM"           # Trip.com
MRK = "MRK"             # Merck & Co.
ADBE = "ADBE"
DIS = "DIS"
TME = "TME"             # Tencent Music Entertainment Group
GS = "GS"               # Goldman Sachs
SEA = "SE"
ERIC = "ERIC"
UBER = "UBER"
INTC = "INTC"
MS = "MS"               # Morgan Stanley
OKTA = "OKTA"
CFLT = "CFLT"
QCOM = "QCOM"           # Qualcomm
ETSY = "ETSY"
SHOP = "SHOP"
GTLB = "GTLB"
PINS = "PINS"           # Pinterest
SQ = "SQ"

INDEX = [
    IXIC,
    SS_000300,
    SS_000001,
]

NASDAQ_GIANTS = [
    GOOG,
    AMZN,
    AAPL,
    META,
    MSFT,
    NVDA,
    NFLX,
    ORCL,
    TSLA,
    PYPL,
    GS,
    MS,
    JPM,
]

NASDAQ_SEMI_CONDUCT = [
    ASML,
    AMD,
    TSM,
    INTC,
    QCOM,
]

NASDAQ_MEDICAL = [
    NVO,
    JNJ,
    MRNA,
    PFE,
    BNTX,
    GILD,
]

NASDAQ_OTHER = [
    ZM,
    BA,
    SQ,
    PINS,
    RIVN,
    ADBE,
    WMT,
    XOM,
    MA,
    PG,
    LVMUY,
    KO,
    BAC,
    CVX,
    DELL,
    PLTR,
    COIN,
    EBAY,
    SNOW,
    SNAP,
    TTD,
    MCD,
    MRK,
    DIS,
    SEA,
    ERIC,
    UBER,
    OKTA,
    CFLT,
    ETSY,
    SHOP,
    GTLB,
]

NASDAQ_CN = [
    IQ,
    BILI,
    CPNG,
    NIO,
    XPEV,
    LI,
    PDD,
    BABA,
    JD,
    FUTU,
    MNSO,
    BEKE,
    EDU,
    YY,
    TME,
    TCOM,
]

HK = [
    HK_0700,
    # HK_1211,
]

ALL = INDEX + HK + NASDAQ_CN + NASDAQ_OTHER + NASDAQ_SEMI_CONDUCT + NASDAQ_GIANTS + NASDAQ_MEDICAL
