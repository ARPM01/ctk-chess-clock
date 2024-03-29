from datetime import timedelta
from enum import Enum


class TimeControl(Enum):
    CLASSICAL = timedelta(minutes=90), timedelta(seconds=30)
    RAPID = timedelta(minutes=25), timedelta(seconds=10)
    BLITZ = timedelta(minutes=5), timedelta(seconds=3)
    BULLET = timedelta(minutes=2), timedelta(seconds=1)

    def __init__(self, duration: timedelta, increment: timedelta):
        self.duration = duration
        self.increment = increment
