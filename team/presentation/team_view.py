from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.core.exceptions import PermissionDenied
from team.domain import Team
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.domain import IsAdminUser
from team.containers import TeamContainer
from league.containers import LeagueContainer

class TeamView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._team_service = TeamContainer.team_service()
        self._league_service = LeagueContainer.league_get_service()

    def post(self, request, league_id: int):
        league = self._league_service.find_one_league(league_id)
        response = self._team_service.register_teams(request_data=request.data, league=league, user_data=request.user)
        return Response(response, status=status.HTTP_201_CREATED)

    def put(self, request, *args, **kwargs):
        try:
            league_id = request.query_params.get('leagueId')
            team_id = request.query_params.get('teamId')
            league = self._league_service.find_one_league(league_id)
            team = self._team_service.find_one_team(team_id)
            self._team_service.change_team(request_data=request.data, league=league, team=team, user_data=request.user)
            return Response(status=status.HTTP_200_OK)
        except Team.DoesNotExist:
            return Response({"error": "리그를 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)
        except PermissionDenied:
            return Response({"error": "권한이 없습니다."}, status=status.HTTP_403_FORBIDDEN)
        
    def delete(self, request):
        pass
