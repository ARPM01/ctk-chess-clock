import customtkinter as ctk

from src.models import Player, Constant


class PlayerButtonFrame(ctk.CTkFrame):
    def __init__(
        self, master, player_left: Player, player_right: Player, *args, **kwargs
    ):
        super().__init__(master, *args, **kwargs)
        self.player_left = player_left
        self.player_right = player_right

        self.moves_made_player_left = ctk.CTkLabel(
            self,
            text=Constant.STRING_MOVES_MADE.format(
                moves_made=self.player_left.moves_made
            ),
        )
        self.moves_made_player_left.place(
            rely=0.95,
            relx=0.1,
            anchor=ctk.CENTER,
        )
        self.moves_made_player_right = ctk.CTkLabel(
            self,
            text=Constant.STRING_MOVES_MADE.format(
                moves_made=self.player_right.moves_made
            ),
        )
        self.moves_made_player_right.place(
            rely=0.95,
            relx=0.9,
            anchor=ctk.CENTER,
        )

    def update_moves_made(self):
        self.moves_made_player_left.configure(
            text=Constant.STRING_MOVES_MADE.format(
                moves_made=self.player_left.moves_made
            )
        )
        self.moves_made_player_right.configure(
            text=Constant.STRING_MOVES_MADE.format(
                moves_made=self.player_right.moves_made
            )
        )
