import samp  # Обязательно импортировать в главный файл (этот). На варнинг внимания не обращать.
from pysamp import *  # Этот пакет содержит все методы сампа.
from pysamp.dialog import Dialog  # Это класс для работы с диалогами. Чисто для примера.
from python.player import Player  # Это кастомный класс игрока.


samp.config(encoding='cp1251')  # Для отображения кириллицы.


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
@Player.using_pool  # Во всех функциях, которые в качестве аргумента принимают игрока - использовать этот декоратор.
def on_player_connect(player: Player):
    player.send_client_message(-1, f'Добро пожаловать на сервер, {player.get_name()}!')
    send_client_message_to_all(-1, f'Игрок {{90ffaa}}{player.get_name()} {{ffffff}}подключился к серверу!')


@Player.on_disconnect
@Player.using_pool
def on_player_disconnect(player: Player, reason: int):
    send_client_message_to_all(-1, f'Игрок {{90ffaa}}{player.get_name()} {{ffffff}}отключился от сервера!')
    Player.remove_from_pool(player)  # При отключении игрока, обязательно удалять его из пула.
