import re

VALID_DATES = [
    '2025-06-02', '2025-06-03', '2025-06-04', '2025-06-05', '2025-06-06',
    '2025-06-09', '2025-06-10', '2025-06-11', '2025-06-12', '2025-06-13',
    '2025-06-16', '2025-06-17', '2025-06-18',               '2025-06-20',
    '2025-06-23', '2025-06-24', '2025-06-25', '2025-06-26', '2025-06-27',

    '2025-06-30', '2025-07-01', '2025-07-02', '2025-07-03',
    '2025-07-07', '2025-07-08', '2025-07-09', '2025-07-10', '2025-07-11',
    '2025-07-14', '2025-07-15', '2025-07-16', '2025-07-17', '2025-07-18',
    '2025-07-21', '2025-07-22', '2025-07-23', '2025-07-24', '2025-07-25',
    '2025-07-28', '2025-07-29', '2025-07-30', '2025-07-31', '2025-08-01',

    '2025-08-04', '2025-08-05', '2025-08-06', '2025-08-07', '2025-08-08',
    '2025-08-11', '2025-08-12', '2025-08-13', '2025-08-14', '2025-08-15',
    '2025-08-18', '2025-08-19', '2025-08-20', '2025-08-21', '2025-08-22',
    '2025-08-25', '2025-08-26', '2025-08-27', '2025-08-28', '2025-08-29',

    '2025-09-02', '2025-09-03', '2025-09-04', '2025-09-05',
    '2025-09-08', '2025-09-09', '2025-09-10', '2025-09-11', '2025-09-12',
    '2025-09-15', '2025-09-16', '2025-09-17', '2025-09-18', '2025-09-19',
    '2025-09-22', '2025-09-23', '2025-09-24', '2025-09-25', '2025-09-26',
    '2025-09-29', '2025-09-30', '2025-10-01', '2025-10-02', '2025-10-03',

    '2025-10-06', '2025-10-07', '2025-10-08', '2025-10-09', '2025-10-10',
    '2025-10-13', '2025-10-14', '2025-10-15', '2025-10-16', '2025-10-17',
    '2025-10-20', '2025-10-21', '2025-10-22', '2025-10-23', '2025-10-24',
    '2025-10-27', '2025-10-28', '2025-10-29', '2025-10-30', '2025-10-31',

    '2025-11-03', '2025-11-04', '2025-11-05', '2025-11-06', '2025-11-07',
    '2025-11-10', '2025-11-11', '2025-11-12',
]

train_48m = '_train_48m'
train_42m = '_train_42m'
train_36m = '_train_36m'

# 48m/42m/36m
TRAIN_MODE = [
    train_48m,
    train_42m,
    train_36m,
]

#
# 48m/42m/36m
#
# 4: 4
# 5: 5, 4
# 6: 6, 5
# 7: 7, 6, 5
# 8: 8, 7, 6
# 9: 9, 8, 7
# 10: 90%, 80%, 70%
#
predict_48m_t4_h4 = '_predict_48m_t4_h4'
predict_48m_t5_h5 = '_predict_48m_t5_h5'
predict_48m_t5_h4 = '_predict_48m_t5_h4'
predict_48m_t6_h6 = '_predict_48m_t6_h6'
predict_48m_t6_h5 = '_predict_48m_t6_h5'
predict_48m_t7_h7 = '_predict_48m_t7_h7'
predict_48m_t7_h6 = '_predict_48m_t7_h6'
predict_48m_t7_h5 = '_predict_48m_t7_h5'
predict_48m_t8_h8 = '_predict_48m_t8_h8'
predict_48m_t8_h7 = '_predict_48m_t8_h7'
predict_48m_t8_h6 = '_predict_48m_t8_h6'
predict_48m_t9_h9 = '_predict_48m_t9_h9'
predict_48m_t9_h8 = '_predict_48m_t9_h8'
predict_48m_t9_h7 = '_predict_48m_t9_h7'
predict_48m_t10_h9 = '_predict_48m_t10_h9'
predict_48m_t10_h8 = '_predict_48m_t10_h8'
predict_48m_t10_h7 = '_predict_48m_t10_h7'

