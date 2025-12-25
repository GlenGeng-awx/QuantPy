# CN INDEX
ETF_CSI_300 = "510300.SS"
ETF_SSE_DIVIDEND = "510880.SS"
ETF_STAR_50 = "588000.SS"
ETF_CHI_NEXT = "159915.SZ"

# US INDEX
QQQ = "QQQ"
VOO = "VOO"
KWEB = "KWEB"
GOLD = "GLD"
BTC = "BTC-USD"

# SEVEN GIANTS
AAPL = "AAPL"
MSFT = "MSFT"
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
SHOP = "SHOP"           # Shopify
PINS = "PINS"           # Pinterest
XYZ = "XYZ"             # Block
COIN = "COIN"           # Coinbase
LVMUY = "LVMUY"         # LVMH Moët Hennessy Louis Vuitton
SEA = "SE"              # Shopee
CPNG = "CPNG"           # Coupang
ORCL = "ORCL"           # Oracle
ADBE = "ADBE"
BA = "BA"               # Boeing
HPQ = "HPQ"             # HP Inc
DELL = "DELL"           # Dell Technologies
ERIC = "ERIC"
SPOT = "SPOT"           # Spotify

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
AFRM = "AFRM"           # Affirm Holdings

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
TSM = "TSM"             # TSMC
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
GILD = "GILD"           # Gilead Sciences
BNTX = "BNTX"           # BioNTech SE

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
BILI = "BILI"
FUTU = "FUTU"
TME = "TME"             # Tencent Music Entertainment Group

# HONG KONG COMPANIES
TENCENT = "0700.HK"     # Tencent

CN_INDEX = [
    ETF_CSI_300,
    ETF_SSE_DIVIDEND,
    ETF_STAR_50,
    ETF_CHI_NEXT,
]

US_INDEX = [
    QQQ,
    VOO,
    KWEB,
    GOLD,
    BTC,
]

V_4000B = [
    NVDA,
    AAPL,
]

V_3000B = [
    GOOG,
    MSFT,
]

V_2000B = [
    AMZN,
]

V_1000B = [
    META,
    TSLA,
    AVGO,
    TSM,
    LLY,
]

V_500B = [
    WMT,
    JPM,
    VISA,
    MA,
    TENCENT,
    ORCL,
    JNJ,
]

V_300B = [
    NFLX,
    ASML,
    XOM,
    CVX,
    PG,
    KO,
    BAC,
    PLTR,
    AMD,
    BABA,
]

V_200B = [
    GS,
    MS,
    MCD,
    DIS,
    NVO,
    MRK,
    SHOP,
]

V_100B = [
    ADBE,
    QCOM,
    PFE,
    GILD,
    BA,
    UBER,
    PDD,
    SPOT,
    HOOD,
    INTC,
]

V_50B = [
    PYPL,
    COIN,
    SNOW,
    NU,
    SEA,
    DELL,
]

V_30B = [
    CPNG,
    EBAY,
    XYZ,
    TCOM,
    JD,
    BIDU,
    ERIC,
]

V_10B = [
    TTD,
    TME,
    HPQ,
    BNTX,
    ZM,
    SNAP,
    BEKE,
    OKTA,
    PINS,
    AFRM,
    FUTU,
    RIVN,
    LI,
    XPEV,
    NIO,
    BILI,
]

ALL = CN_INDEX + US_INDEX \
      + V_4000B + V_3000B + V_2000B + V_1000B \
      + V_500B + V_300B + V_200B + V_100B \
      + V_50B + V_30B + V_10B
