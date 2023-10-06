from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.models.is_admin_user import IsAdminUser
from manage.services import post_game


class GameRegisterView(APIView):
    """
    경기를 등록하는 View
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def post(self, request, *args, **kwargs):
        try:
            post_game(request.data, request.user)
            return Response(status=status.HTTP_201_CREATED)
        except Exception as e:
             return Response({"detail": "잘못된 요청입니다.", "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
