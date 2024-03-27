from game.domain import GameRepository, LineupPlayer, GameTeam
from game.serializers import (
                            LineupPlayerRequestSerialzier,
                            LineupPlayerSaveSerialzier,
                            LineupPlayerChangeSerialzier,
                            )
class LineupPlayerService:

    def __init__(self, game_repository: GameRepository, *args, **kwargs):
        self._game_repository = game_repository
    
    def register_lineup_player(self, game_team_id: int, request_data):
        game_team = self._game_repository.find_game_team_by_id(game_team_id)
        lineup_player_request_serializer = LineupPlayerRequestSerialzier(data=request_data, many=True)
        lineup_player_request_serializer.is_valid(raise_exception=True)
        lineup_player_datas = lineup_player_request_serializer.validated_data

        for lineup_player_data in lineup_player_datas:
            self._create_lineup_player_object(game_team, lineup_player_data)

    def change_lineup_player(self, game_team_id: int, request_data: dict):
        game_team = self._game_repository.find_game_team_by_id(game_team_id)
        lineup_player_change_serializer = LineupPlayerChangeSerialzier(data=request_data, many=True)
        lineup_player_change_serializer.is_valid(raise_exception=True)
        lineup_player_change_datas: list[dict] = lineup_player_change_serializer.validated_data
        exist_lineup_player_ids: set = self._get_exist_lineup_players(game_team.id)

        for lineup_player_change_data in lineup_player_change_datas:
            target_id: int = lineup_player_change_data.get('id', None)
            if not target_id:
                self._create_lineup_player_object(game_team, lineup_player_change_data)
                continue

            if target_id in exist_lineup_player_ids:
                exist_lineup_player_ids.remove(target_id)

            lineup_player = self._game_repository.find_lineup_player_by_id(target_id)
            lineup_player_save_serializer = LineupPlayerSaveSerialzier(lineup_player, data=lineup_player_change_data, partial=True)
            lineup_player_save_serializer.is_valid(raise_exception=True)
            lineup_player_save_serializer.save()

        if exist_lineup_player_ids:
            self._game_repository.delete_lineup_players_by_ids(exist_lineup_player_ids)

    def _get_exist_lineup_players(self, game_team_id: int):
        lineup_players = self._game_repository.find_lineup_players_by_game_team_id(game_team_id)
        return set(player.id for player in lineup_players)
    
    def _create_lineup_player_object(self, game_team: GameTeam, lineup_player_data: dict):
        lineup_player = LineupPlayer(
            game_team=game_team,
            name=lineup_player_data.get('name'),
            description=lineup_player_data.get('description'),
            number=lineup_player_data.get('number'),
            is_captain=lineup_player_data.get('is_captain'),
            league_team_player_id=lineup_player_data.get('league_team_player_id')
        )
        self._game_repository.save_lineup_player(lineup_player)