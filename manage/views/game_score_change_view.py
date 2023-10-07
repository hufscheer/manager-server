from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.models.is_admin_user import IsAdminUser
from manage.services import get_game_info, change_game_score


class GameScoreChangeView(APIView):
    """
    경기의 점수를 변경하는 View
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def get(self, request, game_id: int):
        try:
            response = get_game_info(game_id)
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
             return Response({"detail": "잘못된 요청입니다.", "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, game_id: int):
        try:
            change_game_score(request.data, game_id)
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
             return Response({"detail": "잘못된 요청입니다.", "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
