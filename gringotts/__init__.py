#
# for giant_model.py
#
MASK = 'mask'                           # will launch 2 ** mask process per stock

#
# for tiny_model.py
#
RECALL_STEP = 'recall_step'             # step for checking the past

FORECAST_STEP = 'forecast_step'         # step for checking the future
MARGIN = 'margin'                       # margin for checking the trade

SUCCESSFUL_RATE = 'successful_rate'     # successful rate for both long and short
HIT_THRESHOLD = 'hit_threshold'         # hit threshold for both long and short

base_conf = {
    MASK: 0,
    SUCCESSFUL_RATE: 80,
    FORECAST_STEP: 5,
}

conf_3 = {
    **base_conf,
    MARGIN: 0.03, HIT_THRESHOLD: 8,
}

conf_5 = {
    **base_conf,
    MARGIN: 0.05, HIT_THRESHOLD: 5,
}

conf_10 = {
    **base_conf,
    MARGIN: 0.10, HIT_THRESHOLD: 2,
}

confs = [
    # recall 3d
    {
        RECALL_STEP: 3, **conf_3,
    },
    {
        RECALL_STEP: 3, **conf_5,
    },
    {
        RECALL_STEP: 3, **conf_10,
    },

    # recall 4d
    {
        RECALL_STEP: 4, **conf_3,
    },
    {
        RECALL_STEP: 4, **conf_5,
    },
    {
        RECALL_STEP: 4, **conf_10,
    },

    # recall 5d
    {
        RECALL_STEP: 5, **conf_3,
    },
    {
        RECALL_STEP: 5, **conf_5,
    },
    {
        RECALL_STEP: 5, **conf_10,
    },
]
