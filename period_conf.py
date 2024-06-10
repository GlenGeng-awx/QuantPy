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

local_max_price_3rd_quasi = 'local_max_price_3rd_quasi'
local_min_price_3rd_quasi = 'local_min_price_3rd_quasi'

range_max_price_15 = 'range_max_price_15'
range_max_price_30 = 'range_max_price_30'

range_min_price_15 = 'range_min_price_15'
range_min_price_30 = 'range_min_price_30'

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

# period
PERIOD_CONF = {}

PERIOD_CONF[IXIC] = [
    # ('2017-01-01', datetime.now().strftime('%Y-%m-%d')),
    # ('2017-01-01', '2020-05-12'),
    # ('2020-01-01', '2023-01-01'),
    ('2022-01-01', datetime.now().strftime('%Y-%m-%d'))
]

PERIOD_CONF[SS_000001] = [
    ('2017-01-01', datetime.now().strftime('%Y-%m-%d'))
]

PERIOD_CONF[PDD] = [
    ('2019-01-01', datetime.now().strftime('%Y-%m-%d'))
]


def default_period():
    current_date = datetime.now()

    date_1y_ago = current_date - timedelta(days=365 * 1)
    date_2y_ago = current_date - timedelta(days=365 * 2)
    date_3y_ago = current_date - timedelta(days=365 * 3)

    return [
        # (date_1y_ago.strftime('%Y-%m-%d'), current_date.strftime('%Y-%m-%d')),
        # (date_2y_ago.strftime('%Y-%m-%d'), current_date.strftime('%Y-%m-%d')),
        (date_3y_ago.strftime('%Y-%m-%d'), current_date.strftime('%Y-%m-%d')),
    ]


def get_period(stock_name):
    if stock_name in PERIOD_CONF:
        return PERIOD_CONF[stock_name]
    else:
        return default_period()


# display option
DISPLAY_CONF_1 = {
    # candle stick
    'enable_up_box': True,
    'enable_down_box': True,
    'enable_sr_level': False,

    # volume
    'enable_peak_volume_up': True,
    'enable_peak_volume_down': True,
}

DISPLAY_CONF_2 = {
    # candle stick
    'enable_up_box': False,
    'enable_down_box': False,
    'enable_sr_level': False,

    # volume
    'enable_peak_volume_up': False,
    'enable_peak_volume_down': False,
}

DISPLAY_CONF = DISPLAY_CONF_1
