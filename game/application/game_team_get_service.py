from game.domain import GameRepository, GameTeamPlayer
from game.serializers import GameTeamPlayerGetSerializer

class GameTeamGetService:
    def __init__(self, game_repository: GameRepository, *args, **kwargs):
        self._game_repository = game_repository

    def get_all_game_team_player(self, game_team_id: int):
        game_team_players: list[GameTeamPlayer] = self._game_repository.find_game_team_players_by_game_team_id(game_team_id)
        game_team_player_get_serializer = GameTeamPlayerGetSerializer(game_team_players, many=True)
        return game_team_player_get_serializer.data