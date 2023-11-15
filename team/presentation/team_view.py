from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.core.exceptions import PermissionDenied
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.domain import IsAdminUser
from team.containers import TeamContainer

class TeamView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._team_service = TeamContainer.team_service()

    def post(self, request, league_id: int):
        response = self._team_service.register_teams(request_data=request.data, league_id=league_id, user_data=request.user)
        return Response(response, status=status.HTTP_201_CREATED)

    def put(self, request, *args, **kwargs):
        try:
            league_id = request.query_params.get('leagueId')
            team_id = request.query_params.get('teamId')
            self._team_service.change_team(request_data=request.data, league_id=league_id, team_id=team_id, user_data=request.user)
            return Response(status=status.HTTP_200_OK)
        except PermissionDenied:
            return Response({"error": "권한이 없습니다."}, status=status.HTTP_403_FORBIDDEN)
