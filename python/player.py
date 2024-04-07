from pysamp.player import Player as BasePlayer
from functools import wraps


class Player(BasePlayer):
    _pool: dict[int, BasePlayer] = {}

    def __init__(self, player_id):
        super().__init__(player_id)

    @classmethod
    def from_pool(cls: BasePlayer, player) -> "Player":
        if isinstance(player, int):
            player_id = player
        
        if isinstance(player, BasePlayer):
            player_id = player.id

        player: Player = cls._pool.get(player_id)

        if not player:
            cls._pool[player_id] = player = cls(player_id)

        return player

    @classmethod
    def remove_from_pool(cls, player: BasePlayer):
        del cls._pool[player.id]
    
    @classmethod
    def using_pool(cls, func):
        @wraps(func)
        def from_pool(*args, **kwargs):
            args = list(args)
            args[0] = cls.from_pool(args[0])
            return func(*args, **kwargs)

        return from_pool
