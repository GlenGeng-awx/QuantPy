#
# for giant_model.py
#

MASK = 0                    # will launch 2 ** mask process per stock
SUCCESSFUL_RATE = 80        # successful full for both long and short
HIT_THRESHOLD = 5           # hit threshold  for both long and short

#
# for tiny_model.py
#
RECALL_STEP = 3             # step for checking the past
FORECAST_STEP = 5           # step for checking the future
MARGIN = 0.03               # margin for checking the trade
