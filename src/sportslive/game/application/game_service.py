from game.domain import GameRepository, Game, GameTeam
from accounts.domain import Member
from game.serializers import (
                    GameRequestSerializer,
                    GameChangeSerializer,
                    GameInfoResponseSerializer,
                )
from league.domain import LeagueRepository, League
from django.core.exceptions import PermissionDenied
from utils.exceptions.game_exceptions import CantDeleteGameError, CantParsingYoutubeUrl, BiggerThanMaxRoundError
from datetime import datetime
import re

class GameService:
    def __init__(self, game_repository: GameRepository, league_repository: LeagueRepository):
        self._game_repository = game_repository
        self._league_repository = league_repository

    def create_game(self, league_id: int, request_data, user_data: Member):
        game_request_serializer = GameRequestSerializer(data=request_data)
        game_request_serializer.is_valid(raise_exception=True)
        game_data: dict = game_request_serializer.validated_data

        league = self._league_repository.find_league_by_id(league_id)
        self._check_round(game_data, league)
        new_game: Game = self._create_game_object(game_data, user_data, league)
        self._game_repository.save_game(new_game)

        team_ids = game_data.get('team_ids')
        for team_id in team_ids:
            new_game_team: GameTeam = self._create_game_team_object(team_id, new_game)
            self._game_repository.save_game_team(new_game_team)

    def change_game(self, game_id: int, request_data, user_data: Member):
        game: Game = self._game_repository.find_game_with_manger_by_id(game_id)
        if game.manager.organization != user_data.organization:
            raise PermissionDenied
        league = self._league_repository.find_league_by_id(game.league_id)
        game_change_serializer = GameChangeSerializer(game, data=request_data)
        game_change_serializer.is_valid(raise_exception=True)
        game_change_data = game_change_serializer.validated_data
        self._check_round(game_change_data, league)
        self._change_game_object(game, game_change_data)

    def delete_game(self, game_id: int, user_data: Member):
        game: Game = self._game_repository.find_game_with_manger_by_id(game_id)
        if game.manager.organization != user_data.organization:
            raise PermissionDenied
        if game.state != 'SCHEDULED':
            raise CantDeleteGameError

        self._game_repository.delete_game(game)

    def get_game_info(self, game_id: int):
        game: Game = self._game_repository.find_game_by_id_with_sport_and_league(game_id)
        game_info_response_serialzier = GameInfoResponseSerializer(game)
        return game_info_response_serialzier.data
    
    def _check_round(self, game_data: dict, league: League):
        round = game_data.get('round')
        league_max_round = league.max_round
        if round > league_max_round:
            raise BiggerThanMaxRoundError
        
    def _create_game_object(self, game_data: dict, user_data: Member, league: League) -> Game:
        return Game(
            sport_id=game_data.get('sport_id'),
            manager=user_data,
            league=league,
            name=game_data.get('name'),
            start_time=game_data.get('start_time'),
            video_id=self._parsing_youtube_url(game_data.get('video_id', None)),
            round=game_data.get('round'),
            quarter_changed_at=datetime.now()
        )
    
    def _change_game_object(self, game: Game, game_change_data: dict):
        game.sport_id = game_change_data.get('sport_id')
        game.start_time = game_change_data.get('start_time')
        game.video_id = self._parsing_youtube_url(game_change_data.get('video_id', None))
        game.game_quarter = game_change_data.get('game_quarter')
        game.name = game_change_data.get('name')
        game.state = game_change_data.get('state')
        game.round = game_change_data.get('round')
        game.quarter_changed_at = datetime.now()
        self._game_repository.save_game(game)

    def _create_game_team_object(self, team_id: int, game: Game) -> GameTeam:
        return GameTeam(game=game, league_team_id=team_id)
    
    def _parsing_youtube_url(self, video_url):
        if not video_url:
            return None
        
        regex_patterns = [
            r'(?:v=|\/)([0-9A-Za-z_-]{11}).*',
            r'youtu\.be\/([0-9A-Za-z_-]{11}).*'
        ]
        
        for pattern in regex_patterns:
            match = re.search(pattern, video_url)
            if match:
                return match.group(1)
        
        raise CantParsingYoutubeUrl

    class _ExtraGameInfoDTO:
        def __init__(self, sport_name: str, state: str):
            self.sport_name = sport_name
            self.state = state
    