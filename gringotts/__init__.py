from conf import *

#
# keys for configuration
#
MODE = 'mode'                           # train or predict
MASK = 'mask'                           # used in train, launch 2 ** mask process per stock
CROSS = 'cross'                         # used in predict, cross stock validation

RECALL_STEP = 'recall_step'             # step for checking the past

FORECAST_STEP = 'forecast_step'         # step for checking the future
MARGIN = 'margin'                       # margin for checking the trade
HIT_THRESHOLD = 'hit_threshold'         # hit threshold for both long and short
SUCCESSFUL_RATE = 'successful_rate'     # successful rate for both long and short

evaluators = [
    {
        FORECAST_STEP: 5,
        MARGIN: margin,
        HIT_THRESHOLD: hit_threshold,
        SUCCESSFUL_RATE: 90,
    }
    for (margin, hit_threshold) in [
        (0.05, 8),
        (0.10, 3),
    ]
]

train_confs = [
    {
        MODE: 'train',
        RECALL_STEP: 3,
        MASK: 1,
        'evaluators': evaluators,
    },
    {
        MODE: 'train',
        RECALL_STEP: 4,
        MASK: 2,
        'evaluators': evaluators,
    },
    {
        MODE: 'train',
        RECALL_STEP: 5,
        MASK: 3,
        'evaluators': evaluators,
    },
]

predict_confs = [
    [
        {
            MODE: 'predict',
            RECALL_STEP: 3,
            CROSS: '',
            # CROSS: TSLA,
            **evaluator,
        } for evaluator in evaluators
    ],
    [
        {
            MODE: 'predict',
            RECALL_STEP: 4,
            CROSS: '',
            # CROSS: TSLA,
            **evaluator,
        } for evaluator in evaluators
    ],
    [
        {
            MODE: 'predict',
            RECALL_STEP: 5,
            CROSS: '',
            # CROSS: TSLA,
            **evaluator,
        } for evaluator in evaluators
    ],
]


if __name__ == '__main__':
    print(train_confs)
    print(predict_confs)
