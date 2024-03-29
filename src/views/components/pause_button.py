import customtkinter as ctk

from PIL import Image

from src.models import Constant


class PauseButton(ctk.CTkButton):
    def __init__(self, master, **kwargs):
        super().__init__(
            master,
            image=ctk.CTkImage(
                dark_image=Image.open(Constant.PATH_PLAY),
                size=Constant.SIZE_ICONS,
            ),
            text="",
            **kwargs
        )
        self.__is_playing = False

        self.__clock = master.master
        self.__clock.bind("<space>", self.__on_space_key)

    def to_pause(self):
        self.configure(
            image=ctk.CTkImage(dark_image=Image.open(Constant.PATH_PAUSE)),
            command=self.to_play,
        )
        self.__is_playing = True

    def to_play(self):
        self.configure(
            image=ctk.CTkImage(dark_image=Image.open(Constant.PATH_PLAY)),
            command=self.to_pause,
        )
        self.__is_playing = False

    def __on_space_key(self, _):
        if self.__is_playing:
            self.__clock.pause()
        else:
            self.__clock.start()
