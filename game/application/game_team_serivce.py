from game.domain import GameRepository, GameTeamPlayer, GameTeam
from game.serializers import (
                            GameTeamSaveSerializer,
                            GameTeamRequestSerializer,
                            GameTeamPlayerRequestSerialzier,
                            GameTeamPlayerChangeSerialzier,
                            GameTeamPlayerSaveSerialzier,
                            GameScoreChangeSerializer,
                            )
from team.domain import TeamRepository

class GameTeamService:

    def __init__(self, game_repository: GameRepository, team_repository: TeamRepository, *args, **kwargs):
        self._game_repository = game_repository
        self._team_repository = team_repository

    def create_game_team(self, request_data, game_id: int):
        game_team_request_serializer = GameTeamRequestSerializer(data=request_data)
        game_team_request_serializer.is_valid(raise_exception=True)
        game_team_data = game_team_request_serializer.validated_data
        team_ids: list = game_team_data.get('team_ids')

        game = self._game_repository.find_game_by_id(game_id)

        for team_id in team_ids:
            team = self._team_repository.find_team_by_id(team_id)
            game_team_save_serializer = GameTeamSaveSerializer(data={'game': game.id, 'team': team.id})
            game_team_save_serializer.is_valid(raise_exception=True)
            game_team_save_serializer.save()
    
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

    def change_score(self, request_data: dict):
        game_score_change_serializer = GameScoreChangeSerializer(data=request_data)
        game_score_change_serializer.is_valid(raise_exception=True)
        game_score_data: dict = game_score_change_serializer.validated_data
        team_score_mapping_list: list[dict] = game_score_data.get('team_score')

        for team_score_mapping in team_score_mapping_list:
            team_id = team_score_mapping.get('id')
            new_score = team_score_mapping.get('score')

            game_team: GameTeam = self._game_repository.find_game_team_by_id(team_id)
            game_team.score = new_score
            self._game_repository.save_game_team(game_team)

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