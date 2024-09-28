#
# keys for configuration
#
MODE = 'mode'                           # train/predict/dev
MASK = 'mask'                           # used in train, launch 2 ** mask process per stock

FROM_DATE = 'from_date'                 # start date for train/predict/dev
TO_DATE = 'to_date'                     # end date for train/predict/dev

TRAIN_FROM_DATE = 'train_from_date'     # used in predict, start date for train
TRAIN_TO_DATE = 'train_to_date'         # used in predict, end date for train

PREDICT_FROM_DATE = 'predict_from_date' # used in dev, start date for predict
PREDICT_TO_DATE = 'predict_to_date'     # used in dev, end date for predict

RECALL_STEP = 'recall_step'             # step for checking the past
FORECAST_STEP = 'forecast_step'         # step for checking the future
MARGIN = 'margin'                       # margin for checking the trade
HIT_THRESHOLD = 'hit_threshold'         # hit threshold for both long and short
SUCCESSFUL_RATE = 'successful_rate'     # successful rate for both long and short

evaluators = [
    {
        MARGIN: margin,
        HIT_THRESHOLD: hit_threshold,
        SUCCESSFUL_RATE: 90,
    }
    for (margin, hit_threshold) in [
        (0.02, 4),
        (0.04, 4),
        (0.06, 4),
        (0.08, 4),
        (0.10, 4),
        (0.12, 4),
        (0.14, 4),
        (0.16, 4),
        (0.18, 4),
        (0.20, 4),
        (0.22, 4),
        (0.24, 4),
    ]
]

# history 400, recall 4, forecast 10, expect margin 20, hit 4
# history 200, recall 4, forecast  5, expect margin 10, hit 4
# history 100, recall 4, forecast  3, expect margin  5, hit 4
train_confs = [
    {
        MODE: 'train',
        FROM_DATE: '',
        TO_DATE: '',

        RECALL_STEP: 4,
        FORECAST_STEP: forecast_step,

        MASK: 4,
        'evaluators': evaluators,
    }
    for forecast_step in [10, 5, 3]
]

predict_confs = [
    [
        {
            MODE: 'predict',
            FROM_DATE: '',
            TO_DATE: '',

            TRAIN_FROM_DATE: '',
            TRAIN_TO_DATE: '',

            RECALL_STEP: 4,
            FORECAST_STEP: forecast_step,

            **evaluator,
        } for evaluator in evaluators
    ]
    for forecast_step in [10, 5, 3]
]

dev_confs = [
    [
        {
            MODE: 'dev',
            FROM_DATE: '',
            TO_DATE: '',

            PREDICT_FROM_DATE: '',
            PREDICT_TO_DATE: '',

            RECALL_STEP: 4,
            FORECAST_STEP: forecast_step,

            **evaluator,
        } for evaluator in evaluators
    ]
    for forecast_step in [10, 5, 3]
]

if __name__ == '__main__':
    import json

    print(json.dumps(train_confs, indent=4))
    print(json.dumps(predict_confs, indent=4))
    print(json.dumps(dev_confs, indent=4))
