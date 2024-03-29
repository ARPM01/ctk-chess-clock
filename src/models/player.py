from datetime import timedelta

import customtkinter as ctk

from .color import Color
from .side import Side


class Player:
    def __init__(
        self,
        color: Color,
        side: Side,
        time_left: timedelta,
        increment: timedelta,
    ):
        self.color = color
        self.side = side
        self.time_left = time_left
        self.increment = increment
        self.moves_made = 0
        self.turn_ended = False
