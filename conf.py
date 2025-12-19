# CN INDEX
CSI_300_ETF = "510300.SS"
Dividend_ETF = "510880.SS"
STAR_MARKET_50_ETF = "588000.SS"

# US INDEX
QQQ = "QQQ"
SPY = "SPY"
SCHD = "SCHD"
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
ETSY = "ETSY"
SHOP = "SHOP"           # Shopify
GTLB = "GTLB"
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
MNSO = "MNSO"
BILI = "BILI"
EDU = "EDU"
FUTU = "FUTU"
TME = "TME"             # Tencent Music Entertainment Group

# HONG KONG COMPANIES
TENCENT = "0700.HK"     # Tencent

V_INDEX = [
    CSI_300_ETF,
    Dividend_ETF,
    STAR_MARKET_50_ETF,

    SCHD,
    QQQ,
    SPY,
    KWEB,

    GOLD,
    BTC,
]

V_4000B = [
    NVDA,
    AAPL,
]

V_3000B = [
    MSFT,
    GOOG,
]

V_2000B = [
    AMZN,
]

V_1000B = [
    META,
    TSLA,
    TSM,
    AVGO,
]

V_500B = [
    LLY,
    WMT,
    JPM,
    VISA,
    MA,
    TENCENT,
    ORCL,
]

V_300B = [
    NFLX,
    ASML,
    XOM,
    CVX,
    JNJ,
    PG,
    KO,
    BAC,
    PLTR,
]

V_200B = [
    BABA,
    AMD,
    GS,
    MS,
    MCD,
    DIS,
    NVO,
    MRK,
]

V_100B = [
    ADBE,
    QCOM,
    PFE,
    GILD,
    BA,
    UBER,
    SHOP,
    PDD,
    SPOT,
]

V_50B = [
    INTC,
    HOOD,
    PYPL,
    COIN,
    SNOW,
    NU,
    SEA,
    CPNG,
    DELL,
]

V_30B = [
    EBAY,
    TTD,
    XYZ,
    TCOM,
    JD,
    TME,
    BIDU,
]

V_10B = [
    HPQ,
    BNTX,
    ZM,
    SNAP,
    BEKE,
    ERIC,
    OKTA,
    PINS,
    AFRM,
    FUTU,
    RIVN,
    LI,
    XPEV,
    NIO,
]

V_SMALL = [
    BILI,
    ETSY,
    GTLB,
    MNSO,
    EDU,
]

ALL = V_INDEX \
      + V_4000B + V_3000B + V_2000B + V_1000B \
      + V_500B + V_300B + V_200B + V_100B \
      + V_50B + V_30B + V_10B \
      + V_SMALL
