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

recall_3 = {RECALL_STEP: 3, MASK: 1}
recall_4 = {RECALL_STEP: 4, MASK: 2}
recall_5 = {RECALL_STEP: 5, MASK: 3}

stock_margin_3 = {MARGIN: 0.03, HIT_THRESHOLD: 8}
stock_margin_5 = {MARGIN: 0.05, HIT_THRESHOLD: 5}
stock_margin_9 = {MARGIN: 0.09, HIT_THRESHOLD: 2}

index_margin_1 = {MARGIN: 0.01, HIT_THRESHOLD: 8}
index_margin_3 = {MARGIN: 0.03, HIT_THRESHOLD: 5}
index_margin_5 = {MARGIN: 0.05, HIT_THRESHOLD: 2}

stock_confs = [
    {
        **base_conf,
        **recall_step,
        **margin,
    }
    for recall_step in (recall_3, recall_4, recall_5) for margin in (stock_margin_3, stock_margin_5, stock_margin_9)
]

index_confs = [
    {
        **base_conf,
        **recall_step,
        **margin,
    }
    for recall_step in (recall_3, recall_4, recall_5) for margin in (index_margin_1, index_margin_3, index_margin_5)
]


if __name__ == '__main__':
    for conf in stock_confs:
        print(conf)

    for conf in index_confs:
        print(conf)
