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

    def put(self, request, team_id: int, *args, **kwargs):
        self._team_service.change_team(request_data=request.data, team_id=team_id, user_data=request.user)
        return Response(status=status.HTTP_200_OK)
