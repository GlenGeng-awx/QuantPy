from conf import *

#
# lines
# -----
#   date1, date2, prev_len, post_len
#       or
#   date, prev_len, post_len, date1, date2
#
# sr_levels
# ---------
#   date, prev_len, post_len
#
CORE_BANKING = {
    IXIC: {
        'lines': [
            ('2023-02-02', '2023-07-19', 10, 250),
            ('2023-03-10', 10, 400, '2023-02-02', '2023-07-19'),
            ('2023-10-26', 10, 250, '2023-02-02', '2023-07-19'),

            ('2024-07-10', '2024-08-21', 10, 20),
        ],
        'sr_levels': [
            ('2024-03-22', 10, 100),
        ],
    },
    SS_000300: {
        'lines': [
            ('2023-04-18', '2023-08-04', 10, 250),
            ('2023-06-07', 5, 300, '2023-04-18', '2023-08-04'),
            ('2023-07-24', 5, 300, '2023-04-18', '2023-08-04'),

            ('2023-09-04', '2023-11-06', 5, 70),
            ('2023-08-23', 10, 100, '2023-09-04', '2023-11-06'),

            ('2024-05-20', '2024-07-19', 5, 60),
            ('2024-07-08', 10, 60, '2024-05-20', '2024-07-19'),
        ],
        'sr_levels': [
            ('2023-08-23', 10, 200),
        ],
    },
    SS_000001: {
        'lines': [
            ('2023-08-25', '2023-10-23', 5, 80),
            ('2024-05-20', '2024-07-19', 10, 60),
        ],
    },
    TSLA: {
        'lines': [
            ('2023-08-18', '2023-10-30', 10, 140),
            ('2023-07-18', 10, 250, '2023-08-18', '2023-10-30'),

            ('2024-07-10', '2024-08-21', 10, 20),
            ('2024-04-22', '2024-08-07', 10, 20),
        ],
        'sr_levels': [
            ('2023-02-15', 10, 200),
            ('2023-06-20', 10, 200),
            ('2023-04-26', 10, 200),
        ],
    },
    HK_0700: {
        'lines': [
            ('2023-03-10', '2023-05-31', 10, 180),
            ('2023-04-03', 10, 250, '2023-03-10', '2023-05-31'),
        ],
        'sr_levels': [
            ('2023-04-03', 10, 200),
            ('2023-07-31', 20, 200),
            ('2023-11-23', 30, 150),
        ],
    },
    BILI: {
        'lines': [
            ('2023-06-05', '2023-09-21', 10, 120),
            ('2023-06-15', 5, 150, '2023-06-05', '2023-09-21'),

            ('2023-11-15', '2023-12-29', 10, 30),

            ('2024-03-12', '2024-05-17', 10, 50),
            ('2024-04-19', 10, 80, '2024-03-12', '2024-05-17'),

            ('2024-07-11', '2024-08-05', 5, 30),
        ],
        'sr_levels': [
            ('2024-03-12', 10, 115),
        ],
    },
    PDD: {
        'lines': [
            ('2023-06-15', '2023-09-01', 10, 60),
        ],
        'sr_levels': [
            ('2023-08-01', 5, 200),
            ('2023-10-11', 5, 200),
            ('2024-01-11', 10, 150),
        ],
    },
    IQ: {
        'lines': [
            ('2023-02-28', '2023-07-31', 10, 300),

            ('2024-07-01', '2024-07-24', 10, 60),
            ('2024-07-11', 10, 60, '2024-07-01', '2024-07-24'),
        ],
        'sr_levels': [
            ('2024-02-05', 10, 100),
        ],
    },
    BABA: {
        'lines': [
            ('2023-08-18', '2023-09-21', 10, 45),
            ('2023-09-01', 5, 80, '2023-08-18', '2023-09-21'),

            ('2024-06-28', '2024-07-25', 5, 40),
            ('2024-07-12', 5, 40, '2024-06-28', '2024-07-25'),
        ],
        'sr_levels': [
            ('2023-12-29', 10, 150)
        ],
    },
    BA: {
        'lines': [
            ('2024-05-29', '2024-06-18', 10, 40),
        ],
        'sr_levels': [
            ('2024-03-28', 10, 100)
        ],
    },
    COIN: {
        'sr_levels': [
            ('2024-03-08', 10, 120),
            ('2024-02-16', 10, 130),
            ('2024-02-05', 10, 140),
        ],
    },
    PLTR: {
        'lines': [
            ('2023-08-01', '2024-03-07', 10, 160),
            ('2023-10-30', 10, 260, '2023-08-01', '2024-03-07'),
        ],
    },
    SNOW: {
        'lines': [
            ('2023-02-02', '2023-06-15', 10, 200),

            ('2023-07-18', '2023-09-11', 10, 50),
            ('2023-10-26', '2024-01-18', 10, 20),
            ('2023-12-14', 10, 45, '2023-10-26', '2024-01-18'),

            ('2024-05-16', '2024-07-05', 10, 60),
        ],
    },
    FUTU: {
        'lines': [
            ('2023-02-01', '2023-09-06', 10, 200),
            ('2023-05-31', 10, 310, '2023-02-01', '2023-09-06'),
        ],
    },
    NVDA: {
        'lines': [
            ('2024-03-07', '2024-06-18', 10, 10),
            ('2024-04-19', 10, 120, '2024-03-07', '2024-06-18'),

            ('2024-07-10', '2024-08-19', 5, 40),
        ],
    },
    BEKE: {
        'lines': [
            ('2023-02-13', '2023-03-03', 5, 100),
            ('2023-03-09', 5, 80, '2023-02-13', '2023-03-03'),
            ('2023-06-08', '2023-07-28', 5, 35),

            ('2023-09-01', '2023-12-28', 10, 100),
            ('2023-10-19', 5, 100, '2023-09-01', '2023-12-28'),

            ('2024-07-03', '2024-08-19', 5, 40),
        ],
    },
    RIVN: {
        'lines': [
            ('2023-07-31', '2023-12-19', 10, 150),
            ('2023-09-29', 10, 220, '2023-07-31', '2023-12-19'),
        ],
    },
    MRNA: {
        'lines': [
            ('2023-03-01', '2023-08-15', 10, 80),
            ('2023-03-20', 10, 220, '2023-03-01', '2023-08-15'),
            ('2023-04-13', 10, 220, '2023-03-01', '2023-08-15'),

            ('2024-02-13', '2024-04-19', 10, 10),
            ('2024-01-08', 5, 120, '2024-02-13', '2024-04-19'),
        ],
    },
    MNSO: {
        'lines': [
            ('2023-11-20', '2024-01-16', 10, 50),

            ('2024-02-22', '2024-03-21', 10, 45),
            ('2024-03-07', 5, 70, '2024-02-22', '2024-03-21'),

            ('2024-05-30', '2024-07-12', 10, 40),
            ('2024-05-22', 5, 60, '2024-05-30', '2024-07-12'),
        ],
    },
    EDU: {
        'lines': [
            ('2023-08-04', '2023-12-01', 10, 10),
            ('2023-09-01', 10, 140, '2023-08-04', '2023-12-01'),
            ('2023-09-21', 10, 140, '2023-08-04', '2023-12-01'),
            ('2024-05-14', '2024-07-03', 10, 10),
            ('2024-04-24', 10, 120, '2024-05-14', '2024-07-03'),
        ],
    },
    BNTX: {
        'lines': [
            ('2023-08-30', '2024-01-02', 200, 200),
        ],
    },
    XPEV: {
        'lines': [
            ('2023-02-01', '2023-03-30', 10, 100),
            ('2023-03-14', 5, 100, '2023-02-01', '2023-03-30'),

            ('2023-08-29', '2023-09-29', 10, 80),
            ('2023-08-18', 10, 110, '2023-08-29', '2023-09-29'),

            ('2024-03-12', '2024-05-02', 10, 100),
            ('2024-05-10', 5, 100, '2024-03-12', '2024-05-02'),
        ],
    }
}