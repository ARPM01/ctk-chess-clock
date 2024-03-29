import customtkinter as ctk

from src.models import Constant


class TimeControlButton(ctk.CTkButton):
    def __init__(self, master, **kwargs):
        super().__init__(master, text=Constant.STRING_PICK_TIME_CONTROL, **kwargs)
        self.master = master

    def disable(self):
        self.configure(state=ctk.DISABLED)
