from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.core.exceptions import PermissionDenied
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.domain import IsAdminUser
from team.containers import TeamContainer
from league.containers import LeagueContainer

class TeamView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.team_service = TeamContainer.team_service()
        self.league_service = LeagueContainer.league_get_service()

    def post(self, request, league_id: int):
        league = self.league_service.find_one_league(league_id)
        response = self.team_service.register_teams(request_data=request.data, league=league, user_data=request.user)
        return Response(response, status=status.HTTP_201_CREATED)

    def put(self, request):
        pass
    def delete(self, request):
        pass
