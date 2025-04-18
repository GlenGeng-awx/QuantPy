from conf import *

#
# lines
# -----
#   date1, date2, prev_len, post_len
#   date, prev_len, post_len, date1, date2
#   date, prev_len, post_len
#
# elliott
# -------
#  (1), (2), (3), (4), (5), (A), (B), (C), (W), (X), (Y)
#   1,   2,   3,   4,   5,   A,   B,   C,   W,   X,   Y
#   i,   ii,  iii, iv,  v,   a,   b,   c,   w,   x,   y
#
# tech
# ----
#   S:      Shoulder
#   H:      Head
#   H 3%:   Head 103%
#
#   Top/Bottom: for Box
#
#   -------------------
#   Wait, Warn
#   Call, Put
#
#   -------------------
#   Brk:    Break
#   Ack:    Reach the target
#
#   G:      Gap
#   BG:     Breakaway Gap
#   RG:     Runaway Gap
#   EG:     Exhaustion Gap
#
CORE_BANKING = {
    IXIC: {
        'lines': [
            ('2023-07-19', '2024-07-10', 10, 20),
            ('2023-10-26', 10, 300, '2023-07-18', '2024-07-10'),

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

            ('2025-02-19', '2025-03-25', 10, 20),

            ('2022-12-02', 60, 80),
            ('2024-04-19', 5, 300),
            ('2024-07-10', 5, 300),
            ('2024-08-07', 70, 200),
            ('2025-03-13', 5, 100),
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
            '2024-08-21': ['1'],
            '2024-09-06': ['2'],
            '2024-12-16': ['3'],
            '2025-01-14': ['4'],
            '2025-02-19': ['5', '(5)'],
            '2025-03-13': ['(A)'],
            '2025-03-25': ['(B)'],
            '2025-04-08': ['(C)'],
        },
        'tech': {
            '2024-07-10': ['S'],
            '2024-12-16': ['H'],
            '2025-02-19': ['H'],
            '2025-03-06': ['Brk'],
            '2025-04-04': ['EG'],
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
            ('2023-07-31', 100, 350),
            ('2023-05-31', 10, 350),
        ],
        'tech': {
            '2023-05-31': ['S'],
            '2024-01-22': ['H'],
            '2024-08-28': ['S'],
            '2024-09-26': ['Brk'],
        },
    },
    TSLA: {
        'lines': [
            ('2023-07-18', '2024-12-17', 10, 10),
            ('2024-04-22', 10, 300, '2023-07-18', '2024-12-17'),

            ('2023-07-18', '2023-12-27', 10, 10),
            ('2023-10-30', 10, 140, '2023-07-18', '2023-12-27'),

            ('2023-02-15', 10, 800),
            ('2023-07-18', 10, 500),
            ('2024-06-11', 10, 300),
        ],
        'elliott': {
            '2023-02-15': ['(1)'],
            '2023-04-26': ['(2)'],
            '2023-07-18': ['(3)'],
            '2023-10-30': ['W'],
            '2023-12-27': ['X'],
            '2024-04-22': ['Y', '(4)'],
            '2024-04-29': ['1'],
            '2024-06-11': ['2'],
            '2024-07-10': ['3'],
            '2024-08-07': ['4'],
            '2024-09-30': ['i'],
            '2024-10-23': ['ii'],
            '2024-11-11': ['iii'],
            '2024-11-27': ['iv'],
            '2024-12-17': ['v', '5', '(5)'],
        },
    },
    HK_0700: {
        'lines': [
            ('2024-03-05', '2024-07-25', 10, 50),
            ('2024-05-17', 10, 300, '2024-03-05', '2024-07-25'),

            ('2024-10-07', '2024-12-20', 10, 20),
            ('2024-11-26', 10, 40, '2024-10-07', '2024-12-20'),
        ],
        'elliott': {
            '2023-01-27': ['(1)'],
            '2023-05-31': ['W'],
            '2023-06-16': ['X'],
            '2024-01-22': ['Y', '(2)'],
            '2024-01-25': ['1'],
            '2024-03-05': ['2'],
            '2024-05-17': ['3'],
            '2024-07-25': ['4'],
            '2024-10-07': ['5', '(3)'],
            '2024-11-26': ['A'],
            '2024-12-20': ['B'],
            '2025-01-13': ['C', '(4)'],
            '2025-03-06': ['(5)'],
        },
    },
    BILI: {
        'lines': [
            ('2024-08-22', '2025-01-10', 150, 100),
        ],
        'elliott': {
            '2024-06-21': ['(1)'],
            '2024-08-22': ['(2)'],
            '2024-10-02': ['(3)'],
            '2024-11-26': ['A'],
            '2024-12-09': ['B'],
            '2025-01-10': ['C', '(4)'],
            '2025-03-07': ['1'],
        },
    },
    UBER: {
        'lines': [
            ('2024-12-31', '2025-02-05', 10, 50),
            ('2025-02-18', '2025-03-24', 10, 50),

            ('2024-02-15', 10, 300),
            ('2024-08-05', 180, 200),
        ],
        'elliott': {
            '2022-09-15': ['(1)'],
            '2022-12-27': ['(2)'],
            '2024-02-15': ['(3)'],
            '2024-08-05': ['(4)'],
            '2024-10-11': ['(5)'],
            '2024-12-13': ['(A)'],
            '2025-02-18': ['(B)'],
        },
        'tech': {
            '2024-02-15': ['S'],
            '2024-10-11': ['H'],
            '2025-02-18': ['S'],
            '2025-04-04': ['BG'],
        },
    },
    PDD: {
        'lines': [
            ('2025-02-21', 10, 100),
        ],
        'elliott': {
            '2023-01-27': ['(1)'],
            '2023-05-25': ['(2)'],
            '2024-01-11': ['(3)'],
            '2024-03-08': ['(4)'],
            '2024-05-24': ['(5)'],
            '2024-08-28': ['(A)'],
            '2024-10-04': ['(B)'],
            '2024-12-30': ['(C)'],
        }
    },
    IQ: {
        'lines': [
            ('2023-02-28', '2024-05-16', 10, 10),
            ('2024-02-05', 10, 240, '2023-02-28', '2024-05-16'),

            ('2025-01-13', '2025-03-03', 10, 40),

            ('2024-12-09', 30, 100),
        ],
        'tech': {
            '2024-11-22': ['S'],
            '2025-01-13': ['H'],
            '2025-03-03': ['S'],
        },
    },
    BABA: {
        'lines': [
            ('2024-05-17', '2024-10-07', 10, 160),
        ],
    },
    BA: {
        'lines': [
            ('2022-08-16', '2023-07-31', 10, 100),
            ('2022-09-30', 10, 300, '2022-08-16', '2023-07-31'),

            ('2024-11-14', 10, 100),
            ('2024-12-27', 20, 100),
        ],
        'elliott': {
            '2022-08-16': ['(1)'],
            '2022-09-30': ['(2)'],
            '2023-07-31': ['(3)'],
            '2023-10-25': ['(4)'],
            '2023-12-15': ['(5)'],
            '2024-04-24': ['(A)'],
            '2024-07-31': ['(B)'],
            '2024-11-14': ['(C)'],
            '2025-02-12': ['(1)'],
            '2025-04-04': ['(2)'],
        },
        'tech': {
            '2025-03-25': ['Wait', 'Call'],
        },
    },
    COIN: {
        'lines': [
            ('2023-10-27', '2024-09-06', 10, 10),
            ('2024-03-25', 10, 190, '2023-10-27', '2024-09-06'),

            ('2024-03-25', 10, 300),
            ('2024-09-06', 150, 200),
        ],
        'elliott': {
            '2023-02-02': ['(1)'],
            '2023-05-03': ['(2)'],
            '2023-07-19': ['1'],
            '2023-10-27': ['2'],
            '2023-12-28': ['3'],
            '2024-02-05': ['4'],
            '2024-03-25': ['5', '(3)'],
            '2024-05-16': ['W'],
            '2024-07-22': ['X'],
            '2024-09-06': ['Y', '(4)'],
            '2024-12-06': ['(5)'],
            '2024-12-31': ['1'],
            '2025-01-30': ['2'],
            '2025-03-13': ['3'],
            '2025-03-25': ['4'],
            '2025-04-08': ['5', '(A)'],
        },
        'tech': {
            '2024-03-25': ['S'],
            '2024-12-06': ['H'],
        },
    },
    PLTR: {
        'lines': [
            ('2025-01-13', 10, 100),
            ('2025-03-25', 10, 100),
        ],
        'elliott': {
            '2023-02-15': ['(1)'],
            # '2023-03-10': ['(2)'],
            '2023-08-01': ['(3)'],
            '2023-09-26': ['(4)'],
            '2023-11-20': ['1'],
            '2024-01-05': ['2'],
            '2024-03-07': ['3'],
            '2024-04-19': ['4'],
            '2024-07-23': ['i'],
            '2024-08-05': ['ii'],
            '2024-12-24': ['iii'],
            '2025-01-13': ['iv'],
            '2025-02-18': ['v', '5', '(5)'],
        },
    },
    NVDA: {
        'lines': [
            ('2025-01-06', '2025-03-24', 5, 20),

            ('2024-06-18', 10, 250),
            ('2024-08-07', 60, 200),
        ],
        'elliott': {
            '2023-08-31': ['(1)'],
            '2023-10-26': ['(2)'],
            '2024-06-18': ['(3)'],
            '2024-08-07': ['(4)'],
            '2024-11-07': ['(5)'],
            '2024-12-18': ['1'],
            '2025-01-06': ['2'],
            '2025-03-10': ['3'],
            '2025-03-24': ['4'],
            '2025-04-04': ['5', '(A)'],
        },
        'tech': {
            '2024-06-18': ['S'],
            '2024-07-10': ['S'],
            '2024-11-07': ['H'],
            '2025-01-06': ['H'],
        },
    },
    BEKE: {
        'lines': [
        ],
    },
    RIVN: {
        'lines': [
            ('2023-12-19', '2025-01-03', 10, 100),
            ('2024-04-15', '2024-11-06', 10, 100),
        ],
        'elliott': {
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
            ('2025-02-14', '2025-03-19', 10, 20),
            ('2025-01-22', 10, 60),
        ],
    },
    BNTX: {
        'lines': [
            ('2024-12-19', 25, 60),
        ],
        'tech': {
            '2024-12-06': ['S'],
            '2025-01-07': ['H'],
            '2025-01-28': ['H'],
            '2025-02-18': ['S'],
            '2025-03-10': ['Brk'],
            '2025-03-31': ['EG']
        },
    },
    XPEV: {
        'lines': [
        ],
        'elliott': {
            '2024-11-11': ['1'],
            '2025-01-02': ['2'],
            '2025-03-11': ['3'],
            '2025-04-08': ['4'],
        },
    },
    EBAY: {
        'lines': [
            ('2024-05-06', '2024-10-31', 10, 140),
            ('2024-10-08', 10, 100, '2024-05-06', '2024-10-31'),

            ('2025-02-27', 40, 40),
        ],
        'tech': {
            '2025-01-08': ['S'],
            '2025-02-25': ['H'],
            '2025-04-01': ['S'],
            '2025-04-04': ['Brk'],
        },
    },
    META: {
        'lines': [
            ('2023-07-28', '2024-04-05', 10, 10),
            ('2023-10-26', 10, 160, '2023-07-28', '2024-04-05'),
            ('2024-07-25', 10, 200, '2023-07-28', '2024-04-05'),

            ('2024-07-05', 10, 300),
            ('2024-07-25', 10, 300),
            ('2024-12-31', 30, 100),
            ('2024-12-11', 10, 100),
        ],
        'elliott': {
            '2023-02-07': ['(1)'],
            '2023-02-27': ['(2)'],
            '2023-07-28': ['1'],
            '2023-10-26': ['2'],
            '2024-04-05': ['3'],
            '2024-04-30': ['4'],
            '2024-07-05': ['5', '(3)'],
            '2024-07-25': ['(4)'],
            '2024-10-04': ['3'],
            '2024-11-15': ['4'],
            '2025-02-14': ['5', '(5)'],
        },
        'tech': {
            '2024-12-11': ['S'],
            '2025-02-14': ['H'],
            '2025-03-25': ['S'],
        },
    },
    LI: {
        'lines': [
            ('2023-08-07', '2023-11-20', 10, 10),
            ('2023-10-20', 10, 100, '2023-08-07', '2023-11-20'),

            ('2024-08-28', '2025-01-13', 10, 100),
            ('2024-10-07', 10, 160, '2024-08-28', '2025-01-13'),
        ],
        'elliott': {
        },
    },
    ZM: {
        'lines': [
            ('2025-01-17', 50, 50),
            ('2024-11-25', 10, 60),

            ('2024-10-03', 5, 200),
        ],
        'elliott': {
            '2024-08-27': ['1'],
            '2024-09-18': ['2'],
            '2024-11-12': ['3'],
            '2024-11-19': ['4'],
            '2024-11-25': ['5'],
            '2025-01-17': ['A'],
            '2025-01-28': ['B'],
        },
        'tech': {
            '2024-11-25': ['Top'],
            '2025-01-28': ['Top'],
            '2025-02-25': ['BG', 'Brk'],
        },
    },
    TSM: {
        'lines': [
            ('2023-09-26', '2024-08-05', 10, 170),

            ('2025-03-13', '2025-03-19', 5, 10),
            ('2025-03-12', 5, 15, '2025-03-13', '2025-03-19'),

            ('2024-07-10', 10, 200),
            ('2024-08-05', 120, 200),
        ],
        'elliott': {
            '2023-06-14': ['(1)'],
            '2023-09-26': ['(2)'],
            '2024-03-07': ['3'],
            '2024-04-19': ['4'],
            '2024-07-10': ['(3)'],
            '2024-08-05': ['(4)'],
            '2025-01-23': ['(5)'],
            '2025-04-08': ['(A)'],
        },
        'tech': {
            '2024-07-10': ['S'],
            '2025-01-23': ['H'],
        },
    },
    AMD: {
        'lines': [
            ('2024-03-07', '2024-10-08', 10, 10),
            ('2024-08-07', 100, 200, '2024-03-07', '2024-10-08'),

            ('2022-11-30', 10, 600),
            ('2025-02-19', 20, 100),
        ],
        'elliott': {
            '2022-11-30': ['(1)'],
            '2023-01-05': ['(2)'],
            '2023-06-12': ['(3)'],
            '2023-10-26': ['(4)'],
            '2024-03-07': ['(5)'],
            '2024-05-01': ['A'],
            '2024-07-10': ['B'],
            '2024-08-07': ['C', '(W)'],
            '2024-10-08': ['(X)'],
            '2025-03-10': ['A'],
            '2025-03-25': ['B'],
            '2025-04-08': ['C', '(Y)'],
        },
    },
    PFE: {
        'lines': [
        ],
        'elliott': {
        },
    },
    NIO: {
        'lines': [
            ('2023-01-27', '2023-07-12', 10, 400),
            ('2023-03-31', 10, 500, '2023-01-27', '2023-07-12'),
        ],
    },
    BLOCK: {
        'lines': [
            ('2023-10-30', '2024-08-05', 10, 10),
            ('2023-12-27', 10, 240, '2023-10-30', '2024-08-05'),
        ],
        'tech': {
            '2025-03-19': ['Put'],
        },
    },
    SHOP: {
        'lines': [
            ('2024-09-06', '2025-01-14', 10, 40),
        ],
        'elliott': {
            '2022-12-01': ['(1)'],
            '2022-12-28': ['(2)'],
            '2023-07-13': ['3'],
            '2023-10-27': ['4'],
            '2024-02-09': ['5', '(3)'],
            '2024-04-15': ['W'],
            '2024-05-06': ['X'],
            '2024-08-05': ['Y', '(4)'],
            '2024-08-21': ['1'],
            '2024-09-06': ['2'],
            '2024-12-17': ['3'],
            '2025-01-14': ['4'],
            '2025-02-18': ['5', '(5)']
        },
    },
    ETSY: {
        'lines': [
            ('2024-01-31', '2024-05-02', 5, 100),
            ('2024-02-12', 5, 200, '2024-01-31', '2024-05-02'),
        ],
    },
    MS: {
        'lines': [
        ],
        'elliott': {
            '2024-01-02': ['(1)'],
            '2024-01-18': ['(2)'],
            '2024-07-17': ['(3)'],
            '2024-08-05': ['(4)'],
            '2025-02-06': ['(5)'],
        },
    },
    CPNG: {
        'lines': [
            ('2024-11-05', '2025-02-19', 10, 40),
            ('2025-01-10', 10, 100, '2024-11-05', '2025-02-19'),

            ('2024-07-25', 500, 200),
        ],
        'elliott': {
            '2023-08-10': ['(1)'],
            '2024-02-05': ['(2)'],
            '2024-05-07': ['(3)'],
            '2024-07-25': ['(4)'],
            '2024-11-05': ['(5)'],
        },
        'tech': {
            '2024-05-07': ['S'],
            '2024-11-05': ['H'],
            '2025-02-19': ['S'],
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
        ],
    },
    ERIC: {
        'lines': [
        ],
        'elliott': {
            '2023-12-27': ['1'],
            '2024-04-15': ['2'],
            '2025-01-23': ['3'],
            '2025-04-08': ['4'],
        },
    },
    LVMUY: {
        'lines': [
        ],
    },
    OKTA: {
        'lines': [
            ('2024-03-07', 10, 300),
        ],
    },
    NFLX: {
        'lines': [
            ('2023-10-18', '2024-08-05', 10, 200),

            ('2024-07-05', 10, 200),
            ('2024-12-11', 10, 200),
            ('2025-01-14', 50, 100),
        ],
        'elliott': {
            '2023-07-19': ['(1)'],
            '2023-10-18': ['(2)'],
            '2024-07-05': ['(3)'],
            '2024-08-05': ['(4)'],
            '2024-12-11': ['3'],
            '2025-02-14': ['(5)'],
        },
        'tech': {
            '2024-12-11': ['S'],
            '2025-02-14': ['H'],
            '2025-03-25': ['H'],
        },
    },
    TME: {
        'lines': [
            ('2024-07-23', '2024-12-09', 10, 60),
            ('2024-09-18', '2025-01-13', 10, 20),
        ],
        'tech': {
            '2025-02-12': ['Brk'],
        },
    },
    AAPL: {
        'lines': [
            ('2025-03-13', '2025-03-28', 2, 7),

            ('2022-10-28', 30, 120),
            ('2023-07-31', 10, 500),
            ('2024-04-19', 10, 400),
            ('2024-07-16', 10, 200),
            ('2025-01-21', 80, 60),
        ],
        'elliott': {
            '2023-02-15': ['(1)'],
            '2023-03-01': ['(2)'],
            '2023-07-31': ['(3)'],
            '2024-04-19': ['(4)'],
            '2024-12-26': ['(5)'],
            '2025-04-08': ['(A)'],
        },
        'tech': {
            '2022-11-09': ['S'],
            '2023-01-05': ['H'],
            '2023-03-01': ['S'],
            '2024-07-16': ['S'],
            '2024-10-21': ['S'],
            '2024-12-26': ['H', 'H'],
            '2025-02-24': ['S'],
            '2025-04-07': ['Ack'],
        },
    },
    ASML: {
        'lines': [
            ('2024-07-10', '2025-02-13', 10, 50),
            ('2024-11-20', 10, 100, '2024-07-10', '2025-02-13'),

            ('2025-01-06', 10, 100),
            ('2025-01-28', 30, 100),
        ],
        'elliott': {
            '2023-07-18': ['(1)'],
            '2023-10-03': ['(2)'],
            '2024-03-07': ['(3)'],
            '2024-05-01': ['(4)'],
            '2024-07-10': ['(5)'],
            '2024-11-20': ['(A)'],
            '2025-02-13': ['(B)'],
        },
        'tech': {
            '2025-01-06': ['Top'],
            '2025-02-13': ['Top'],
            '2025-04-09': ['Put'],
        },
    },
    QCOM: {
        'lines': [
            ('2023-07-31', 10, 600),

            ('2024-10-14', 40, 100),
            ('2024-11-20', 80, 200),
        ],
        'elliott': {
            '2023-07-31': ['(1)'],
            '2023-10-25': ['(2)'],
            '2024-03-07': ['(3)'],
            '2024-04-19': ['(4)'],
            '2024-06-18': ['(5)'],
            '2024-08-07': ['(A)'],
            '2025-02-05': ['(B)'],
            '2025-04-08': ['(C)'],
        },
        'tech': {
            '2024-10-14': ['Top'],
            '2025-02-05': ['Top'],
        },
    },
    GS: {
        'lines': [
            ('2024-06-11', 10, 300),
            ('2025-03-13', 110, 40),
        ],
        'elliott': {
            '2024-01-08': ['(1)'],
            '2024-02-14': ['(2)'],
            '2024-06-11': ['4'],
            '2024-08-30': ['(3)'],
            '2024-09-10': ['(4)'],
            '2025-02-18': ['(5)'],
            '2025-03-13': ['(A)'],
            '2025-03-25': ['(B)'],
        },
        'tech': {
            '2024-11-29': ['S'],
            '2025-02-18': ['H'],
            '2025-03-25': ['S'],
            '2025-04-03': ['Brk'],
        },
    },
    INTC: {
        'lines': [
            ('2024-04-01', '2024-07-18', 10, 10),
            ('2024-05-10', 10, 80, '2024-04-01', '2024-07-18'),

            ('2024-11-07', 80, 100),
            ('2024-09-06', 30, 160),
        ],
        'elliott': {
        },
    },
    SEA: {
        'lines': [
            ('2025-01-02', 35, 100),
            ('2025-03-03', 30, 40),
        ],
        'elliott': {
            '2024-06-18': ['(1)'],
            '2024-08-05': ['(2)'],
            '2024-12-04': ['(3)'],
            '2025-01-02': ['(4)'],
            '2025-03-05': ['(5)'],
        },
        'tech': {
            '2025-02-18': ['S'],
            '2025-03-05': ['H'],
            '2025-04-02': ['S'],
            '2025-04-03': ['BG', 'Brk'],
        },
    },
    GILD: {
        'lines': [
            ('2024-07-03', '2025-01-08', 10, 100),
            ('2024-11-07', 10, 100, '2024-07-03', '2025-01-08'),
        ],
    },
    MA: {
        'lines': [
            ('2023-01-25', '2024-03-21', 10, 300),
            ('2023-10-27', 10, 400, '2023-01-25', '2024-03-21'),

            ('2024-03-21', 10, 300),
            ('2024-07-25', 10, 200),
            ('2024-12-26', 10, 100),
        ],
        'elliott': {
            '2023-01-25': ['(1)'],
            '2023-03-13': ['(2)'],
            '2024-03-21': ['(3)'],
            '2024-07-25': ['(4)'],
            '2025-02-28': ['(5)'],
            '2025-04-08': ['(A)'],
        },
    },
    GOOG: {
        'lines': [
            ('2023-10-27', '2024-09-09', 20, 200),
            ('2024-07-10', 20, 160, '2023-10-27', '2024-09-09'),

            ('2024-07-10', 10, 200),
            ('2024-09-09', 130, 200),
        ],
        'elliott': {
            '2023-10-11': ['(1)'],
            '2023-10-27': ['(2)'],
            '2024-07-10': ['(3)'],
            '2024-09-09': ['(4)'],
            '2025-02-04': ['(5)'],
            '2025-04-08': ['(A)'],
        },
        'tech': {
            '2024-07-10': ['S'],
            '2025-02-04': ['H'],
        },
    },
    AMZN: {
        'lines': [
            ('2023-10-26', '2024-08-05', 10, 200),
            ('2024-07-02', 100, 160, '2023-10-26', '2024-08-05'),

            ('2023-09-13', 10, 500),
            ('2024-09-24', 10, 200),
            ('2024-08-05', 150, 200),
        ],
        'elliott': {
            '2023-09-13': ['(1)'],
            '2023-10-26': ['(2)'],
            '2024-07-02': ['(3)'],
            '2024-08-05': ['(4)'],
            '2025-01-14': ['4'],
            '2025-02-04': ['(5)'],
        },
        'tech': {
            '2024-11-13': ['S'],
            '2024-12-16': ['H'],
            '2025-02-04': ['H'],
            '2025-03-25': ['S'],
            '2025-04-03': ['Brk'],
        },
    },
    PG: {
        'lines': [
            ('2023-05-01', 20, 200),
        ],
        'tech': {
            '2023-08-08': ['Brk'],
            '2024-02-01': ['Brk'],
        },
    },
    XOM: {
        'lines': [
            ('2023-04-28', '2023-09-27', 20, 500),
            ('2024-01-18', 10, 300, '2023-04-28', '2023-09-27'),
        ],
    },
    MCD: {
        'lines': [
            ('2022-09-30', '2024-07-09', 10, 10),
            ('2024-10-18', 10, 200, '2022-09-30', '2024-07-09'),
            ('2023-06-30', 80, 350, '2022-09-30', '2024-07-09'),

            ('2025-01-16', 10, 100),
            ('2025-02-19', 20, 100),
        ],
        'tech': {
            '2025-02-11': ['S'],
            '2025-03-07': ['H'],
            '2025-04-03': ['S'],
        }
    },
    ORCL: {
        'lines': [
            ('2024-08-07', 300, 200),
            ('2025-01-13', 100, 100),
        ],
        'elliott': {
            '2023-09-11': ['(1)'],
            '2023-10-26': ['(2)'],
            '2024-07-08': ['(3)'],
            '2024-08-07': ['(4)'],
            '2024-11-21': ['(5)'],
            '2025-01-13': ['(A)'],
            '2025-01-23': ['(B)'],
            '2025-04-08': ['(C)'],
        },
        'tech': {
            '2024-07-12': ['S'],
            '2024-11-21': ['H'],
            '2025-01-23': ['H'],
        },
    },
    JPM: {
        'lines': [
            ('2024-04-17', 10, 300),
            ('2024-09-13', 10, 200),
            ('2024-11-25', 10, 100),
            ('2025-03-13', 100, 40),
        ],
        'elliott': {
            '2023-02-15': ['(1)'],
            '2023-03-24': ['(2)'],
            '2023-07-24': ['(3)'],
            '2023-10-27': ['(4)'],
            '2024-03-28': ['1'],
            '2024-04-17': ['2'],
            '2024-08-30': ['3'],
            '2024-09-13': ['4'],
            '2025-02-18': ['(5)'],
        },
        'tech': {
            '2024-11-25': ['S'],
            '2025-02-18': ['H'],
            '2025-03-25': ['S'],
            '2025-04-04': ['Brk'],
        },
    },
    NVO: {
        'lines': [
            ('2024-08-07', '2025-01-17', 10, 100),
            ('2024-08-30', 10, 240, '2024-08-07', '2025-01-17'),

            ('2024-04-19', 50, 130),
        ],
        'elliott': {
            '2024-08-07': ['1'],
            '2024-08-30': ['2'],
            '2025-01-17': ['3'],
            '2025-03-05': ['4'],
        },
        'tech': {
            '2024-03-07': ['S'],
            '2024-06-25': ['H'],
            '2024-08-30': ['S'],
            '2024-10-01': ['Brk'],
        },
    },
    AVGO: {
        'lines': [
            ('2025-03-07', '2025-03-19', 2, 5),
            ('2025-03-06', '2025-03-18', 2, 5),

            ('2024-06-17', 10, 300),
            ('2024-08-07', 10, 200),
        ],
        'elliott': {
            '2023-08-01': ['(1)'],
            '2023-09-21': ['(2)'],
            '2023-12-18': ['1'],
            '2024-01-04': ['2'],
            '2024-03-07': ['3'],
            '2024-04-19': ['4'],
            '2024-06-17': ['5', '(3)'],
            '2024-08-07': ['(4)'],
            '2024-10-09': ['3'],
            '2024-11-27': ['4'],
            '2024-12-16': ['(5)'],
            '2025-01-27': ['1'],
            '2025-02-12': ['2'],
            '2025-03-06': ['3'],
            '2025-03-14': ['4'],
            '2025-04-04': ['5', '(A)'],
        },
        'tech': {
            '2025-03-26': ['Brk'],
        },
    },
    YY: {
        'lines': [
            ('2024-07-09', 70, 60),
        ],
    },
    WMT: {
        'lines': {
            # ('2024-10-07', '2025-01-02', 10, 10),
            # ('2024-12-06', 10, 40, '2024-10-07', '2025-01-02'),
            #
            # ('2024-03-21', '2024-07-17', 10, 10),
            # ('2024-05-01', 10, 300, '2024-03-21', '2024-07-17'),

            ('2024-08-07', 10, 200),
            ('2024-12-06', 10, 100),
            ('2025-01-02', 50, 100),
        },
        'elliott': {
            '2022-11-28': ['(1)'],
            '2023-03-10': ['(2)'],
            '2023-11-15': ['(3)'],
            '2023-12-08': ['(4)'],
            '2024-03-21': ['1'],
            '2024-05-01': ['2'],
            '2024-07-17': ['3'],
            '2024-08-07': ['4'],
            '2024-09-13': ['i'],
            '2024-10-07': ['ii'],
            '2024-12-06': ['iii'],
            '2025-01-02': ['iv'],
            '2025-02-13': ['v', '5', '(5)'],
            '2025-04-08': ['A'],
        },
    },
    MSFT: {
        'lines': [
            ('2023-09-26', '2024-04-30', 10, 10),
            ('2024-03-21', 10, 100, '2023-09-26', '2024-04-30'),

            ('2024-07-05', '2024-12-17', 10, 10),
            ('2024-08-05', 10, 200, '2024-07-05', '2024-12-17'),

            ('2023-07-18', 10, 500),
            ('2024-10-31', 50, 150),
        ],
        'elliott': {
            '2023-07-18': ['(1)'],
            '2023-09-26': ['(2)'],
            '2024-03-21': ['(3)'],
            '2024-04-30': ['(4)'],
            '2024-07-05': ['(5)'],
            '2024-08-05': ['(A)'],
            '2024-12-17': ['(B)'],
            '2025-01-14': ['1'],
            '2025-01-28': ['2'],
            '2025-03-13': ['3'],
            '2025-03-25': ['4'],
            '2025-04-08': ['5', '(C)'],
        },
        'tech': {
            '2024-09-19': ['S'],
            '2024-12-17': ['H'],
            '2025-01-28': ['S'],
            '2025-04-08': ['Ack'],
        },
    },
    TTD: {
       'elliott': {
           '2022-12-02': ['(1)'],
           '2023-01-06': ['(2)'],
           '2023-07-31': ['(3)'],
           '2023-11-13': ['(4)'],
           '2023-12-19': ['1'],
           '2024-01-16': ['2'],
           '2024-07-09': ['3'],
           '2024-08-02': ['4'],
           '2024-12-04': ['5', '(5)'],
       }
    },
    ADBE: {
        'lines': [
            ('2024-02-02', '2024-09-12', 10, 80),
            ('2024-06-03', 10, 260, '2024-02-02', '2024-09-12'),

            ('2023-02-02', 10, 600),
            ('2023-02-24', 10, 600),
        ],
        'elliott': {
            '2023-02-02': ['(1)'],
            '2023-02-24': ['(2)'],
            '2023-09-05': ['(3)'],
            '2023-09-27': ['(4)'],
            '2024-02-02': ['(5)'],
            '2024-06-03': ['(A)'],
            '2024-09-12': ['(B)'],
            '2024-10-31': ['1'],
            '2024-12-06': ['2'],
            '2025-01-10': ['3'],
            '2025-02-18': ['4'],
            '2025-04-08': ['5', '(C)'],
        },
        'tech': {
            '2025-03-13': ['Warn'],
        },
    },
    CVX: {
        'lines': [
        ],
        'elliott': {
        },
    },
    BAC: {
        'lines': [
            ('2024-01-18', '2024-08-05', 10, 10),
            ('2024-07-16', 10, 120, '2024-01-18', '2024-08-05'),

            ('2024-04-16', 80, 400),
            ('2024-11-27', 10, 100),
            ('2024-12-19', 120, 100),
        ],
        'elliott': {
            '2024-01-05': ['(1)'],
            '2024-01-18': ['(2)'],
            '2024-04-16': ['4'],
            '2024-07-16': ['(3)'],
            '2024-08-05': ['(4)'],
            '2024-11-27': ['(5)'],
            '2025-04-04': ['(A)'],
        },
        'tech': {
            '2024-07-16': ['S'],
            '2024-11-27': ['H'],
            '2025-02-06': ['H'],
            '2025-03-06': ['Brk'],
        },
    },
    JNJ: {
        'tech': {
            '2025-03-10': ['Wait', 'Put'],
        },
    },
    MRK: {
        'lines': [
            ('2024-08-06', '2025-02-14', 10, 100),
            ('2024-09-18', 10, 160, '2024-08-06', '2025-02-14'),

            ('2024-11-15', 10, 100),
        ],
        'elliott': {
            '2024-08-06': ['1'],
            '2024-09-18': ['2'],
            '2025-02-14': ['3'],
            '2025-03-17': ['4'],
            '2025-04-10': ['5'],
        },
    },
    DIS: {
        'lines': [
            ('2024-04-02', '2024-11-27', 10, 100),
            ('2023-10-27', '2024-08-13', 10, 200),
        ]
    },
    VISA: {
        'lines': [
            ('2025-01-13', 50, 100),
        ],
        'elliott': {
            '2023-01-27': ['(1)'],
            '2023-03-13': ['(2)'],
            '2024-03-21': ['(3)'],
            '2024-07-25': ['(4)'],
            '2025-01-13': ['4'],
            '2025-02-28': ['(5)'],
            '2025-04-08': ['(A)'],
        },
    },
    TCOM: {
        'lines': [
            ('2024-10-17', 20, 150),
        ],
        'elliott': {
            '2023-01-26': ['(1)'],
            '2023-10-20': ['(2)'],
            '2024-05-20': ['(3)'],
            '2024-08-02': ['(4)'],
            '2024-12-09': ['(5)'],
            '2025-02-28': ['(A)'],
            '2025-03-19': ['(B)'],
        },
        'tech': {
            '2024-10-04': ['S'],
            '2024-11-05': ['S'],
            '2024-12-09': ['H'],
            '2025-01-30': ['H'],
            '2025-03-19': ['S'],
            '2025-04-04': ['RG'],
        },
    },
    HPQ: {
        'lines': [
            ('2024-11-25', '2025-02-20', 10, 100),
            ('2024-12-19', 10, 100, '2024-11-25', '2025-02-20'),

            ('2024-12-19', 100, 100),
        ],
        'elliott': {
            '2024-01-08': ['1'],
            '2024-04-18': ['2'],
            '2024-05-30': ['3'],
            '2024-08-07': ['4'],
            '2024-11-25': ['5'],
            '2024-12-19': ['A'],
            '2025-02-20': ['B'],
            '2025-03-13': ['C'],
        },
        'tech': {
            '2024-08-30': ['S'],
            '2024-11-25': ['H'],
            '2025-02-20': ['S'],
            '2025-02-28': ['Brk'],
            '2025-03-13': ['Warn 26.4'],
        },
    },
    LLY: {
        'lines': [
            ('2024-04-25', 10, 300),
            ('2024-07-15', 10, 200),
        ],
        'elliott': {
            '2023-10-16': ['(1)'],
            '2023-12-20': ['(2)'],
            '2024-03-04': ['(3)'],
            '2024-04-25': ['(4)'],
            '2024-07-15': ['(5)'],
            '2024-11-18': ['(A)'],
            '2025-03-03': ['(B)'],
        },
        'tech': {
            '2024-08-30': ['Top'],
            '2025-03-03': ['Top'],
            '2025-04-04': ['RG'],
        },
    },
    NU: {
        'lines': [
            ('2024-11-11', '2025-02-10', 10, 100),
            ('2024-12-23', 10, 100, '2024-11-11', '2025-02-10'),

            ('2025-02-10', '2025-03-19', 10, 40),

            ('2022-11-08', 40, 140),
            ('2023-09-05', 10, 500),
            ('2024-04-19', 50, 300),
        ],
        'elliott': {
            '2023-02-16': ['(1)'],
            '2023-03-24': ['(2)'],
            '2023-07-13': ['(3)'],
            '2023-09-05': ['(4)'],
            '2023-11-14': ['1'],
            '2024-01-03': ['2'],
            '2024-03-22': ['3'],
            '2024-04-19': ['4'],
            '2024-11-11': ['5', '(5)'],
            '2024-12-23': ['(A)'],
            '2025-02-10': ['(B)'],
        },
        'tech': {
            '2022-10-11': ['S'],
            '2023-01-05': ['H'],
            '2023-03-24': ['S'],
            '2023-05-05': ['Brk'],
            '2024-03-22': ['S'],
            '2024-07-16': ['S'],
            '2024-09-17': ['H'],
            '2024-11-11': ['H'],
            '2025-02-10': ['S'],
            '2025-03-19': ['S'],
            '2025-04-04': ['BG'],
        },
    },
    HOOD: {
        'lines': [
            ('2024-07-16', 10, 200),
            ('2025-03-10', 80, 40),
        ],
        'elliott': {
            '2024-07-16': ['(1)'],
            '2024-05-10': ['4'],
            '2024-08-05': ['(2)'],
            '2024-12-16': ['3'],
            '2024-12-31': ['4'],
            '2025-02-14': ['(3)'],
            '2025-03-10': ['A'],
            '2025-03-24': ['B'],
        },
        'tech': {
            '2024-12-16': ['S'],
            '2025-02-14': ['H'],
            '2025-03-24': ['S'],
            '2025-04-04': ['BG'],
        },
    },
    PYPL: {
        'lines': [
            ('2024-07-25', 200, 200),
            ('2024-04-30', 50, 300),

            ('2024-11-19', 10, 60),
            ('2024-12-16', 10, 40),
        ],
        'elliott': {
        },
        'tech': {
            '2024-04-30': ['S'],
            '2024-12-16': ['H'],
        },
    },
    JD: {
        'lines': [
            ('2024-08-05', '2025-01-10', 10, 100),
            ('2024-10-07', 10, 200, '2024-08-05', '2025-01-10'),
        ],
        'elliott': {
            '2024-05-17': ['(1)'],
            '2024-08-05': ['(2)'],
            '2024-10-07': ['(3)'],
            '2025-01-10': ['(4)'],
            '2025-03-17': ['1'],
            '2025-04-08': ['2'],
        },
    },
    DELL: {
        'lines': [
            ('2024-11-22', '2025-02-19', 10, 100),
            ('2025-02-03', 10, 200, '2024-11-22', '2025-02-19'),

            ('2023-10-26', 5, 400),
            ('2025-02-03', 120, 100),
        ],
        'elliott': {
            '2022-12-01': ['(1)'],
            '2023-03-13': ['(2)'],
            '2023-09-11': ['(3)'],
            '2023-10-26': ['(4)'],
            '2024-05-29': ['(5)'],
            '2024-08-07': ['(A)'],
            '2024-11-22': ['(B)'],
            '2025-04-04': ['(C)'],
        },
        'tech': {
            '2024-08-30': ['S'],
            '2024-11-22': ['H'],
            '2025-02-19': ['S'],
            '2025-03-03': ['Brk'],
        }
    },
    BIDU: {
        'lines': [
            ('2025-01-10', '2025-03-03', 10, 40),

            ('2023-05-03', 10, 500),
            ('2024-12-09', 40, 100),
        ],
        'elliott': {
            '2023-05-03': ['(1)'],
            '2023-07-31': ['(2)'],
            '2024-09-06': ['(3)'],
            '2024-10-02': ['(4)'],
            '2025-01-10': ['(5)'],
            '2025-03-18': ['(1)'],
            '2025-04-08': ['(2)'],
        },
        'tech': {
            '2024-11-22': ['S'],
            '2025-01-10': ['H'],
            '2025-02-14': ['Brk'],
            '2025-03-03': ['S'],
            '2025-03-17': ['Brk'],
            '2025-04-04': ['BG'],
        },
    },
    PINS: {
        'lines': [
            ('2024-11-07', '2024-12-09', 5, 35),
            ('2024-11-15', '2024-12-31', 5, 20),
        ],
        'tech': {
            '2025-01-23': ['Brk'],
        },
    },
    SNOW: {
        'lines': [
            ('2024-10-11', 10, 160),
            ('2024-12-04', 10, 80),
            ('2024-12-31', 30, 70),
        ],
        'tech': {
            '2024-12-04': ['H'],
            '2025-02-18': ['H 3%'],
            '2025-03-10': ['Brk'],
            '2025-03-31': ['Brk'],
        },
    }
}
