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

FORECAST_STEP = 'forecast_step'         # step for checking the future
MARGIN = 'margin'                       # margin for checking the trade
HIT_THRESHOLD = 'hit_threshold'         # hit threshold for both long and short
SUCCESSFUL_RATE = 'successful_rate'     # successful rate for both long and short
