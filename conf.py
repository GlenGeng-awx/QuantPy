IXIC = "^IXIC"
QQQ = "QQQ"
KWEB = "KWEB"
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

LLY = "LLY"             # Eli Lilly And Co
AVGO = "AVGO"           # Broadcom Inc

INDEX = [
    IXIC,
    QQQ,
    KWEB,
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
    AVGO,
]

NASDAQ_MEDICAL = [
    NVO,
    JNJ,
    MRNA,
    PFE,
    BNTX,
    GILD,
    LLY,
    MRK,
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

V_INDEX = [
    QQQ,
    KWEB,
    SS_000300,
]

V_3000B = [
    MSFT,
    AAPL,
    NVDA,
]

V_2000B = [
    GOOG,
    AMZN,
]

V_1000B = [
    META,
    TSLA,
    TSM,
    AVGO,
]

v_500B = [
    NFLX,
    JPM,
    ASML,
    LLY,
    WMT,
    MA,
    HK_0700,
]

V_300B = [
    ORCL,
    NVO,
    JNJ,
    XOM,
    PG,
    KO,
    BAC,
    BABA,
]

V_200B = [
    GS,
    MS,
    MRK,
    ADBE,
    CVX,
    PLTR,
    MCD,
    DIS,
]

V_100B = [
    AMD,
    INTC,
    QCOM,
    PFE,
    GILD,
    BA,
    UBER,
    SHOP,
    PDD,
]

CANDIDATES = V_INDEX + V_3000B + V_2000B + V_1000B + v_500B + V_300B + V_200B + V_100B