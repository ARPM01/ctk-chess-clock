import customtkinter as ctk
import sounddevice as sd
import soundfile as sf

import platform

from src.models import TimeControl, Player, Constant, Status
from src.views.components import (
    PlayerButton,
    PauseButton,
    TimeControlButton,
    ResetButton,
    PlayerButtonFrame,
)
from src.views.time_control_picker import TimeControlPicker


class Clock(ctk.CTk):
    def __init__(self, player_left: Player, player_right: Player):
        super().__init__()

        ctk.set_appearance_mode("dark")

        if platform.system() == "Windows":
            self.iconbitmap(Constant.PATH_ICON)

        WIDTH, HEIGHT = 600, 400
        self.geometry(f"{WIDTH}x{HEIGHT}")
        self.title(Constant.APP_TITLE)

        self.player_left = player_left
        self.player_right = player_right
        self.status = Status.PAUSED

        self.default_time_control = ctk.StringVar(
            self, TimeControl.CLASSICAL.name.capitalize()
        )
        self.time_control = self.default_time_control

        self.time_control.trace_add("write", self.change_time_control)

        self.time_control_picker = None
        self.current_turn = self.player_left

        self.game_buttons_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.game_buttons_frame.pack(side=ctk.TOP, anchor=ctk.CENTER, pady=10)

        self.time_control_button = TimeControlButton(
            self.game_buttons_frame,
            command=self.show_time_control_picker,
        )
        self.pause_button = PauseButton(self.game_buttons_frame, command=self.start)
        self.reset_button = ResetButton(self.game_buttons_frame, command=None)

        self.time_control_button.grid(row=0, column=0, padx=5)
        self.pause_button.grid(row=0, column=1, padx=5)
        self.reset_button.grid(row=0, column=2, padx=5)

        self.player_button_frame = PlayerButtonFrame(
            self, self.player_left, self.player_right
        )
        self.player_button_frame.pack(
            side=ctk.BOTTOM,
            fill=ctk.BOTH,
            expand=True,
        )

        self.player_left_button = PlayerButton(
            self.player_button_frame,
            self.player_left,
            command=self.end_player_left_turn,
        )
        self.player_right_button = PlayerButton(
            self.player_button_frame,
            self.player_right,
            command=self.end_player_right_turn,
        )
        self.player_left_button.place(
            relx=0,
            rely=0.05,
            relheight=0.85,
            relwidth=0.75,
        )
        self.player_right_button.place(
            relx=0.75,
            rely=0.05,
            relheight=0.85,
            relwidth=0.3,
        )

        self.end_turn_data, self.end_turn_fs = sf.read(Constant.PATH_TURN_END_SFX)

    def run(self):
        self.show_time_control_picker()
        self.player_left_button.disable()
        self.player_right_button.disable()

        self.mainloop()

    def show_time_control_picker(self, *args):
        if (
            self.time_control_picker is None
            or not self.time_control_picker.winfo_exists()
        ):
            self.time_control_picker = TimeControlPicker(self)
        else:
            self.time_control_picker.focus()

    def end_player_left_turn(self):
        # TODO: Bind to left click and CAPS LOCK using button click event

        sd.play(self.end_turn_data, self.end_turn_fs)

        self.player_left.moves_made += 1
        self.player_button_frame.update_moves_made()

        self.player_left_button.increment_time()
        self.player_left_button.disable()

        self.player_right_button.enable()
        self.player_right_button.count_down()

        self.current_turn = self.player_right

        self.toggle_anim(end_turn=self.player_left)

    def end_player_right_turn(self):
        # TODO: bind to right click and return

        sd.play(self.end_turn_data, self.end_turn_fs)

        self.player_right.moves_made += 1
        self.player_button_frame.update_moves_made()

        self.player_right_button.increment_time()
        self.player_right_button.disable()

        self.player_left_button.enable()
        self.player_left_button.count_down()

        self.current_turn = self.player_right

        self.toggle_anim(end_turn=self.player_right)

    def toggle_anim(self, end_turn: Player):
        if end_turn == self.player_left:
            self.player_left_button.slide_left()
            self.player_right_button.slide_left()

        elif end_turn == self.player_right:
            self.player_left_button.slide_right()
            self.player_right_button.slide_right()

    def change_time_control(self, *args):
        self.__change_duration()
        self.__change_increment()

    def __change_duration(self):
        time_control_enum = TimeControl[self.time_control.get().upper()]
        self.player_left_button.set_time_left(time_control_enum.duration)
        self.player_right_button.set_time_left(time_control_enum.duration)

    def __change_increment(self):
        time_control_enum = TimeControl[self.time_control.get().upper()]
        self.player_left.increment = time_control_enum.increment
        self.player_right.increment = time_control_enum.increment

    def start(self):
        self.status = Status.PLAYING
        self.time_control_button.disable()
        self.pause_button.to_pause()

        if self.current_turn == self.player_left:
            self.player_left_button.enable()
            self.player_left_button.count_down()
            self.player_right_button.disable()

        elif self.current_turn == self.player_right:
            self.player_right_button.enable()
            self.player_right_button.count_down()
            self.player_left_button.disable()

    def pause(self):
        self.status = Status.PAUSED
        self.pause_button.to_play()

        self.player_left_button.disable()
        self.player_right_button.disable()

    def end(self):
        pass
        # TODO: implement end game
