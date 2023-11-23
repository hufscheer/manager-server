from game.domain import GameRepository, GameTeam
from game.serializers import (
                            GameTeamSaveSerializer,
                            GameTeamRequestSerializer,
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