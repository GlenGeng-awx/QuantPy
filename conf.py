from datetime import datetime, timedelta

# price
local_max_price_1st = 'local_max_price_1st'
local_max_price_2nd = 'local_max_price_2nd'
local_max_price_3rd = 'local_max_price_3rd'
local_max_price_4th = 'local_max_price_4th'

local_min_price_1st = 'local_min_price_1st'
local_min_price_2nd = 'local_min_price_2nd'
local_min_price_3rd = 'local_min_price_3rd'
local_min_price_4th = 'local_min_price_4th'

# volume
volume_reg = 'volume_reg'

local_max_volume_1st = 'local_max_volume_1st'
local_max_volume_2nd = 'local_max_volume_2nd'
local_max_volume_3rd = 'local_max_volume_3rd'
local_max_volume_4th = 'local_max_volume_4th'

local_min_volume_1st = 'local_min_volume_1st'
local_min_volume_2nd = 'local_min_volume_2nd'
local_min_volume_3rd = 'local_min_volume_3rd'
local_min_volume_4th = 'local_min_volume_4th'

volume_ma_5 = 'volume_ma_5'
volume_ma_15 = 'volume_ma_15'
volume_ma_30 = 'volume_ma_30'
volume_ma_60 = 'volume_ma_60'

# Stock Name
IXIC = "^IXIC"
SS_000300 = "000300.SS"
SS_000001 = "000001.SS"
GC_F = "GC=F"

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
TSM = "TSM"
BA = "BA"

ZM = "ZM"
SNAP = "SNAP"
EBAY = "EBAY"
IQ = "IQ"

HK_0700 = "0700.HK"
BABA = "BABA"
JD = "JD"
BEKE = "BEKE"
MNSO = "MNSO"
BILI = "BILI"
EDU = "EDU"
CPNG = "CPNG"


def default_period():
    current_date = datetime.now()

    date_0y_ago = datetime(current_date.year, 1, 1).strftime('%Y-%m-%d')
    date_1y_ago = datetime(current_date.year - 1, 1, 1).strftime('%Y-%m-%d')
    date_5y_ago = datetime(current_date.year - 5, 1, 1).strftime('%Y-%m-%d')

    current_date = current_date.strftime('%Y-%m-%d')

    return [
        (date_0y_ago, current_date, '1h'),
        (date_1y_ago, current_date, '1d'),
        (date_5y_ago, current_date, '1wk'),
    ]


def get_period(_stock_name):
    return default_period()

