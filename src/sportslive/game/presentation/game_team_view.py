from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.core.exceptions import PermissionDenied
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.domain import IsAdminUser
from game.containers import GameContainer

class GameTeamView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._game_team_serivce = GameContainer.game_team_serivice()

    def post(self, request, game_id: int):
        self._game_team_serivce.create_game_team(request.data, game_id)
        return Response(status=status.HTTP_200_OK)