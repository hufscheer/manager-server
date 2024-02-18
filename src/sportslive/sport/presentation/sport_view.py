from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.domain import IsAdminUser
from sport.containers import SportContainer
from drf_yasg.utils import swagger_auto_schema
from sport.serializers import SportsNameResponseSerializer

class SportView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._sport_serivce = SportContainer.sport_service()

    @swagger_auto_schema(responses={"200": SportsNameResponseSerializer(many=True)})
    def get(self, request):
        """
        모든 스포츠 목록 조회 API
        """
        response = self._sport_serivce.get_all_sport_list()
        return Response(response, status=status.HTTP_200_OK)