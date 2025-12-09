import re

VALID_DATES = [
    '2025-12-01', '2025-12-02', '2025-12-03', '2025-12-04', '2025-12-05',
    '2025-12-08',
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
