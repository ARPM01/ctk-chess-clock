from src.models import Color, TimeControl, Player, Side
from src.views import Clock, TimeControlPicker

if __name__ == "__main__":
    # TODO: set default in a config.ini
    default_time_control = TimeControl.CLASSICAL

    player_1 = Player(
        Color.WHITE,
        Side.LEFT,
        default_time_control.duration,
        default_time_control.increment,
    )
    player_2 = Player(
        Color.BLACK,
        Side.RIGHT,
        default_time_control.duration,
        default_time_control.increment,
    )

    clock = Clock(player_1, player_2)

    clock.run()

# TODO: prepare executable on github release
