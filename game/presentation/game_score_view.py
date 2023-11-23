from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.domain import IsAdminUser
from game.containers import GameContainer

class GameScoreView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._game_team_serivice = GameContainer.game_team_serivice()
    
    def post(self, request, *args, **kwargs):
        self._game_team_serivice.change_score(request.data)
        return Response(status=status.HTTP_200_OK)