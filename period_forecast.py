from period_conf import *
from period_display import *

# (from_date, direction, length, pst)
forcast_period = {
    IXIC: [
        ('2024-04-19', 'up', 80, 20),
    ],
    MRNA: [
        ('2024-05-24', 'down', 15, 22),
    ],
    PDD: [
        ('2024-05-24', 'down', 15, 23),
    ],
    TSLA: [
        ('2024-04-29', 'down', 40, 34),
    ],
    BABA: [
        ('2024-05-31', 'up', 20, 33),
    ],
    HK_0700: [
        ('2024-05-17', 'down', 40, 21),
    ],
    JD: [
        ('2024-05-29', 'up', 25, 44),
    ],
    BEKE: [
        ('2024-05-17', 'down', 30, 30),
    ],
    PLTR: [
        ('2024-04-19', 'up', 50, 35)
    ]
}


class PeriodForecast:
    def __init__(self, period_display: PeriodDisplay):
        self.stock_name = period_display.stock_name
        self.stock_df = period_display.stock_df
        self.period_display = period_display

    # (_from_idx, from_date, from_low, _to_idx, to_date, to_high, length, delta, pst, mid)
    def build_up_box(self, from_date, length, pst):
        condition = self.stock_df['Date'].apply(lambda x: shrink_date_str(x) == from_date)
        if not condition.any():
            return ()

        from_low = self.stock_df[condition]['low'].values[0]

        to_date = calculate_next_n_workday(from_date, length)
        to_high = from_low * (1 + pst / 100)

        delta = to_high - from_low
        mid = (from_low + to_high) / 2

        return None, from_date, from_low, None, to_date, to_high, length, delta, pst, mid

    # (_from_idx, from_date, from_high, _to_idx, to_date, to_low, length, delta, pst, mid)
    def build_down_box(self, from_date, length, pst):
        condition = self.stock_df['Date'].apply(lambda x: shrink_date_str(x) == from_date)
        if not condition.any():
            return ()

        from_high = self.stock_df[condition]['high'].values[0]

        to_date = calculate_next_n_workday(from_date, length)
        to_low = from_high * (1 - pst / 100)

        delta = from_high - to_low
        mid = (from_high + to_low) / 2

        return None, from_date, from_high, None, to_date, to_low, length, delta, pst, mid

    def forecast(self):
        if self.stock_name not in forcast_period:
            return

        for (from_date, direction, length, pst) in forcast_period[self.stock_name]:
            print(f'forecast {self.stock_name} {direction} {length} days from {from_date} with {pst}%')

            if direction == 'up':
                box = self.build_up_box(from_date, length, pst)
                if len(box) == 0:
                    continue
                print('up box ->', box)
                self.period_display.add_up_box(*box, forcast=True)
            else:
                box = self.build_down_box(from_date, length, pst)
                if len(box) == 0:
                    continue
                print('down box ->', box)
                self.period_display.add_down_box(*box, forcast=True)
