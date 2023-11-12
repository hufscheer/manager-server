from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.core.exceptions import PermissionDenied
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.domain import IsAdminUser
from team.containers import TeamContainer
from league.containers import LeagueContainer

class TeamGetView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._team_get_service = TeamContainer.team_get_service()

    def get(self, request, league_id: int):
        response = self._team_get_service.get_all_teams(league_id)
        return Response(response, status=status.HTTP_200_OK)