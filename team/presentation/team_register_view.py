from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.core.exceptions import PermissionDenied
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.domain import IsAdminUser
from team.containers import TeamContainer

class TeamRegisterView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._team_register_service = TeamContainer.team_register_service()
        
    def post(self, request, league_id: int):
        response = self._team_register_service.register_teams(request_data=request.data, league_id=league_id, user_data=request.user)
        return Response(response, status=status.HTTP_201_CREATED)
