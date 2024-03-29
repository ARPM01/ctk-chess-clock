import customtkinter as ctk

from src.models import TimeControl


class TimeControlPicker(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)

        self.center_window(master)
        self.title("Time Control")
        self.grab_set()
        self.attributes("-topmost", True)

        self.master = master

        self.time_control_option_label = ctk.CTkLabel(self, text="Time Control: ")
        self.time_control_option_menu = ctk.CTkOptionMenu(
            self,
            variable=self.master.time_control,
            values=[time_control.name.capitalize() for time_control in TimeControl],
        )

        self.ok_button = ctk.CTkButton(self, text="OK", command=self.destroy)

        self.time_control_option_label.grid(row=0, column=0, padx=10, pady=10)
        self.time_control_option_menu.grid(
            row=0, column=1, padx=10, pady=10, sticky=ctk.NSEW
        )
        self.ok_button.grid(
            row=1, column=0, columnspan=2, padx=10, pady=10, sticky=ctk.NSEW
        )

        # TODO: add support for custom time control

    def center_window(self, master):
        self.update_idletasks()

        # Get the master window's width, height, and position
        master_width = master.winfo_width()
        master_height = master.winfo_height()
        master_x = master.winfo_rootx()
        master_y = master.winfo_rooty()

        # Calculate the position of the top-left corner of the window
        position_top = int(master_y + master_height / 2 - self.winfo_height() / 2)
        position_left = int(master_x + master_width / 2 - self.winfo_width() / 2)

        # Position the window
        self.geometry(f"+{position_left}+{position_top}")
