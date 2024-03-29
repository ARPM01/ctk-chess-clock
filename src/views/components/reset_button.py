import customtkinter as ctk

from PIL import Image

from src.models import Constant


class ResetButton(ctk.CTkButton):
    def __init__(self, master, **kwargs):
        super().__init__(
            master,
            image=ctk.CTkImage(
                dark_image=Image.open(Constant.PATH_RESET),
                size=Constant.SIZE_ICONS,
            ),
            text="",
            **kwargs
        )
        self.master = master
