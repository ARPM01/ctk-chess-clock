from datetime import timedelta

import customtkinter as ctk

from src.models import Player, Constant, Color, Side
from src.utils import timedelta_to_str


class PlayerButton(ctk.CTkButton):
    def __init__(self, master, player: Player, **kwargs):
        super().__init__(master, text=player.time_left, **kwargs)

        self.master = master
        self.player = player

        self.__ms_counter = 0

        if player.color == Color.WHITE:
            self.configure(
                fg_color=Constant.WHITE,
                hover_color=Constant.WHITE_HOVER,
                text_color=Constant.BLACK,
            )
        elif player.color == Color.BLACK:
            self.configure(
                fg_color=Constant.BLACK,
                hover_color=Constant.BLACK_HOVER,
                text_color=Constant.WHITE,
            ),

    def enable(self):
        self.configure(state=ctk.NORMAL)
        self.player.turn_ended = False

    def disable(self):
        self.configure(state=ctk.DISABLED)
        self.player.turn_ended = True

    def slide_left(self, x=0.75):
        if x < 0.25:
            return

        if self.player.side == Side.LEFT:
            self.place(relx=0, relwidth=x)
        elif self.player.side == Side.RIGHT:
            self.place(relx=x, relwidth=0.25 + (0.75 - x))

        self.after(2, self.slide_left, x - 0.01)

    def slide_right(self, x=0.25):
        if x > 0.75:
            return

        if self.player.side == Side.LEFT:
            self.place(relx=0, relwidth=x)
        elif self.player.side == Side.RIGHT:
            self.place(relx=x, relwidth=0.25 + (0.75 - x))

        self.after(2, self.slide_right, x + 0.01)

    def count_down(self):
        def update_time_left():
            if self.player.turn_ended:
                return

            if self.__ms_counter != 0 and self.__ms_counter % 1000 == 0:
                self.player.time_left = self.player.time_left - timedelta(seconds=1)
                self.configure(text=timedelta_to_str(self.player.time_left))

            if self.player.time_left > timedelta(seconds=0):
                self.__ms_counter += 1
                self.after(1, update_time_left)

            # TODO: Implement else here -- when a player has run out of time. Add sfc for end game.

        self.after(1, update_time_left)

    def set_time_left(self, time_left: timedelta):
        self.player.time_left = time_left
        self.configure(text=timedelta_to_str(time_left))

    def increment_time(self):
        self.player.time_left += self.player.increment
        self.configure(text=timedelta_to_str(self.player.time_left))
