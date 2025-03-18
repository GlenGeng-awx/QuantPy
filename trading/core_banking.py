from conf import *

#
# lines
# -----
#   date1, date2, prev_len, post_len
#       or
#   date, prev_len, post_len, date1, date2
#
# elliott
# -------
#   (1), 1, i
#   (A), A, a
#
CORE_BANKING = {
    IXIC: {
        'lines': [
            ('2023-07-19', '2024-07-10', 10, 200),
            ('2023-10-26', 10, 400, '2023-07-18', '2024-07-10'),

            ('2024-08-21', '2024-12-16', 10, 10),
            ('2024-09-06', 10, 100, '2024-08-21', '2024-12-16'),
        ],
        'elliott': {
            '2023-07-19': ['(1)'],
            '2023-10-26': ['(2)'],
            '2024-03-22': ['3'],
            '2024-04-19': ['4'],
            '2024-07-10': ['(3)'],
            '2024-08-07': ['(4)'],
            '2024-08-21': ['1'],
            '2024-09-06': ['2'],
            '2024-11-11': ['iii'],
            '2024-11-15': ['iv'],
            '2024-12-16': ['3'],
            '2025-01-14': ['4'],
        },
    },
    QQQ: {
        'lines': [
            ('2023-07-18', '2024-07-10', 10, 10),
            ('2023-10-26', 10, 350, '2023-07-18', '2024-07-10'),

            ('2024-08-21', '2024-12-16', 10, 10),
            ('2024-09-06', 10, 120, '2024-08-21', '2024-12-16'),

            ('2024-07-10', '2025-02-19', 10, 10),
            ('2024-08-07', 100, 200, '2024-07-10', '2025-02-19'),
        ],
        'elliott': {
            '2023-07-18': ['(1)'],
            '2023-08-18': ['W'],
            '2023-09-05': ['X'],
            '2023-10-26': ['Y', '(2)'],
            '2024-03-22': ['3'],
            '2024-04-19': ['4'],
            '2024-07-10': ['(3)'],
            '2024-08-07': ['(4)'],
            '2024-08-21': ['i'],
            '2024-09-06': ['ii'],
            '2024-11-08': ['iii'],
            '2024-11-15': ['iv'],
            '2024-12-16': ['v', '1'],
        },
    },
    SS_000300: {
        'lines': [
        ],
        'elliott': {
            '2023-08-23': ['1'],
            '2023-09-04': ['2'],
            '2023-10-23': ['3'],
            '2023-11-06': ['4'],
            '2024-02-02': ['5'],
            '2024-03-18': ['A'],
            '2024-04-12': ['B'],
            '2024-05-20': ['C'],
            '2024-07-08': ['1'],
            '2024-07-19': ['2'],
            '2024-08-29': ['3'],
            '2024-08-30': ['4'],
            '2024-09-13': ['5'],
            '2024-10-08': ['(1)'],
            '2024-11-26': ['A'],
            '2024-12-12': ['B'],
            '2025-01-13': ['C', '(2)'],
        },
    },
    SS_000001: {
        'lines': [
            # ('2023-06-26', '2023-10-23', 50, 80),
            # ('2024-02-28', '2024-03-27', 5, 50),
            # ('2024-05-20', '2024-07-19', 10, 50),
        ],
        'elliott': {
            '2024-10-08': ['(1)'],
            '2024-10-17': ['A'],
            '2024-11-07': ['B'],
            '2024-11-26': ['i'],
            '2024-12-12': ['ii'],
            '2025-01-13': ['iii'],
            '2025-01-24': ['iv'],
        },
    },
    KWEB: {
        'lines': [
        ],
        'elliott': {
            '2023-01-26': ['(1)'],
            '2023-03-09': ['a'],
            '2023-03-30': ['b'],
            '2023-05-31': ['c', 'W'],
            '2023-07-31': ['X'],
            '2023-10-20': ['a'],
            '2023-11-15': ['b'],
            '2024-01-22': ['c', 'Y', '(2)'],
            '2024-05-17': ['1'],
            '2024-06-28': ['a'],
            '2024-07-12': ['b'],
            '2024-08-28': ['c', '2'],
            '2024-10-07': ['3'],
            '2024-11-22': ['a'],
            '2024-12-09': ['b'],
            '2025-01-10': ['c', '4'],
            '2025-02-21': ['i'],
            '2025-03-03': ['ii'],
        },
    },
    TSLA: {
        'lines': [
            ('2023-07-18', '2024-12-17', 10, 10),
            ('2024-04-22', 10, 300, '2023-07-18', '2024-12-17'),

            ('2023-07-18', '2023-12-27', 10, 10),
            ('2023-10-30', 10, 140, '2023-07-18', '2023-12-27'),
        ],
        'elliott': {
            '2023-07-18': ['(1)'],
            '2023-10-30': ['W'],
            '2023-12-27': ['X'],
            '2024-04-22': ['Y', '(2)'],
            '2024-04-29': ['1'],
            '2024-06-11': ['2'],
            '2024-07-10': ['3'],
            '2024-08-07': ['4'],
            '2024-09-30': ['i'],
            '2024-10-23': ['ii'],
            '2024-11-11': ['iii'],
            '2024-11-27': ['iv'],
            '2024-12-17': ['v', '5', '(3)'],
        },
    },
    HK_0700: {
        'lines': [
            ('2024-03-05', '2024-07-25', 10, 50),
            ('2024-05-17', 10, 100, '2024-03-05', '2024-07-25'),

            ('2024-10-07', '2024-12-20', 10, 20),
            ('2024-11-26', 10, 40, '2024-10-07', '2024-12-20'),
        ],
        'elliott': {
            '2024-01-25': ['1'],
            '2024-03-05': ['2'],
            '2024-05-17': ['3'],
            '2024-07-25': ['4'],
            '2024-10-07': ['5'],
            '2024-11-26': ['A'],
            '2024-12-20': ['B'],
            '2025-01-13': ['C'],
        },
    },
    BILI: {
        'lines': [
            # ('2023-06-05', '2023-09-21', 10, 120),
            # ('2023-06-15', 5, 150, '2023-06-05', '2023-09-21'),
            #
            # ('2024-03-12', '2024-05-17', 10, 50),
            # ('2024-04-19', 10, 80, '2024-03-12', '2024-05-17'),
            # ('2024-08-22', 10, 80, '2024-03-12', '2024-05-17'),
        ],
        'elliott': {
            '2024-03-12': ['1'],
            '2024-03-26': ['2'],
            '2024-05-17': ['3'],
            '2024-05-29': ['4'],
            '2024-06-21': ['5', '(1)'],
            '2024-07-24': ['A'],
            '2024-08-05': ['B'],
            '2024-08-22': ['C', '(2)'],
            '2024-10-02': ['(3)'],
            '2024-11-26': ['A'],
            '2024-12-09': ['B'],
        },
    },
    UBER: {
       'elliott': {
           '2023-02-08': ['1'],
           '2023-04-25': ['2'],
           '2023-07-31': ['3'],
           '2023-10-26': ['4'],
           '2023-12-27': ['i'],
           '2024-01-05': ['ii'],
           '2024-02-08': ['iii'],
           '2024-02-13': ['iv'],
           '2024-02-15': ['v', '5'],
           '2024-08-05': ['A'],
           '2024-10-11': ['B'],
           '2024-12-13': ['C'],
        },
    },
    PDD: {
        'lines': [
        ],
        'elliott': {
            '2023-01-27': ['(1)'],
            '2023-05-25': ['(2)'],
            '2024-01-11': ['(3)'],
            '2024-03-08': ['(4)'],
            '2024-05-24': ['(5)'],
            '2024-08-28': ['(A)'],
            '2024-10-04': ['(B)'],
        }
    },
    IQ: {
        'lines': [
            ('2023-02-28', '2023-07-31', 10, 345),
            ('2023-05-10', 10, 200, '2023-02-28', '2023-07-31'),
            ('2024-07-11', 10, 200, '2023-02-28', '2023-07-31'),
        ],
    },
    BABA: {
        'lines': [
            ('2024-05-17', '2024-10-07', 10, 100),
        ],
    },
    BA: {
        'lines': [
            ('2024-08-07', '2024-10-10', 10, 35),
        ],
        'elliott': {
            '2024-04-24': ['A'],
            '2024-07-31': ['B'],
            '2024-11-14': ['C'],
            '2024-12-27': ['1'],
            '2025-01-15': ['2'],
        },
    },
    COIN: {
        'lines': [
            ('2024-03-25', '2024-12-06', 10, 10),
            ('2024-09-06', 240, 200, '2024-03-25', '2024-12-06'),
        ],
        'elliott': {
            '2023-07-19': ['1'],
            '2023-10-27': ['2'],
            '2023-12-28': ['3'],
            '2024-02-05': ['4'],
            '2024-03-25': ['5', '(1)'],
            '2024-05-16': ['W'],
            '2024-07-22': ['X'],
            '2024-09-06': ['Y', '(2)'],
            '2024-12-06': ['1'],
            '2024-12-31': ['a'],
            '2025-01-30': ['b'],
            '2025-03-10': ['c'],
        },
    },
    PLTR: {
        'lines': [
        ],
        'elliott': {
            '2024-07-23': ['1'],
            '2024-08-05': ['2'],
            '2024-10-10': ['3'],
            '2024-11-04': ['4'],
            '2024-12-24': ['5', '(3)'],
            '2025-01-13': ['(4)'],
        },
    },
    NVDA: {
        'lines': [
            ('2023-10-26', '2024-08-07', 10, 10),
            ('2024-11-07', 400, 10, '2023-10-26', '2024-08-07'),
        ],
        'elliott': {
            '2023-10-26': ['(2)'],
            '2024-06-18': ['(3)'],
            '2024-08-07': ['(4)'],
            '2024-11-07': ['(5)'],
        },
    },
    BEKE: {
        'lines': [
            ('2023-02-13', '2023-03-03', 5, 100),
            ('2023-03-09', 5, 80, '2023-02-13', '2023-03-03'),

            ('2023-09-01', '2023-12-28', 10, 100),
            ('2023-10-19', 5, 100, '2023-09-01', '2023-12-28'),

            ('2024-10-04', '2024-11-07', 5, 60),
        ],
    },
    RIVN: {
        'lines': [
        ],
        'elliott': {
            '2023-04-25': ['(3)'],
            '2023-12-19': ['(4)'],
            '2024-04-15': ['(5)'],
            '2024-07-12': ['(1)'],
            '2024-11-06': ['(2)'],
        },
    },
    MRNA: {
        'lines': [
        ],
        'elliott': {
            '2023-11-09': ['(3)'],
            '2024-01-08': ['A'],
            '2024-02-13': ['B'],
            '2024-05-24': ['C', '(4)'],
            '2024-07-01': ['1'],
            '2024-07-16': ['2'],
            '2024-08-12': ['i'],
            '2024-10-24': ['iii'],
            '2024-11-15': ['3'],
            '2025-01-07': ['4'],
            '2025-01-16': ['i'],
            '2025-01-28': ['ii'],
            '2025-02-12': ['iii'],
        },
    },
    MNSO: {
        'lines': [
            # ('2023-09-14', '2024-05-13', 10, 160),
            # ('2023-08-11', 10, 140, '2023-09-14', '2024-05-13'),
            # ('2023-10-05', 10, 300, '2023-09-14', '2024-05-13'),
            # ('2023-12-14', 10, 220, '2023-09-14', '2024-05-13'),
            #
            # ('2023-11-20', '2024-01-16', 10, 50),
            # ('2024-05-30', 10, 70, '2023-11-20', '2024-01-16'),
            # ('2024-05-22', 5, 60, '2023-11-20', '2024-01-16'),
            #
            # ('2024-02-22', '2024-03-21', 10, 45),
            # ('2024-03-07', 5, 70, '2024-02-22', '2024-03-21'),
            # ('2024-09-24', 5, 70, '2024-02-22', '2024-03-21'),
            # ('2024-09-03', 5, 90, '2024-02-22', '2024-03-21'),
        ],
        'elliott': {
            '2024-10-04': ['1'],
            '2024-10-17': ['2'],
            '2024-10-30': ['i'],
            '2024-11-22': ['ii'],
            '2024-12-03': ['iii'],
            '2024-12-19': ['iv'],
            '2025-01-03': ['v', '3'],
        },
    },
    EDU: {
        'lines': [
            ('2024-05-14', '2024-07-03', 10, 160),
        ],
    },
    BNTX: {
        'lines': [
            # ('2023-08-30', '2024-01-02', 200, 200),
            # ('2023-03-01', 10, 350, '2023-08-30', '2024-01-02'),
            # ('2023-04-14', 10, 350, '2023-08-30', '2024-01-02'),
        ],
    },
    XPEV: {
        'lines': [
            ('2023-08-29', '2023-09-29', 10, 60),
            ('2023-08-18', 10, 100, '2023-08-29', '2023-09-29'),
            ('2023-11-24', 10, 300, '2023-08-29', '2023-09-29'),

            ('2024-10-02', '2024-11-11', 10, 60),
            ('2024-08-20', 5, 100, '2024-10-02', '2024-11-11'),
        ],
    },
    EBAY: {
        'lines': [
            ('2024-05-06', '2024-10-31', 10, 100),
            ('2024-10-08', 10, 100, '2024-05-06', '2024-10-31'),
        ],
    },
    META: {
        'lines': [
            ('2023-02-07', '2023-07-28', 10, 200),
            ('2023-10-26', 10, 160, '2023-02-07', '2023-07-28'),
            ('2024-07-25', 10, 200, '2023-02-07', '2023-07-28'),
        ],
        'elliott': {
            '2023-02-07': ['1'],
            '2023-07-28': ['3'],
            '2023-10-26': ['4'],
            '2024-04-05': ['5', '(1)'],
            '2024-04-30': ['(2)'],
            '2024-07-05': ['1'],
            '2024-07-25': ['2'],
            '2024-12-11': ['3'],
            '2024-12-31': ['4'],
            '2025-02-14': ['5', '(3)'],
        },
    },
    LI: {
        'lines': [
            ('2023-08-07', '2023-11-20', 10, 10),
            ('2023-10-20', 10, 100, '2023-08-07', '2023-11-20'),

            ('2024-08-28', '2025-01-13', 10, 10),
            ('2024-10-07', 10, 160, '2024-08-28', '2025-01-13'),
        ],
        'elliott': {
        },
    },
    ZM: {
        'lines': [
        ],
        'elliott': {
            '2024-08-27': ['1'],
            '2024-09-18': ['2'],
            '2024-11-12': ['iii'],
            '2024-11-19': ['iv'],
            '2024-11-25': ['3'],
            '2025-01-17': ['4'],
        },
    },
    TSM: {
        'lines': [
            ('2023-06-14', '2024-07-10', 10, 10),
            ('2024-08-05', 200, 200, '2023-06-14', '2024-07-10'),
        ],
        'elliott': {
            '2023-06-14': ['(1)'],
            '2023-09-26': ['(2)'],
            '2024-07-10': ['(3)'],
            '2024-08-05': ['(4)'],
            '2025-01-23': ['(5)'],
        },
    },
    AMD: {
        'lines': [
            ('2024-03-07', '2024-10-08', 10, 10),
            ('2024-08-07', 100, 200, '2024-03-07', '2024-10-08'),
        ],
        'elliott': {
            '2023-06-12': ['(1)'],
            '2023-10-26': ['(2)'],
            '2024-03-07': ['(3)'],
            '2024-05-01': ['a'],
            '2024-07-10': ['b'],
            '2024-08-07': ['c', 'W'],
            '2024-10-08': ['X'],
        },
    },
    PFE: {
        'lines': [
            ('2024-10-09', '2025-01-30', 10, 20),
        ],
        'elliott': {
            '2024-08-16': ['1'],
            '2024-10-09': ['2'],
            '2024-11-15': ['3'],
            '2025-01-30': ['4'],
        },
    },
    NIO: {
        'lines': [
            ('2023-01-27', '2023-07-12', 10, 400),
            ('2023-03-31', 10, 500, '2023-01-27', '2023-07-12'),
        ],
    },
    SQ: {
        'lines': [
            ('2024-07-16', '2024-09-19', 5, 40),
            ('2024-08-05', 5, 60, '2024-07-16', '2024-09-19'),

            ('2024-08-05', '2024-09-06', 5, 40),
            ('2024-07-16', 5, 60, '2024-08-05', '2024-09-06'),
            ('2024-08-19', 5, 60, '2024-08-05', '2024-09-06'),
        ],
    },
    SHOP: {
        'lines': [
            ('2024-09-06', '2025-01-14', 10, 40),
            ('2024-12-17', 10, 100, '2024-09-06', '2025-01-14'),
        ],
        'elliott': {
            '2022-12-01': ['1'],
            '2022-12-28': ['2'],
            '2023-07-13': ['3'],
            '2023-10-27': ['4'],
            '2024-02-09': ['5'],
            '2024-04-15': ['W'],
            '2024-05-06': ['X'],
            '2024-08-05': ['Y'],
            '2024-08-21': ['1'],
            '2024-09-06': ['2'],
            '2024-12-17': ['3'],
            '2025-01-14': ['4'],
        },
    },
    ETSY: {
        'lines': [
            ('2024-01-31', '2024-05-02', 5, 200),
            ('2024-02-02', 5, 200, '2024-01-31', '2024-05-02'),
            ('2024-02-12', 5, 200, '2024-01-31', '2024-05-02'),
        ],
    },
    MS: {
        'lines': [
        ],
        'elliott': {
            '2024-01-02': ['1'],
            '2024-01-18': ['2'],
            '2024-07-17': ['3'],
            '2024-08-05': ['4'],
            '2024-11-21': ['5'],
            '2024-12-19': ['A'],
            '2025-02-06': ['B'],
        },
    },
    CPNG: {
        'lines': [
            # ('2023-09-01', '2023-10-24', 10, 90),
            # ('2023-11-01', 10, 70, '2023-09-01', '2023-10-24'),
            #
            # ('2024-02-05', '2024-07-25', 5, 60),
            # ('2024-08-19', 120, 60, '2024-02-05', '2024-07-25'),
            # ('2024-03-22', 10, 200, '2024-02-05', '2024-07-25'),
            # ('2024-03-13', 10, 200, '2024-02-05', '2024-07-25'),
        ],
        'elliott': {
            '2023-08-10': ['(1)'],
            '2024-02-05': ['(2)'],
            '2024-05-30': ['(3)'],
            '2024-07-25': ['(4)'],
            '2024-11-05': ['(5)'],
        },
    },
    GTLB: {
        'lines': [
            ('2023-02-02', '2023-07-13', 10, 400),
            ('2023-12-28', 10, 240, '2023-02-02', '2023-07-13'),
            ('2023-12-20', 10, 240, '2023-02-02', '2023-07-13'),
        ],
    },
    SNAP: {
        'lines': [
            ('2024-09-09', '2024-10-22', 5, 60),
            ('2024-08-07', 5, 100, '2024-09-09', '2024-10-22'),
            ('2024-08-19', 5, 100, '2024-09-09', '2024-10-22'),
            ('2024-11-19', 5, 100, '2024-09-09', '2024-10-22'),
        ],
    },
    ERIC: {
        'lines': [
            ('2024-04-15', '2024-08-06', 10, 200),
            ('2024-06-05', 10, 200, '2024-04-15', '2024-08-06'),
        ],
    },
    LVMUY: {
        'lines': [
            ('2024-03-14', '2024-08-23', 10, 100),
            ('2024-09-27', 10, 100, '2024-03-14', '2024-08-23'),
        ],
    },
    OKTA: {
        'lines': [
            ('2024-03-07', '2024-08-23', 5, 100),
        ],
    },
    NFLX: {
        'lines': [
            ('2023-10-18', '2024-08-05', 10, 200),
            ('2023-07-19', 10, 500, '2023-10-18', '2024-08-05'),
        ],
        'elliott': {
            '2023-07-19': ['(1)'],
            '2023-10-18': ['(2)'],
            '2024-07-05': ['(3)'],
            '2024-08-05': ['(4)'],
            '2025-02-14': ['(5)'],
        },
    },
    TME: {
        'lines': [
            ('2024-07-23', '2024-10-02', 10, 100),
            ('2024-09-18', '2024-11-13', 10, 100),
        ],
    },
    AAPL: {
        'lines': [
            ('2023-07-31', '2024-12-26', 10, 10),
            ('2024-04-19', 10, 300, '2023-07-31', '2024-12-26'),
            ('2023-10-26', 10, 400, '2023-07-31', '2024-12-26'),

            ('2024-08-06', '2024-09-16', 10, 40),
        ],
        'elliott': {
            '2023-07-31': ['(1)'],
            '2023-10-26': ['A'],
            '2023-12-14': ['B'],
            '2024-01-05': ['i'],
            '2024-01-23': ['ii'],
            '2024-03-07': ['iii'],
            '2024-04-12': ['iv'],
            '2024-04-19': ['v', 'C', '(2)'],
            '2024-07-16': ['3'],
            '2024-08-06': ['a'],
            '2024-08-29': ['b'],
            '2024-09-16': ['c'],
            '2024-10-21': ['d'],
            '2024-11-04': ['e', '4'],
            '2024-12-26': ['(3)'],
            '2025-01-21': ['A'],
        },
    },
    ASML: {
        'lines': [
            # ('2024-07-10', '2024-10-14', 10, 100),
        ],
        'elliott': {
            '2023-02-02': ['(1)'],
            '2023-10-03': ['(2)'],
            '2023-12-14': ['1'],
            '2024-01-04': ['2'],
            '2024-03-07': ['3'],
            '2024-05-01': ['4'],
            '2024-07-10': ['5', '(3)'],
            '2024-11-20': ['(4)'],
        },
    },
    QCOM: {
        'lines': [
            ('2023-10-25', '2024-04-19', 10, 80),
            ('2024-03-07', 10, 100, '2023-10-25', '2024-04-19'),
        ],
    },
    GS: {
        'lines': [
            ('2023-10-27', '2024-04-12', 10, 300),
            ('2023-09-14', 10, 400, '2023-10-27', '2024-04-12'),
        ],
    },
    INTC: {
        'lines': [
            ('2024-04-01', '2024-07-18', 10, 100),
            ('2024-05-10', 10, 100, '2024-04-01', '2024-07-18'),

            # ('2024-01-25', '2024-03-07', 10, 300),
            # ('2024-02-02', 10, 300, '2024-01-25', '2024-03-07'),
        ],
        'elliott': {
            '2023-04-04': ['1'],
            '2023-05-25': ['2'],
            '2023-06-16': ['3'],
            '2023-08-17': ['4'],
            '2023-09-12': ['i'],
            '2023-10-26': ['ii'],
            '2023-11-29': ['iii'],
            '2023-12-06': ['iv'],
            '2023-12-27': ['v', '5'],
            '2024-02-28': ['1'],
            '2024-04-01': ['2'],
            '2024-05-10': ['3'],
            '2024-07-18': ['4'],
            '2024-08-07': ['5'],
            '2024-08-30': ['i'],
            '2024-09-06': ['ii'],
            '2024-09-26': ['iii'],
            '2024-10-31': ['iv'],
            '2024-11-07': ['v', '1'],
            '2024-12-19': ['2'],
            '2025-01-22': ['i'],
        },
    },
    SEA: {
        'lines': [
            ('2024-08-05', '2025-01-02', 10, 60),
            ('2024-12-04', 10, 80, '2024-08-05', '2025-01-02'),
        ],
        'elliott': {
            '2024-03-14': ['1'],
            '2024-04-15': ['2'],
            '2024-05-17': ['3'],
            '2024-05-30': ['4'],
            '2024-06-18': ['5', '(1)'],
            '2024-08-05': ['(2)'],
            '2024-08-23': ['1'],
            '2024-09-09': ['2'],
            '2024-10-24': ['3'],
            '2024-11-08': ['4'],
            '2024-12-04': ['5', '(3)'],
            '2025-01-02': ['(4)'],
            '2025-01-30': ['1'],
        }
    },
    GILD: {
        'lines': [
            ('2024-07-03', '2025-01-08', 10, 10),
            ('2024-11-07', 10, 100, '2024-07-03', '2025-01-08'),
        ],
    },
    MA: {
        'lines': [
            ('2023-10-27', '2024-07-25', 10, 200),
            ('2024-03-21', 300, 300, '2023-10-27', '2024-07-25'),

            ('2024-07-25', '2025-01-10', 10, 100),
            ('2024-10-18', 10, 100, '2024-07-25', '2025-01-10'),
        ],
    },
    GOOG: {
        'lines': [
            ('2022-11-30', '2023-10-11', 10, 100),
            ('2022-12-28', 10, 300, '2022-11-30', '2023-10-11'),

            ('2024-03-06', '2024-09-09', 20, 160),
            ('2024-07-10', 20, 200, '2024-03-06', '2024-09-09'),
        ],
        'elliott': {
            '2022-11-30': ['1'],
            '2022-12-28': ['2'],
            '2023-02-02': ['i'],
            '2023-02-24': ['ii'],
            '2023-06-06': ['iii'],
            '2023-07-10': ['iv'],
            '2023-10-11': ['v', '3'],
            '2023-10-27': ['4'],
            '2024-01-29': ['5', '(1)'],
            '2024-03-06': ['(2)'],
            '2024-07-10': ['(3)'],
            '2024-08-06': ['A'],
            '2024-08-20': ['B'],
            '2024-09-09': ['C', '(4)'],
            '2024-11-12': ['1'],
            '2024-11-22': ['2'],
            '2024-12-16': ['3'],
            '2025-01-14': ['4'],
            '2025-02-04': ['5', '(5)'],
        },
    },
    AMZN: {
        'lines': [
            ('2023-10-26', '2024-08-05', 10, 200),
            ('2024-07-02', 100, 200, '2023-10-26', '2024-08-05'),
        ],
        'elliott': {
            '2023-10-26': ['(2)'],
            '2024-07-02': ['(3)'],
            '2024-08-05': ['(4)'],
            '2024-08-21': ['1'],
            '2024-09-06': ['2'],
            '2024-12-16': ['3'],
            '2025-01-14': ['4'],
            '2025-02-04': ['5', '(5)'],
        },
    },
    PG: {
        'lines': [
            ('2023-10-11', '2025-01-10', 10, 100),
            ('2023-05-01', 10, 500, '2023-10-11', '2025-01-10'),
        ],
        'elliott': {
            '2023-05-01': ['(1)'],
            '2023-10-11': ['(2)'],
            '2023-11-30': ['1'],
            '2023-12-20': ['2'],
            '2024-09-10': ['3'],
            '2024-11-06': ['4'],
            '2024-12-02': ['5', '(3)'],
        },
    },
    XOM: {
        'lines': [
            ('2023-04-28', '2023-09-27', 20, 300),
            ('2024-06-17', 10, 200, '2023-04-28', '2023-09-27'),
            ('2024-01-18', 10, 300, '2023-04-28', '2023-09-27'),
        ],
        'elliott': {
            '2023-02-10': ['(3)'],
            '2023-03-17': ['A'],
            '2023-09-27': ['B'],
            '2024-01-18': ['C', '(4)'],
            '2024-10-07': ['1'],
        },
    },
    MCD: {
        'lines': [
            ('2024-10-18', '2024-12-09', 10, 100),
        ],
        'elliott': {
            '2023-08-21': ['A'],
            '2023-09-14': ['B'],
            '2023-10-12': ['C', '(A)'],
            '2023-12-13': ['A'],
            '2024-01-05': ['B'],
            '2024-01-19': ['C', '(B)'],
            '2024-02-06': ['1'],
            '2024-02-23': ['2'],
            '2024-04-16': ['3'],
            '2024-04-23': ['4'],
            '2024-06-24': ['iv'],
            '2024-07-09': ['5', '(C)'],
            '2024-07-17': ['1'],
            '2024-07-25': ['2'],
            '2024-08-21': ['3'],
            '2024-09-03': ['4'],
            '2024-10-18': ['5', '(1)'],
            '2024-11-21': ['W'],
            '2024-12-09': ['X'],
            '2025-01-16': ['Y', '(2)'],
        }
    },
    ORCL: {
        'lines': [
            ('2023-12-14', '2024-08-07', 10, 200),
            ('2023-06-15', 10, 400, '2023-12-14', '2024-08-07'),
        ],
        'elliott': {
            '2023-06-15': ['(1)'],
            '2023-12-14': ['(2)'],
            '2024-07-12': ['(3)'],
            '2024-08-07': ['(4)'],
            '2024-09-16': ['3'],
            '2024-10-03': ['4'],
            '2024-10-09': ['i'],
            '2024-11-08': ['ii'],
            '2024-11-21': ['(5)'],
            '2025-01-13': ['(A)'],
            '2025-01-23': ['(B)'],
        },
    },
    JPM: {
        'lines': [
            ('2023-10-27', '2024-08-05', 10, 200),
            ('2023-07-24', 10, 500, '2023-10-27', '2024-08-05'),
        ],
        'elliott': {
            '2023-07-24': ['(1)'],
            '2023-10-27': ['(2)'],
            '2024-07-17': ['(3)'],
            '2024-08-05': ['(4)'],
            '2025-02-18': ['(5)'],
        },
    },
    NVO: {
        'lines': [
            ('2024-08-07', '2024-12-20', 10, 40),
            ('2024-08-30', 10, 240, '2024-08-07', '2024-12-20'),
        ],
        'elliott': {
            '2023-04-21': ['(1)'],
            '2023-07-11': ['(2)'],
            '2024-03-07': ['(3)'],
            '2024-04-19': ['(4)'],
            '2024-06-25': ['(5)'],
            '2024-08-07': ['1'],
            '2024-08-30': ['2'],
            '2024-11-18': ['3'],
            '2024-12-11': ['4'],
            '2025-01-17': ['5'],
        },
    },
    AVGO: {
        'lines': [
            ('2023-10-26', '2024-08-07', 10, 200),
            ('2024-06-17', 10, 200, '2023-10-26', '2024-08-07'),
        ],
        'elliott': {
            '2023-09-21': ['(2)'],
            '2023-12-18': ['1'],
            '2024-01-04': ['2'],
            '2024-03-07': ['3'],
            '2024-04-19': ['4'],
            '2024-06-17': ['5', '(3)'],
            '2024-08-07': ['(4)'],
            '2024-08-19': ['1'],
            '2024-09-06': ['2'],
            '2024-10-09': ['3'],
            '2024-11-27': ['4'],
            '2024-12-16': ['5', '(5)'],
            '2025-01-27': ['A'],
            '2025-02-12': ['B'],
            '2025-03-06': ['C'],
        },
    },
    YY: {
        'lines': [
            ('2024-06-14', '2024-11-01', 10, 100),
            ('2024-07-09', 10, 160, '2024-06-14', '2024-11-01'),
        ],
    },
    WMT: {
        'lines': {
            ('2024-10-07', '2025-01-02', 10, 10),
            ('2024-12-06', 10, 40, '2024-10-07', '2025-01-02'),

            ('2024-03-21', '2024-07-17', 10, 10),
            ('2024-05-01', 10, 300, '2024-03-21', '2024-07-17'),
        },
        'elliott': {
            '2024-03-21': ['1'],
            '2024-05-01': ['2'],
            '2024-07-17': ['3'],
            '2024-08-07': ['4'],
            '2024-09-13': ['i'],
            '2024-10-07': ['ii'],
            '2024-12-06': ['iii'],
            '2025-01-02': ['iv'],
            '2025-02-13': ['v', '5'],
        },
    },
    MSFT: {
        'lines': [
            ('2023-09-26', '2024-04-30', 10, 10),
            ('2024-03-21', 10, 100, '2023-09-26', '2024-04-30'),

            ('2024-07-05', '2024-12-17', 10, 10),
            ('2024-08-05', 10, 200, '2024-07-05', '2024-12-17'),
        ],
        'elliott': {
            '2023-07-18': ['(1)'],
            '2023-09-26': ['(2)'],
            '2024-03-21': ['(3)'],
            '2024-04-30': ['(4)'],
            '2024-07-05': ['(5)'],
            '2024-08-05': ['(A)'],
            '2024-12-17': ['(B)'],
        },
    },
    TTD: {
       'elliott': {
           '2023-07-31': ['(1)'],
           '2023-08-17': ['A'],
           '2023-09-11': ['B'],
           '2023-11-13': ['C', '(2)'],
           '2023-12-19': ['i'],
           '2024-01-16': ['ii'],
           '2024-02-16': ['iii'],
           '2024-04-19': ['iv'],
           '2024-07-09': ['v', '1'],
           '2024-08-02': ['2'],
           '2024-08-23': ['i'],
           '2024-09-09': ['ii'],
           '2024-11-07': ['iii'],
           '2024-11-18': ['iv'],
           '2024-12-04': ['v', '3'],
       }
    },
    ADBE: {
        'lines': [
            ('2024-02-02', '2024-09-12', 10, 80),
            ('2024-06-03', 10, 200, '2024-02-02', '2024-09-12'),
        ],
        'elliott': {
            '2023-03-31': ['(1)'],
            '2023-05-12': ['(2)'],
            '2023-08-01': ['(3)'],
            '2023-09-27': ['(4)'],
            '2024-02-02': ['(5)'],
            '2024-06-03': ['(A)'],
            '2024-09-12': ['(B)'],
            '2024-10-31': ['1'],
            '2024-12-06': ['2'],
            '2025-01-10': ['3'],
        },
    },
    CVX: {
        'elliott': {
        }
    },
    BAC: {
        'lines': [
            ('2024-01-18', '2024-08-05', 10, 200),
            ('2024-07-16', 10, 120, '2024-01-18', '2024-08-05'),
        ],
        'elliott': {
            '2023-12-14': ['(1)'],
            '2024-01-18': ['(2)'],
            '2024-07-16': ['(3)'],
            '2024-08-05': ['(4)'],
            '2024-11-27': ['(5)'],
        },
    },
    JNJ: {
        'elliott': {
            '2023-03-22': ['(W)'],
            '2023-07-28': ['(X)'],
            '2024-04-16': ['(Y)'],
            '2024-09-10': ['(X)'],
            '2025-01-10': ['A'],
        },
    },
    MRK: {
        'lines': [
            ('2024-08-06', '2024-11-15', 10, 80),
            ('2024-09-18', 10, 160, '2024-08-06', '2024-11-15'),
        ],
        'elliott': {
        },
    },
    DIS: {
        'lines': [
            ('2024-09-06', '2024-10-07', 10, 100),
        ]
    },
    VISA: {
        'lines': [
            ('2023-10-03', '2024-07-25', 10, 10),
            ('2024-03-21', 10, 250, '2023-10-03', '2024-07-25'),

            ('2024-09-25', '2025-01-13', 10, 100),
            ('2024-09-17', 10, 160, '2024-09-25', '2025-01-13'),
        ],
    },
    TCOM: {
        'elliott': {
            '2023-01-26': ['(1)'],
            '2023-05-25': ['(2)'],
            '2024-05-20': ['(3)'],
            '2024-08-02': ['(4)'],
            '2024-12-09': ['(5)'],
        },
    },
}
