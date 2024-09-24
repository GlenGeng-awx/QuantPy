#
# keys for configuration
#
MODE = 'mode'                           # train or predict
MASK = 'mask'                           # used in train, launch 2 ** mask process per stock

FROM_DATE = 'from_date'                 # start date for training or predicting
TO_DATE = 'to_date'                     # end date for training or predicting

TRAIN_FROM_DATE = 'train_from_date'     # used in predict, start date for training
TRAIN_TO_DATE = 'train_to_date'         # used in predict, end date for training

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
        # (0.02, 3),     # for index
        (0.04, 3),       # for stock
        # (0.10, 4),
        # (0.20, 3),
    ]
]

train_confs = [
    # {
    #     MODE: 'train',
    #     RECALL_STEP: 3,
    #     MASK: 4,
    #     'evaluators': evaluators,
    # },
    {
        MODE: 'train',
        FROM_DATE: '',
        TO_DATE: '',

        RECALL_STEP: 4,
        MASK: 4,
        'evaluators': evaluators,
    },
    # {
    #     MODE: 'train',
    #     RECALL_STEP: 5,
    #     MASK: 4,
    #     'evaluators': evaluators,
    # },
]

predict_confs = [
    # [
    #     {
    #         MODE: 'predict',
    #         RECALL_STEP: 3,
    #         **evaluator,
    #     } for evaluator in evaluators
    # ],
    [
        {
            MODE: 'predict',
            FROM_DATE: '',
            TO_DATE: '',

            TRAIN_FROM_DATE: '',
            TRAIN_TO_DATE: '',

            RECALL_STEP: 4,
            **evaluator,
        } for evaluator in evaluators
    ],
    # [
    #     {
    #         MODE: 'predict',
    #         RECALL_STEP: 5,
    #         **evaluator,
    #     } for evaluator in evaluators
    # ],
]


if __name__ == '__main__':
    print(train_confs)
    print(predict_confs)
