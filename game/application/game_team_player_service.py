from game.domain import GameRepository, GameTeamPlayer, GameTeam
from game.serializers import (
                            GameTeamPlayerRequestSerialzier,
                            GameTeamPlayerChangeSerialzier,
                            GameTeamPlayerSaveSerialzier,
                            )
class GameTeamPlayerService:

    def __init__(self, game_repository: GameRepository, *args, **kwargs):
        self._game_repository = game_repository
    
    def register_game_team_player(self, game_team_id: int, request_data):
        game_team = self._game_repository.find_game_team_by_id(game_team_id)
        game_team_player_request_serializer = GameTeamPlayerRequestSerialzier(data=request_data, many=True)
        game_team_player_request_serializer.is_valid(raise_exception=True)
        game_team_player_datas = game_team_player_request_serializer.validated_data

        for game_team_player_data in game_team_player_datas:
            self._create_game_team_player_object(game_team, game_team_player_data)

    def change_game_team_player(self, game_team_id: int, request_data: dict):
        game_team = self._game_repository.find_game_team_by_id(game_team_id)
        game_team_player_change_serializer = GameTeamPlayerChangeSerialzier(data=request_data, many=True)
        game_team_player_change_serializer.is_valid(raise_exception=True)
        game_team_player_change_datas: list[dict] = game_team_player_change_serializer.validated_data
        exist_game_team_player_ids: set = self._get_exist_game_team_players(game_team.id)

        for game_team_player_change_data in game_team_player_change_datas:
            target_id: int = game_team_player_change_data.get('id', None)
            if not target_id:
                self._create_game_team_player_object(game_team, game_team_player_change_data)
                continue

            if target_id in exist_game_team_player_ids:
                exist_game_team_player_ids.remove(target_id)

            game_team_player = self._game_repository.find_game_team_player_by_id(target_id)
            game_team_player_save_serializer = GameTeamPlayerSaveSerialzier(game_team_player, data=game_team_player_change_data, partial=True)
            game_team_player_save_serializer.is_valid(raise_exception=True)
            game_team_player_save_serializer.save()

        if exist_game_team_player_ids:
            self._game_repository.delete_game_team_players_by_ids(exist_game_team_player_ids)

    def _get_exist_game_team_players(self, game_team_id: int):
        game_team_players = self._game_repository.find_game_team_players_by_game_team_id(game_team_id)
        return set(player.id for player in game_team_players)
    
    def _create_game_team_player_object(self, game_team: GameTeam, game_team_player_data: dict):
        game_team_player = GameTeamPlayer(
            game_team=game_team,
            name=game_team_player_data.get('name'),
            description=game_team_player_data.get('description')
        )
        self._game_repository.save_game_team_player(game_team_player)