from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.domain import IsAdminUser
from game.containers import GameContainer

class GameTeamPlayerView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._game_team_player_service = GameContainer.game_team_player_service()

    def post(self, request, game_team_id: int):
        self._game_team_player_service.register_game_team_player(game_team_id, request.data)
        return Response(status=status.HTTP_201_CREATED)
    
    def put(self, request, game_team_id: int):
        self._game_team_player_service.change_game_team_player(game_team_id, request.data)
        return Response(status=status.HTTP_200_OK)