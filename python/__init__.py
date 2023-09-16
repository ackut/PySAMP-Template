import samp  # It's a normal.
from pysamp import *
from python.player import *


samp.config(encoding='cp1251')  # For support cyrillic characters.


@on_gamemode_init
def on_init():
    set_game_mode_text('PySAMP Mode')
    add_player_class(0, -2623.6630, 1408.8757, 7.1015, 195.1507, -1, -1, -1, -1, -1, -1)
    show_player_markers(1)
    show_name_tags(True)
    set_name_tag_draw_distance(40)
    enable_stunt_bonus_for_all(False)
    disable_interior_enter_exits()
    set_weather(0)


@Player.on_connect
@Player.using_pool
def on_player_connect(player: Player):
    player.send_client_message(-1, f'Welcome, {player.get_name()}!')

    
@Player.on_disconnect
@Player.using_pool
def on_player_disconnect(player: Player, reason: int):
    player.remove_from_pool(player)
