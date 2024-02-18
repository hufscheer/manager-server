from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.core.exceptions import PermissionDenied
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.domain import IsAdminUser
from league.containers import LeagueContainer
from drf_yasg.utils import swagger_auto_schema
from league.serializers import (
    LeagueSportRegistrationSerializer,
    LeagueRegisterResponseSerializer,
    LeagueSportChangeSerializer,
    LeagueDeleteSerializer,
)

class LeagueView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._league_serivice = LeagueContainer.league_service()

    @swagger_auto_schema(
            request_body=LeagueSportRegistrationSerializer,
            responses={"201": LeagueRegisterResponseSerializer}
            )
    def post(self, request):
        """
        리그 생성 API
        """
        response = self._league_serivice.register_league(request.data, request.user)
        return Response(response, status=status.HTTP_201_CREATED)
    
    @swagger_auto_schema(request_body=LeagueSportChangeSerializer, responses={"200": ""})
    def put(self, request):
        """
        리그 수정 API
        """
        self._league_serivice.change_league(request.data, request.user)
        return Response(status.HTTP_200_OK)
        
    @swagger_auto_schema(request_body=LeagueDeleteSerializer, responses={"204": ""})
    def delete(self, request):
        """
        리그 삭제 API
        """
        self._league_serivice.delete_league(request.data, request.user)
        return Response(status.HTTP_204_NO_CONTENT)