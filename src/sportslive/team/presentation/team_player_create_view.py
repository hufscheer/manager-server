from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.domain import IsAdminUser
from team.containers import TeamContainer
from drf_yasg.utils import swagger_auto_schema
from team.serializers import (
    TeamPlayerRegisterRequestSerializer,
    TeamPlayerChangeRequestSerializer
)

class TeamPlayerCreateView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._team_player_service = TeamContainer.team_player_service()


    @swagger_auto_schema(request_body=TeamPlayerRegisterRequestSerializer(many=True), responses={"201": ''})
    def post(self, request, team_id: int):
        """
        리그팀 플레이어 생성 API
        """
        self._team_player_service.register_team_players(request_data=request.data, team_id=team_id)
        return Response(status=status.HTTP_201_CREATED)