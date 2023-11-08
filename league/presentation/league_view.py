from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.domain import IsAdminUser
from league.containers import LeagueContainer

class LeagueView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._league_serivice = LeagueContainer.league_service()

    def post(self, request):

        self._league_serivice.register_league(request.data, request.user)
        return Response(status=status.HTTP_200_OK)

    def put(self, request):
        pass

    def delete(self, request):
        pass