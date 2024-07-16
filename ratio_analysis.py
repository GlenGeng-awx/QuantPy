
ratio_382 = 0.382
ratio_500 = 0.500
ratio_618 = 0.618
ratio_786 = 0.786

ratio_1000 = 1.000
ratio_1618 = 1.618
ratio_2618 = 2.618


def wave_retrace(wave_from, wave_to):
    if wave_from < wave_to:
        net = wave_to - wave_from

        down_382 = wave_to - net * ratio_382
        down_500 = wave_to - net * ratio_500
        down_618 = wave_to - net * ratio_618
        down_786 = wave_to - net * ratio_786

        print(f"wave_retrace: from={wave_from}, to={wave_to}, net={net:.2f}\n" +
              f"\tdown_382={down_382:.2f}\n" +
              f"\tdown_500={down_500:.2f}\n" +
              f"\tdown_618={down_618:.2f}\n" +
              f"\tdown_786={down_786:.2f}\n")
    else:  # wave_from > wave_to
        net = wave_from - wave_to

        up_382 = wave_to + net * ratio_382
        up_500 = wave_to + net * ratio_500
        up_618 = wave_to + net * ratio_618
        up_786 = wave_to + net * ratio_786

        print(f"wave_retrace: from={wave_from}, to={wave_to}, net={net:.2f}\n" +
              f"\tup_382={up_382:.2f}\n" +
              f"\tup_500={up_500:.2f}\n" +
              f"\tup_618={up_618:.2f}\n" +
              f"\tup_786={up_786:.2f}\n")


def zigzag_retrace(zigzag_from, zigzag_a, zigzag_b):
    if zigzag_from > zigzag_a:
        net = zigzag_from - zigzag_a

        down_1000 = zigzag_b - net * ratio_1000
        down_1618 = zigzag_b - net * ratio_1618
        down_2618 = zigzag_b - net * ratio_2618

        print(f"zigzag_retrace: from={zigzag_from}, a={zigzag_a}, b={zigzag_b}, net={net:.2f}\n" +
              f"\tdown_1000={down_1000:.2f}\n" +
              f"\tdown_1618={down_1618:.2f}\n" +
              f"\tdown_2618={down_2618:.2f}\n")
    else:  # zigzag_from < zigzag_a
        net = zigzag_a - zigzag_from

        up_1000 = zigzag_b + net * ratio_1000
        up_1618 = zigzag_b + net * ratio_1618
        up_2618 = zigzag_b + net * ratio_2618

        print(f"zigzag_retrace: from={zigzag_from}, a={zigzag_a}, b={zigzag_b}, net={net:.2f}\n" +
              f"\tup_1000={up_1000:.2f}\n" +
              f"\tup_1618={up_1618:.2f}\n" +
              f"\tup_2618={up_2618:.2f}\n")


wave_retrace(266, 395)
zigzag_retrace(359.8, 381.6, 370.8)
