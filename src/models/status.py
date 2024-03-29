from enum import Enum, auto


class Status(Enum):
    PAUSED = auto()
    PLAYING = auto()
    ENDED = auto()
