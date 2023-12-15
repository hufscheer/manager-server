from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.core.exceptions import PermissionDenied
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.domain import IsAdminUser
from game.containers import GameContainer

class GameTeamGetView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._game_team_get_serivce = GameContainer.game_team_get_serivice()

    def get(self, request, game_id: int):
        response = self._game_team_get_serivce.get_game_teams_info(game_id)
        return Response(response, status=status.HTTP_200_OK)