# INDEX
IXIC = "^IXIC"
QQQ = "QQQ"
KWEB = "KWEB"
SS_000300 = "000300.SS"
SS_000001 = "000001.SS"

# SEVEN GIANTS
AAPL = "AAPL"
MSFT = "MSFT"           # Microsoft
NVDA = "NVDA"
GOOG = "GOOG"
AMZN = "AMZN"
TSLA = "TSLA"
META = "META"

# TECHNOLOGY
NFLX = "NFLX"
PLTR = "PLTR"
SNOW = "SNOW"
ZM = "ZM"
SNAP = "SNAP"
TTD = "TTD"             # The Trade Desk
UBER = "UBER"
OKTA = "OKTA"
CFLT = "CFLT"
ETSY = "ETSY"
SHOP = "SHOP"
GTLB = "GTLB"
PINS = "PINS"           # Pinterest
BLOCK = "XYZ"
COIN = "COIN"
LVMUY = "LVMUY"         # LVMH Moët Hennessy Louis Vuitton
SEA = "SE"
CPNG = "CPNG"
ORCL = "ORCL"           # Oracle
ADBE = "ADBE"
BA = "BA"
HPQ = "HPQ"             # HP Inc
DELL = "DELL"           # Dell Technologies
ERIC = "ERIC"

# FINANCIAL
JPM = "JPM"             # JPMorgan
BAC = "BAC"             # Bank of America
GS = "GS"               # Goldman Sachs
MS = "MS"               # Morgan Stanley

# PAYMENT
MA = "MA"               # Mastercard
VISA = "V"              # Visa Inc
PYPL = "PYPL"           # PayPal
EBAY = "EBAY"
NU = "NU"               # Nu Holdings
HOOD = "HOOD"           # Robinhood

# ENERGY
XOM = "XOM"             # Exxon Mobil
CVX = "CVX"             # Chevron

# CONSUMER GOODS
WMT = "WMT"             # Walmart
PG = "PG"               # Procter & Gamble
KO = "KO"               # Coca-Cola
MCD = "MCD"             # McDonald's
DIS = "DIS"             # Disney

# SEMI CONDUCTOR
TSM = "TSM"             # Taiwan Semiconductor Manufacturing Company
AVGO = "AVGO"           # Broadcom Inc
ASML = "ASML"
AMD = "AMD"
QCOM = "QCOM"           # Qualcomm
INTC = "INTC"

# MEDICAL
LLY = "LLY"             # Eli Lilly And Co
NVO = "NVO"             # Novo Nordisk
JNJ = "JNJ"             # Johnson & Johnson
MRK = "MRK"             # Merck & Co.
PFE = "PFE"             # Pfizer
GILD = "GILD"
MRNA = "MRNA"
BNTX = "BNTX"

# AUTOMOTIVE
RIVN = "RIVN"
NIO = "NIO"
LI = "LI"
XPEV = "XPEV"

# CHINESE COMPANIES
BABA = "BABA"
PDD = "PDD"
JD = "JD"
TCOM = "TCOM"           # Trip.com
BIDU = "BIDU"           # Baidu
BEKE = "BEKE"
MNSO = "MNSO"
BILI = "BILI"
EDU = "EDU"
FUTU = "FUTU"
YY = "YY"
TME = "TME"             # Tencent Music Entertainment Group
IQ = "IQ"

# HONG KONG COMPANIES
HK_0700 = "0700.HK"     # Tencent
HK_1211 = "1211.HK"     # BYD

V_INDEX = [
    QQQ,
    IXIC,
    KWEB,
    SS_000300,
    SS_000001,
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

V_500B = [
    NFLX,
    JPM,
    ASML,
    LLY,
    WMT,
    MA,
    VISA,
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
    LVMUY,
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

V_50B = [
    PYPL,
    COIN,
    SNOW,
    JD,
    NU,
]

V_30B = [
    EBAY,
    CPNG,
    TTD,
    TCOM,
    SEA,
    BLOCK,
    DELL,
    HPQ,
    HOOD,
]

V_10B = [
    RIVN,
    LI,
    XPEV,
    MRNA,
    BNTX,
    ZM,
    SNAP,
    BEKE,
    ERIC,
    OKTA,
    PINS,
    BIDU,
]

V_SMALL = [
    CFLT,
    ETSY,
    GTLB,
    NIO,
    MNSO,
    EDU,
    FUTU,
    BILI,
    TME,
    YY,
    IQ,
]

ALL = V_INDEX \
      + V_3000B + V_2000B + V_1000B \
      + V_500B + V_300B + V_200B + V_100B \
      + V_50B + V_30B + V_10B \
      + V_SMALL

BIG_BOY = V_3000B + V_2000B + V_1000B
MID_BOY = V_500B + V_300B + V_200B + V_100B
TINY_BOY = V_50B + V_30B
SMALL_BOY = V_10B + V_SMALL
