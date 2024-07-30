from conf import *

#
# wave2_forcast:    (from, 1)
# wave2_recon:      (from, 1, 2)
# wave3_forcast:    (from, 1, 2)
# wave3_recon:      (from, 1, 2, 3)
#
RATIO_RECORDS = {
    IXIC: {
        "wave2_forcast": [
            (12595, 18647),
            (15282, 18647),
        ],
        "wave3_forcast": [
            (18647, 17342, 17862),
        ],
        "wave2_recon": [
            (11138, 14358, 12595),
            (14510, 16442, 15282),
            (15282, 18647, 16442),
        ],
    },
    # SS_000001,
    SS_000300: {
        "wave3_forcast": [
            (3179, 3603, 3401),
        ],
        "wave3_recon": [
            (3603, 3475, 3690, 3401),
        ],
    },
    BABA: {
        "wave3_forcast": [
            (67.35, 86.65, 72),
            (72, 79.65, 75.27),
        ],
        "wave2_recon": [
            (67.35, 86.65, 72),
        ],
        "wave3_recon": [
            (66.6, 76.56, 67.35, 86.65),
        ],
    },
    # XPEV,
    # TSLA,
    MRNA: {
        "wave2_forcast": [
            (85.95, 166.61),
        ],
        "wave2_recon": [
            (85.95, 166.61, 115.95),
        ],
        "wave3_recon": [
            (69.51, 115.44, 85.37, 166.61),
        ],
    },
    CPNG: {
        "wave2_forcast": [
            (13.84, 23.65),
            (17.57, 23.65),
        ],
        "wave3_recon": [
            (13.84, 19.62, 17.57, 23.65),
        ],
    },
    COIN: {
        "wave2_forcast": [
            (70.8, 279.71),
            (117.3, 279.71),
        ],
    },
    # SNOW,
    # IQ,
    # JD,
    # BEKE,
    # RIVN,
    # META,
    # MNSO,
    # ZM,
    # BABA,
    # BA,
    # BILI,
    # PDD,
    HK_0700: {
        "wave2_forcast": [
        ],
        "wave3_forcast": [
            (187.74, 408.53, 267.68),
        ],
        "wave2_recon": [
            (187.74, 408.53, 267.68)
        ],
        "wave3_recon": [
        ],
    },
    # FUTU,
}
