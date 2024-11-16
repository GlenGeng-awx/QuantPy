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
DELl = "DELL"           # Dell Technologies

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
TCOM = "TCOM"
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

NASDAQ_GIANTS = [
    IXIC,
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
]

NASDAQ_SEMI_CONDUCT = [
    ASML,
    AMD,
    TSM,
    INTC,
]

NASDAQ_OTHER = [
    ZM,
    BA,
    SQ,
    PINS,
    RIVN,
    ADBE,
    WMT,
    JPM,
    XOM,
    NVO,
    MA,
    PG,
    JNJ,
    LVMUY,
    KO,
    BAC,
    CVX,
    DELl,
    PLTR,
    MRNA,
    PFE,
    COIN,
    EBAY,
    SNOW,
    BNTX,
    SNAP,
    TTD,
    MCD,
    GILD,
    TCOM,
    MRK,
    DIS,
    SEA,
    ERIC,
    UBER,
    OKTA,
    CFLT,
    QCOM,
    ETSY,
    SHOP,
    GTLB,
]

NASDAQ_CN = [
    SS_000300,
    SS_000001,
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
]

HK = [
    HK_0700,
    HK_1211,
]

ALL = HK + NASDAQ_CN + NASDAQ_OTHER + NASDAQ_SEMI_CONDUCT + NASDAQ_GIANTS
