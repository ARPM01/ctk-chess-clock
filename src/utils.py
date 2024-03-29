from datetime import timedelta

from src.models import TimeControl


def timedelta_to_str(timedelta: timedelta):
    time_str = ""

    total_seconds = int(timedelta.total_seconds())
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    if hours != 0:
        time_str += f"{hours}:"
    if minutes != 0:
        time_str += f"{minutes:02}:"

    return time_str + f"{seconds:02}"
