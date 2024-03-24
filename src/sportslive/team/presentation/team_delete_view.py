from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.domain import IsAdminUser
from team.containers import TeamContainer
from drf_yasg.utils import swagger_auto_schema

class TeamDeleteView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._team_service = TeamContainer.team_service()
    
    @swagger_auto_schema(responses={"204": ""})
    def delete(self, request, team_id: int, *args, **kwargs):
        """
        리그팀 삭제 API
        """
        self._team_service.delete_team(team_id=team_id, user_data=request.user)
        return Response(status=status.HTTP_204_NO_CONTENT)
