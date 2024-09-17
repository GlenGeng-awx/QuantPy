#
# keys for configuration
#
MODE = 'mode'                           # train or predict
MASK = 'mask'                           # used in train, launch 2 ** mask process per stock

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
        SUCCESSFUL_RATE: 80,
    }
    for (margin, hit_threshold) in [
        (0.01, 8),
        (0.03, 8),
        (0.05, 5),
        (0.07, 5),
        (0.09, 3),
        (0.12, 3),
        (0.15, 2),
        (0.18, 2),
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
            **evaluator,
        } for evaluator in evaluators
    ],
    [
        {
            MODE: 'predict',
            RECALL_STEP: 4,
            **evaluator,
        } for evaluator in evaluators
    ],
    [
        {
            MODE: 'predict',
            RECALL_STEP: 5,
            **evaluator,
        } for evaluator in evaluators
    ],
]


if __name__ == '__main__':
    print(train_confs)
    print(predict_confs)
