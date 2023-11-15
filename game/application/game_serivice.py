from game.domain import GameRepository
from accounts.domain import Member
from game.serializers import GameRequestSerializer, GameSaveSerializer
from league.domain import LeagueRepository

class GameService:
    def __init__(self, game_repository: GameRepository, league_repository: LeagueRepository, *args, **kwargs):
        self._game_repository = game_repository
        self._league_repository = league_repository

    def create_game(self, league_id: int, request_data, user_data: Member):
        game_request_serializer = GameRequestSerializer(data=request_data)
        game_request_serializer.is_valid(raise_exception=True)
        game_data = game_request_serializer.validated_data

        league = self._league_repository.find_league_by_id(league_id)
        game_data['league'] = league.id
        game_data['administrator'] = user_data.id
        game_save_serialzier = GameSaveSerializer(data=game_data)
        game_save_serialzier.is_valid(raise_exception=True)
        game_save_serialzier.save()