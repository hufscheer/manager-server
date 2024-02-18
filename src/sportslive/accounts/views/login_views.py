from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from accounts.domain import Member
from django.contrib.auth.hashers import check_password
from rest_framework import status

class CustomTokenObtainPairView(TokenObtainPairView):
    """
    로그인을 하고, 토큰을 얻는 view
    """
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        user = Member.objects.filter(email=email).first()

        if not user or not check_password(password, user.password):
            return Response({"detail":'Invalid email/password combination'}, status=status.HTTP_400_BAD_REQUEST)

        refresh = RefreshToken.for_user(user)

        return Response({
            'access': str(refresh.access_token)
        })
