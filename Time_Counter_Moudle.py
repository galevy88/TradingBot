from tradingview_ta import Interval


def get_time_counter(TIME_INTERVAL):
    if TIME_INTERVAL == Interval.INTERVAL_1_MINUTE:
        return 60
    if TIME_INTERVAL == Interval.INTERVAL_5_MINUTES:
        return 300
    if TIME_INTERVAL == Interval.INTERVAL_15_MINUTES:
        return 900
    if TIME_INTERVAL == Interval.INTERVAL_30_MINUTES:
        return 1800
    if TIME_INTERVAL == Interval.INTERVAL_1_HOUR:
        return 3660
    if TIME_INTERVAL == Interval.INTERVAL_2_HOURS:
        return 7200
    if TIME_INTERVAL == Interval.INTERVAL_4_HOURS:
        return 14400
    if TIME_INTERVAL == Interval.INTERVAL_1_DAY:
        return 86400
    if TIME_INTERVAL == Interval.INTERVAL_1_WEEK:
        return 604800
    if TIME_INTERVAL == Interval.INTERVAL_1_MONTH:
        return 24190200