from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.domain import IsAdminUser
from team.containers import TeamContainer
from drf_yasg.utils import swagger_auto_schema
from team.serializers import TeamPlayersResponseSerialier

class TeamPlayerGetView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._team_player_get_service = TeamContainer.team_player_get_service()

    @swagger_auto_schema(responses={"200": TeamPlayersResponseSerialier(many=True)})
    def get(self, request, team_id: int):
        """
        리그 팀 플레이어 전체 조회 API
        """
        response = self._team_player_get_service.get_all_team_player(team_id)
        return Response(response, status=status.HTTP_200_OK)