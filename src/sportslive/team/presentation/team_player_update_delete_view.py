from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.domain import IsAdminUser
from team.containers import TeamContainer
from drf_yasg.utils import swagger_auto_schema
from team.serializers import (
    TeamPlayerChangeRequestSerializer
)

class TeamPlayerUpdateDeleteView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._team_player_service = TeamContainer.team_player_service()

    @swagger_auto_schema(request_body=TeamPlayerChangeRequestSerializer, responses={"200": ''})
    def put(self, request, team_player_id: int):
        """
        리그팀 플레이어 수정 API
        """
        self._team_player_service.change_team_player(request.data, team_player_id)
        return Response(status=status.HTTP_200_OK)
    
    @swagger_auto_schema(responses={"204": ''})
    def delete(self, request, team_player_id: int):
        """
        리그팀 플레이어 삭제 API
        """
        self._team_player_service.delete_team_player(team_player_id, request.user)
        return Response(status=status.HTTP_204_NO_CONTENT)