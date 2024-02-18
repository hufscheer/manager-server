from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.domain import IsAdminUser
from django.contrib.auth.hashers import make_password

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

class MakePasswordTest(APIView):
    """
    서버용 테스트 API 입니다.
    """
    def post(self, request, *args, **kwargs):
        password = request.data.get('password')
        password = make_password(password)
        return Response({
            'password': password
        })