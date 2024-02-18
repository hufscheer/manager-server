from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.core.exceptions import PermissionDenied
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.domain import IsAdminUser
from game.containers import GameContainer
from drf_yasg.utils import swagger_auto_schema
from game.serializers import GameTeamInfoSerializer

class GameTeamGetView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._game_team_get_serivce = GameContainer.game_team_get_serivice()

    @swagger_auto_schema(responses={"200": GameTeamInfoSerializer(many=True)})
    def get(self, request, game_id: int):
        """
        게임 팀 정보 조회
        """
        response = self._game_team_get_serivce.get_game_teams_info(game_id)
        return Response(response, status=status.HTTP_200_OK)