from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.core.exceptions import PermissionDenied
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.domain import IsAdminUser
from team.containers import TeamContainer

class TeamPlayerView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._team_player_service = TeamContainer.team_player_service()

    def post(self, request, team_id: int):
        response = self._team_player_service.register_team_players(request_data=request.data, team_id=team_id)
        return Response(response, status=status.HTTP_201_CREATED)