predict_42m_t4_h4 = '_predict_42m_t4_h4'
predict_42m_t5_h5 = '_predict_42m_t5_h5'
predict_42m_t5_h4 = '_predict_42m_t5_h4'
predict_42m_t6_h6 = '_predict_42m_t6_h6'
predict_42m_t6_h5 = '_predict_42m_t6_h5'
predict_42m_t7_h7 = '_predict_42m_t7_h7'
predict_42m_t7_h6 = '_predict_42m_t7_h6'
predict_42m_t7_h5 = '_predict_42m_t7_h5'
predict_42m_t8_h8 = '_predict_42m_t8_h8'
predict_42m_t8_h7 = '_predict_42m_t8_h7'
predict_42m_t8_h6 = '_predict_42m_t8_h6'
predict_42m_t9_h9 = '_predict_42m_t9_h9'
predict_42m_t9_h8 = '_predict_42m_t9_h8'
predict_42m_t9_h7 = '_predict_42m_t9_h7'
predict_42m_t10_h9 = '_predict_42m_t10_h9'
predict_42m_t10_h8 = '_predict_42m_t10_h8'
predict_42m_t10_h7 = '_predict_42m_t10_h7'

predict_36m_t4_h4 = '_predict_36m_t4_h4'
predict_36m_t5_h5 = '_predict_36m_t5_h5'
predict_36m_t5_h4 = '_predict_36m_t5_h4'
predict_36m_t6_h6 = '_predict_36m_t6_h6'
predict_36m_t6_h5 = '_predict_36m_t6_h5'
predict_36m_t7_h7 = '_predict_36m_t7_h7'
predict_36m_t7_h6 = '_predict_36m_t7_h6'
predict_36m_t7_h5 = '_predict_36m_t7_h5'
predict_36m_t8_h8 = '_predict_36m_t8_h8'
predict_36m_t8_h7 = '_predict_36m_t8_h7'
predict_36m_t8_h6 = '_predict_36m_t8_h6'
predict_36m_t9_h9 = '_predict_36m_t9_h9'
predict_36m_t9_h8 = '_predict_36m_t9_h8'
predict_36m_t9_h7 = '_predict_36m_t9_h7'
predict_36m_t10_h9 = '_predict_36m_t10_h9'
predict_36m_t10_h8 = '_predict_36m_t10_h8'
predict_36m_t10_h7 = '_predict_36m_t10_h7'

PREDICT_MODE = [
    # 48m
    predict_48m_t4_h4,

    predict_48m_t5_h5,
    predict_48m_t5_h4,

    predict_48m_t6_h6,
    predict_48m_t6_h5,

    predict_48m_t7_h7,
    predict_48m_t7_h6,
    predict_48m_t7_h5,

    predict_48m_t8_h8,
    predict_48m_t8_h7,
    predict_48m_t8_h6,

    predict_48m_t9_h9,
    predict_48m_t9_h8,
    predict_48m_t9_h7,

    predict_48m_t10_h9,
    predict_48m_t10_h8,
    predict_48m_t10_h7,

    # 42m
    predict_42m_t4_h4,

    predict_42m_t5_h5,
    predict_42m_t5_h4,

    predict_42m_t6_h6,
    predict_42m_t6_h5,

    predict_42m_t7_h7,
    predict_42m_t7_h6,
    predict_42m_t7_h5,

    predict_42m_t8_h8,
    predict_42m_t8_h7,
    predict_42m_t8_h6,

    predict_42m_t9_h9,
    predict_42m_t9_h8,
    predict_42m_t9_h7,

    predict_42m_t10_h9,
    predict_42m_t10_h8,
    predict_42m_t10_h7,

    # 36m
    predict_36m_t4_h4,

    predict_36m_t5_h5,
    predict_36m_t5_h4,

    predict_36m_t6_h6,
    predict_36m_t6_h5,

    predict_36m_t7_h7,
    predict_36m_t7_h6,
    predict_36m_t7_h5,

    predict_36m_t8_h8,
    predict_36m_t8_h7,
    predict_36m_t8_h6,

    predict_36m_t9_h9,
    predict_36m_t9_h8,
    predict_36m_t9_h7,

    predict_36m_t10_h9,
    predict_36m_t10_h8,
    predict_36m_t10_h7,
]


# _predict_36m_t10_h9 -> train_36m
def get_train_mode(predict_mode: str):
    months, _total, _hit = re.findall(r'\d+', predict_mode)
    return f'_train_{months}m'


if __name__ == '__main__':
    print(get_train_mode(predict_42m_t8_h6))
