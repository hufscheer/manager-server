from game.domain import GameRepository, Game, GameTeam
from accounts.domain import Member
from game.serializers import (
                    GameRequestSerializer,
                    GameChangeSerializer,
                    GameInfoResponseSerializer,
                )
from league.domain import LeagueRepository, League
from django.core.exceptions import PermissionDenied
from datetime import datetime
from pytz import timezone

class GameService:
    def __init__(self, game_repository: GameRepository, league_repository: LeagueRepository, *args, **kwargs):
        self._game_repository = game_repository
        self._league_repository = league_repository

    def create_game(self, league_id: int, request_data, user_data: Member):
        game_request_serializer = GameRequestSerializer(data=request_data)
        game_request_serializer.is_valid(raise_exception=True)
        game_data: dict = game_request_serializer.validated_data

        league = self._league_repository.find_league_by_id(league_id)
        new_game: Game = self._create_game_object(game_data, user_data, league)
        self._game_repository.save_game(new_game)

        team_ids = game_data.get('team_ids')
        for team_id in team_ids:
            new_game_team: GameTeam = self._create_game_team_object(team_id, new_game)
            self._game_repository.save_game_team(new_game_team)

    def change_game(self, game_id: int, request_data, user_data: Member):
        game: Game = self._game_repository.find_game_by_id(game_id)
        if game.manager_id != user_data.id:
            raise PermissionDenied
        
        game_change_serializer = GameChangeSerializer(game, data=request_data)
        game_change_serializer.is_valid(raise_exception=True)
        game_change_data = game_change_serializer.validated_data
        self._change_game_object(game, game_change_data)

    def get_game_info(self, game_id: int):
        game: Game = self._game_repository.find_game_with_sport_by_id(game_id)
        game_info_response_serialzier = GameInfoResponseSerializer(game)
        return game_info_response_serialzier.data
    
    def _create_game_object(self, game_data: dict, user_data: Member, league: League) -> Game:
        return Game(
            sport_id=game_data.get('sport_id'),
            manager=user_data,
            league=league,
            name=game_data.get('name'),
            start_time=game_data.get('start_time'),
            video_id=game_data.get('video_id', None),
            round=game_data.get('round'),
            quarter_changed_at=datetime.now(timezone('Asia/Seoul'))
        )
    
    def _change_game_object(self, game: Game, game_change_data: dict):
        game.sport_id = game_change_data.get('sport_id')
        game.start_time = game_change_data.get('start_time')
        game.video_id = game_change_data.get('video_id')
        game.game_quarter = game_change_data.get('game_quarter')
        game.name = game_change_data.get('name')
        game.state = game_change_data.get('state')
        game.round = game_change_data.get('round')
        game.quarter_changed_at = datetime.now(timezone('Asia/Seoul'))
        self._game_repository.save_game(game)

    def _create_game_team_object(self, team_id: int, game: Game) -> GameTeam:
        return GameTeam(game=game, league_team_id=team_id)
    
    class _ExtraGameInfoDTO:
        def __init__(self, sport_name: str, state: str):
            self.sport_name = sport_name
            self.state = state
    