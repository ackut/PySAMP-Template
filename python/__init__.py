import samp  # Be sure to import into the main file (this one). Do not pay attention to warning.
from pysamp import *  # This package contains all the samp methods.
from pysamp.dialog import Dialog  # This is a class for working with dialogs. Just for example.
from python.player import Player  # It's a custom player class.


samp.config(encoding='cp1251')  # To display the Cyrillic alphabet.


@on_gamemode_init
def on_gamemode_init():
    set_game_mode_text('--.--.24')
    # add_player_class(0, 258.22296142578, 2926.1264648438, 1.78125, 178.83819580078, -1, -1, -1, -1, -1, -1)
    show_player_markers(1)
    show_name_tags(True)
    set_name_tag_draw_distance(40)
    enable_stunt_bonus_for_all(False)
    disable_interior_enter_exits()
    set_weather(0)


@Player.on_connect
@Player.using_pool  # In all functions that take a player as an argument - use this decorator.
def on_player_connect(player: Player):
    player.send_client_message(-1, f'Welcome to the server, {player.get_name()}!')
    send_client_message_to_all(-1, f'Player {{90ffaa}}{player.get_name()} {{ffffffff}} has connected to the server!')


@Player.on_disconnect
@Player.using_pool
def on_player_disconnect(player: Player, reason: int):
    send_client_message_to_all(-1, f'Player {{90ffaa}}{player.get_name()} {{ffffffff}} has disconnected from the server!')
    Player.remove_from_pool(player)  # When disconnecting a player, be sure to remove him from the pool.
