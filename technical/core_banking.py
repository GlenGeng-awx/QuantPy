from conf import *

#
# lines
# -----
#   date1, date2, prev_len, post_len
#       or
#   date, prev_len, post_len, date1, date2
#
CORE_BANKING = {
    IXIC: {
        'lines': [
            ('2023-02-02', '2023-07-19', 10, 250),
            ('2023-03-10', 10, 500, '2023-02-02', '2023-07-19'),
            ('2023-10-26', 10, 250, '2023-02-02', '2023-07-19'),

            ('2023-07-31', '2023-08-31', 10, 60),
            ('2023-08-18', 10, 60, '2023-07-31', '2023-08-31'),

            ('2024-07-10', '2024-08-21', 10, 60),
        ],
    },
    SS_000300: {
        'lines': [
            ('2023-04-18', '2023-08-04', 10, 400),
            ('2023-06-16', 10, 330, '2023-04-18', '2023-08-04'),
            ('2023-06-07', 10, 330, '2023-04-18', '2023-08-04'),
            ('2023-07-24', 10, 300, '2023-04-18', '2023-08-04'),

            ('2023-09-04', '2023-11-06', 5, 70),
        ],
    },
    SS_000001: {
        'lines': [
            ('2023-06-26', '2023-10-23', 50, 80),
            ('2023-05-08', 10, 200, '2023-06-26', '2023-10-23'),

            ('2024-02-28', '2024-03-27', 5, 50),
            ('2024-03-18', 5, 50, '2024-02-28', '2024-03-27'),

            ('2024-05-20', '2024-07-19', 10, 60),
            ('2024-07-08', 10, 60, '2024-05-20', '2024-07-19'),
        ],
    },
    TSLA: {
        'lines': [
            ('2023-08-18', '2023-10-30', 10, 200),
            ('2023-06-20', 10, 350, '2023-08-18', '2023-10-30'),
            ('2023-07-18', 10, 400, '2023-08-18', '2023-10-30'),

            ('2024-04-22', '2024-08-07', 10, 100),
            ('2024-04-29', 10, 200, '2024-04-22', '2024-08-07'),
        ],
    },
    HK_0700: {
        'lines': [
            ('2023-03-10', '2023-05-31', 10, 180),
            ('2023-04-03', 10, 250, '2023-03-10', '2023-05-31'),
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
    },
    PDD: {
        'lines': [
            ('2023-06-15', '2023-09-01', 10, 60),
            ('2023-05-26', 10, 180, '2023-06-15', '2023-09-01'),

            ('2024-01-11', '2024-02-15', 10, 40),
            ('2024-10-04', 5, 60, '2024-01-11', '2024-02-15'),

            ('2024-01-11', '2024-03-20', 10, 120),
            ('2024-10-04', 5, 60, '2024-01-11', '2024-03-20'),
        ],
    },
    IQ: {
        'lines': [
            ('2023-02-28', '2023-07-31', 10, 360),
            ('2023-03-17', 10, 400, '2023-02-28', '2023-07-31'),
            ('2023-05-10', 10, 200, '2023-02-28', '2023-07-31'),
            ('2024-05-06', 10, 200, '2023-02-28', '2023-07-31'),

            ('2024-07-01', '2024-07-24', 10, 50),
            ('2024-07-11', 10, 100, '2024-07-01', '2024-07-24'),
            ('2024-05-16', 10, 200, '2024-07-01', '2024-07-24'),
        ],
    },
    BABA: {
        'lines': [
            ('2023-08-18', '2023-09-21', 10, 45),
            ('2023-09-01', 5, 80, '2023-08-18', '2023-09-21'),

            ('2024-06-28', '2024-07-25', 5, 40),
            ('2024-07-12', 5, 100, '2024-06-28', '2024-07-25'),
        ],
    },
    BA: {
        'lines': [
            ('2023-08-30', '2023-10-11', 10, 15),
            ('2023-12-15', 5, 100, '2023-08-30', '2023-10-11'),
            ('2024-07-31', 10, 50, '2023-08-30', '2023-10-11'),

            ('2023-08-10', '2024-02-07', 10, 200),
            ('2023-07-11', 10, 400, '2023-08-10', '2024-02-07'),
            ('2023-07-19', 10, 400, '2023-08-10', '2024-02-07'),
        ],
    },
    COIN: {
        'lines': [
            ('2024-03-25', '2024-06-06', 10, 100),
            ('2024-04-05', 5, 200, '2024-03-25', '2024-06-06'),
            ('2024-04-19', 5, 200, '2024-03-25', '2024-06-06'),
            ('2024-04-30', 5, 200, '2024-03-25', '2024-06-06'),
        ],
    },
    PLTR: {
        'lines': [
            ('2023-06-15', '2023-07-18', 10, 400),
            ('2023-11-20', 10, 250, '2023-06-15', '2023-07-18'),
            ('2024-05-23', 10, 200, '2023-06-15', '2023-07-18'),
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
            ('2023-02-01', '2023-09-06', 10, 400),
            ('2024-05-17', 10, 150, '2023-02-01', '2023-09-06'),
            ('2023-06-26', 10, 350, '2023-02-01', '2023-09-06'),
            ('2024-03-26', 10, 200, '2023-02-01', '2023-09-06'),
        ],
    },
    NVDA: {
        'lines': [

        ],
    },
    BEKE: {
        'lines': [
            ('2023-02-13', '2023-03-03', 5, 100),
            ('2023-03-09', 5, 80, '2023-02-13', '2023-03-03'),
            ('2023-06-08', '2023-07-28', 5, 35),

            ('2023-09-01', '2023-12-28', 10, 100),
            ('2023-10-19', 5, 100, '2023-09-01', '2023-12-28'),
            ('2023-10-11', 5, 140, '2023-09-01', '2023-12-28'),


            ('2024-07-03', '2024-08-19', 5, 40),
            ('2024-06-28', 5, 100, '2024-07-03', '2024-08-19'),
            ('2024-08-07', 5, 100, '2024-07-03', '2024-08-19'),
        ],
    },
    RIVN: {
        'lines': [
            ('2023-07-31', '2023-12-19', 10, 300),
            ('2023-09-29', 10, 300, '2023-07-31', '2023-12-19'),
            ('2023-08-21', 10, 300, '2023-07-31', '2023-12-19'),
            ('2023-08-24', 10, 300, '2023-07-31', '2023-12-19'),
            ('2024-01-25', 10, 300, '2023-07-31', '2023-12-19'),
            ('2023-11-09', 10, 300, '2023-07-31', '2023-12-19'),
        ],
    },
    MRNA: {
        'lines': [
            ('2023-03-01', '2023-08-15', 10, 80),
            ('2023-03-20', 10, 220, '2023-03-01', '2023-08-15'),
            ('2023-04-13', 10, 220, '2023-03-01', '2023-08-15'),
            ('2024-01-08', 10, 260, '2023-03-01', '2023-08-15'),

            ('2024-02-13', '2024-04-19', 10, 10),
            ('2024-01-08', 5, 120, '2024-02-13', '2024-04-19'),

            ('2024-08-19', '2024-09-11', 5, 60),
            ('2024-08-07', 5, 80, '2024-08-19', '2024-09-11'),
            ('2024-09-04', 5, 80, '2024-08-19', '2024-09-11'),
        ],
    },
    MNSO: {
        'lines': [
            ('2023-09-14', '2024-05-13', 10, 160),
            ('2023-08-11', 10, 240, '2023-09-14', '2024-05-13'),
            ('2023-10-05', 10, 300, '2023-09-14', '2024-05-13'),
            ('2023-12-14', 10, 240, '2023-09-14', '2024-05-13'),

            ('2023-11-20', '2024-01-16', 10, 50),
            ('2024-05-30', 10, 70, '2023-11-20', '2024-01-16'),
            ('2024-05-22', 5, 60, '2023-11-20', '2024-01-16'),
            ('2024-10-04', 5, 60, '2023-11-20', '2024-01-16'),

            ('2024-02-22', '2024-03-21', 10, 45),
            ('2024-03-07', 5, 70, '2024-02-22', '2024-03-21'),
            ('2024-09-24', 5, 70, '2024-02-22', '2024-03-21'),
            ('2024-09-03', 5, 90, '2024-02-22', '2024-03-21'),
        ],
    },
    EDU: {
        'lines': [
            ('2023-08-04', '2023-12-01', 10, 10),
            ('2023-09-01', 10, 140, '2023-08-04', '2023-12-01'),
            ('2023-09-21', 10, 140, '2023-08-04', '2023-12-01'),

            ('2024-05-14', '2024-07-03', 10, 120),
            ('2024-04-24', 10, 200, '2024-05-14', '2024-07-03'),
        ],
    },
    BNTX: {
        'lines': [
            ('2023-08-30', '2024-01-02', 200, 200),
            ('2023-03-01', 10, 350, '2023-08-30', '2024-01-02'),
            ('2023-04-14', 10, 350, '2023-08-30', '2024-01-02'),
        ],
    },
    XPEV: {
        'lines': [
            ('2023-02-01', '2023-03-30', 10, 100),
            ('2023-03-14', 5, 100, '2023-02-01', '2023-03-30'),

            ('2023-08-29', '2023-09-29', 10, 300),
            ('2023-07-28', 10, 400, '2023-08-29', '2023-09-29'),
            ('2023-08-18', 10, 110, '2023-08-29', '2023-09-29'),
            ('2023-11-24', 10, 300, '2023-08-29', '2023-09-29'),

            ('2024-05-02', '2024-07-22', 10, 40),
            ('2024-04-19', 10, 100, '2024-05-02', '2024-07-22'),
        ],
    },
    EBAY: {
        'lines': [
            ('2024-05-06', '2024-07-25', 10, 10),
            ('2024-03-13', 10, 150, '2024-05-06', '2024-07-25'),
            ('2024-04-10', 10, 150, '2024-05-06', '2024-07-25'),
            ('2023-07-19', 10, 300, '2024-05-06', '2024-07-25'),

            ('2024-08-16', '2024-08-28', 5, 10),
            ('2024-08-22', 5, 20, '2024-08-16', '2024-08-28'),
        ],
    },
    META: {
        'lines': [
            ('2023-04-25', '2023-07-24', 10, 300),
            ('2023-05-01', 10, 100, '2023-04-25', '2023-07-24'),
            ('2023-10-26', 10, 300, '2023-04-25', '2023-07-24'),
            ('2024-04-30', 10, 200, '2023-04-25', '2023-07-24'),
            ('2024-07-25', 10, 100, '2023-04-25', '2023-07-24'),
        ],
    },
    LI: {
        'lines': [
            ('2023-10-20', '2024-01-22', 10, 200),
            ('2023-08-07', 5, 400, '2023-10-20', '2024-01-22'),
            ('2023-08-29', 5, 400, '2023-10-20', '2024-01-22'),
            ('2023-09-08', 5, 400, '2023-10-20', '2024-01-22'),
            ('2024-02-27', 5, 400, '2023-10-20', '2024-01-22'),
            ('2024-03-12', 5, 400, '2023-10-20', '2024-01-22'),
        ],
    },
    ZM: {
        'lines': [
            ('2023-02-07', '2023-03-31', 5, 45),
            ('2023-09-06', 5, 50, '2023-02-07', '2023-03-31'),
            ('2023-12-26', 5, 50, '2023-02-07', '2023-03-31'),
            ('2024-03-01', 5, 40, '2023-02-07', '2023-03-31'),
            ('2024-08-27', 5, 40, '2023-02-07', '2023-03-31'),

            ('2024-03-01', '2024-05-22', 5, 70),
            ('2024-08-27', 5, 40, '2024-03-01', '2024-05-22'),
        ],
    },
    TSM: {
        'lines': [
            ('2023-10-27', '2024-01-04', 10, 200),
            ('2023-11-20', 10, 250, '2023-10-27', '2024-01-04'),
            ('2024-02-08', 10, 200, '2023-10-27', '2024-01-04'),
            ('2024-03-07', 10, 180, '2023-10-27', '2024-01-04'),
            ('2024-06-18', 10, 150, '2023-10-27', '2024-01-04'),
        ],
    },
    AMD: {
        'lines': [
            ('2024-03-07', '2024-07-10', 10, 100),
            ('2024-02-21', 10, 200, '2024-03-07', '2024-07-10'),
            ('2024-02-22', 10, 200, '2024-03-07', '2024-07-10'),
            ('2024-04-19', 10, 200, '2024-03-07', '2024-07-10'),
            ('2024-05-28', 10, 200, '2024-03-07', '2024-07-10'),
            ('2023-06-12', 10, 110, '2024-03-07', '2024-07-10'),

            ('2023-02-02', '2023-03-23', 10, 80),
            ('2024-07-31', 10, 80, '2023-02-02', '2023-03-23'),
            ('2024-08-21', 10, 80, '2023-02-02', '2023-03-23'),
            ('2024-08-07', 10, 80, '2023-02-02', '2023-03-23'),
        ],
    },
    PFE: {
        'lines': [
            ('2024-05-22', '2024-07-30', 10, 60),
            ('2024-04-18', 5, 150, '2024-05-22', '2024-07-30'),

      ],
    },
    NIO: {
        'lines': [
            ('2023-01-27', '2023-07-12', 10, 400),
            ('2023-03-31', 10, 400, '2023-01-27', '2023-07-12'),
            ('2023-05-22', 10, 400, '2023-01-27', '2023-07-12'),
            ('2023-05-02', 10, 250, '2023-01-27', '2023-07-12'),

            ('2024-04-19', '2024-08-07', 10, 180),
            ('2024-05-14', 10, 150, '2024-04-19', '2024-08-07'),
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
    PINS: {
        'lines': [
            ('2023-05-04', '2023-10-26', 10, 300),
            ('2023-07-18', 10, 400, '2023-05-04', '2023-10-26'),
            ('2023-10-10', 10, 350, '2023-05-04', '2023-10-26'),
            ('2024-02-06', 10, 200, '2023-05-04', '2023-10-26'),
        ],
    },
    SHOP: {
        'lines': [
            ('2023-03-01', '2023-10-27', 10, 300),
            ('2023-02-02', 10, 500, '2023-03-01', '2023-10-27'),
            ('2023-05-03', 10, 400, '2023-03-01', '2023-10-27'),
            ('2023-05-08', 10, 400, '2023-03-01', '2023-10-27'),
            ('2023-07-13', 10, 400, '2023-03-01', '2023-10-27'),
        ],
    },
    ETSY: {
        'lines': [
            ('2024-01-31', '2024-05-02', 5, 200),
            ('2024-02-02', 5, 200, '2024-01-31', '2024-05-02'),
            ('2024-02-12', 5, 200, '2024-01-31', '2024-05-02'),
        ],
    },
    QCOM: {
        'lines': [
            ('2023-11-20', '2023-12-28', 10, 120),
            ('2024-06-18', '2024-07-16', 10, 60),
        ],
    },
    MS: {
        'lines': [
            ('2024-01-02', '2024-05-21', 5, 100),
            ('2024-04-12', 5, 160, '2024-01-02', '2024-05-21'),
            ('2024-02-13', 5, 160, '2024-01-02', '2024-05-21'),
        ],
    },
    CPNG: {
        'lines': [
            ('2023-09-01', '2023-10-24', 10, 90),
            ('2023-11-01', 10, 70, '2023-09-01', '2023-10-24'),

            ('2024-02-05', '2024-07-25', 5, 60),
            ('2024-08-19', 120, 60, '2024-02-05', '2024-07-25'),
            ('2024-03-22', 10, 200, '2024-02-05', '2024-07-25'),
            ('2024-03-13', 10, 200, '2024-02-05', '2024-07-25'),
        ],
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
            ('2023-05-04', '2023-06-21', 5, 30),
            ('2023-05-26', 10, 50, '2023-05-04', '2023-06-21'),
            ('2024-08-07', 5, 100, '2023-05-04', '2023-06-21'),
            ('2024-09-09', 5, 100, '2023-05-04', '2023-06-21'),
        ],
    },
}
