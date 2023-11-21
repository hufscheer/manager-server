from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
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
    
    def put(self, request, team_player_id: int):
        self._team_player_service.change_team_player(request.data, team_player_id)
        return Response(status=status.HTTP_200_OK)
    
    def delete(self, request, team_player_id: int):
        self._team_player_service.delete_team_player(team_player_id, request.user)
        return Response(status=status.HTTP_204_NO_CONTENT)