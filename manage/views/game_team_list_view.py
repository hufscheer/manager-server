from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.models.is_admin_user import IsAdminUser
from manage.services import get_team_list


class GameTeamListView(APIView):
    """
    특정 게임의 팀 리스트를 조회하는 View
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def get(self, request, game_id: int):
        try:
            response = get_team_list(game_id)
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
             return Response({"detail": "잘못된 요청입니다.", "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
