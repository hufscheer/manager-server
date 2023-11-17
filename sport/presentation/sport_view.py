from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.core.exceptions import PermissionDenied
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.domain import IsAdminUser
from sport.containers import SportContainer

class SportView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._sport_serivce = SportContainer.sport_service()

    def get(self, request):
        response = self._sport_serivce.get_all_sport_list()
        return Response(response, status=status.HTTP_200_OK)