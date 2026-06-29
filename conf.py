# CN INDEX
ETF_CSI_300 = "510300.SS"
ETF_SSE_DIVIDEND = "510880.SS"
ETF_STAR_50 = "588000.SS"
ETF_CHI_NEXT = "159915.SZ"
ETF_GLD_SH = "518680.SS"

# US INDEX
QQQ = "QQQ"
VOO = "VOO"
SOX = "SOXX"
KWEB = "KWEB"
GLD = "GLD"
SLV = "SLV"
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
SEA = "SE"              # Shopee
CPNG = "CPNG"           # Coupang
ADBE = "ADBE"
BA = "BA"               # Boeing
HPQ = "HPQ"             # HP Inc
DELL = "DELL"           # Dell Technologies
ERIC = "ERIC"
SPOT = "SPOT"           # Spotify
CRM = "CRM"             # Salesforce

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
KLAR = "KLAR"           # Klarna

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
MU = "MU"               # Micron Technology
ORCL = "ORCL"           # Oracle

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
    ETF_GLD_SH,
]

US_INDEX = [
    GLD,
    SLV,
    BTC,
    QQQ,
    VOO,
    SOX,
    KWEB,
]

V_4000B = [
    NVDA,
    GOOG,
    AAPL,
]

V_3000B = [
]

V_2000B = [
    MSFT,
    AMZN,
    TSM,
]

V_1000B = [
    AVGO,
    META,
    TSLA,
    MU,
    LLY,
]

V_500B = [
    WMT,
    JPM,
    VISA,
    JNJ,
    ASML,
    XOM,
    AMD,
    INTC,
]

V_200B = [
    TENCENT,
    ORCL,
    MA,
    NFLX,
    CVX,
    PG,
    KO,
    BAC,
    PLTR,
    BABA,
    GS,
    MS,
    MRK,
    NVO,
    QCOM,
    DELL,
]

V_100B = [
    MCD,
    DIS,
    SHOP,
    PFE,
    GILD,
    BA,
    UBER,
    PDD,
    CRM,
    SPOT,
]

V_50B = [
    ADBE,
    HOOD,
    NU,
    SEA,
    SNOW,
]

V_20B = [
    COIN,
    PYPL,
    CPNG,
    EBAY,
    XYZ,
    TCOM,
    JD,
    BIDU,
    ERIC,
    BNTX,
    ZM,
    AFRM,
    HPQ,
    RIVN,
    OKTA,
]

V_10B = [
    BEKE,
    FUTU,
    TME,
    PINS,
    LI,
    XPEV,
    NIO,
]

V_SMALL = [
    TTD,
    SNAP,
    BILI,
    KLAR,
]

ALL = CN_INDEX + US_INDEX \
      + V_4000B + V_3000B + V_2000B + V_1000B \
      + V_500B + V_200B + V_100B \
      + V_50B + V_20B + V_10B \
      + V_SMALL
