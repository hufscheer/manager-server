from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.domain import IsAdminUser

class PermissionTestView(APIView):
    """
    토큰 인증이 되는지 확인하는 view
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def get(self, request):
        try:
            user = request.user
            return Response({"detail": f"{user}, 정상적으로 확인되었습니다."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"detail": "잘못된 요청입니다.", "error": e}, status=status.HTTP_400_BAD_REQUEST)
        