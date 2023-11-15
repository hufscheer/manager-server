from game.domain import GameRepository
from accounts.domain import Member
from game.serializers import GameRequestSerializer, GameSaveSerializer

class GameService:
    def __init__(self, game_repository: GameRepository, *args, **kwargs):
        self._game_repository = game_repository
    
    def create_game(self, league_id: int, request_data, user_data: Member):
        game_request_serializer = GameRequestSerializer(data=request_data)
        game_request_serializer.is_valid(raise_exception=True)
        game_data = game_request_serializer.validated_data

        game_data['administrator'] = user_data.id
        game_data['league'] = league_id
        game_save_serialzier = GameSaveSerializer(data=game_data)
        game_save_serialzier.is_valid(raise_exception=True)
        game_save_serialzier.save()

    def create_game_team(self):
        pass