from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.domain import IsAdminUser
from league.containers import LeagueContainer
from league.domain import League
from drf_yasg.utils import swagger_auto_schema
from league.serializers import LeagueListGetSerializer

class LeagueGetView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._league_get_service = LeagueContainer.league_get_service()

    @swagger_auto_schema(responses={"200": LeagueListGetSerializer})
    def get(self, request):
        """
        리그 전제 조회 API
        """
        response = self._league_get_service.get_leagues(request.user)
        return Response(response, status.HTTP_200_OK)
