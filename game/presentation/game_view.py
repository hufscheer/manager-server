from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.core.exceptions import PermissionDenied
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.domain import IsAdminUser
from game.containers import GameContainer

class GameView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._game_serivce = GameContainer.game_service()

    def post(self, request, league_id: int):
        self._game_serivce.create_game(league_id, request.data, request.user)
        return Response(status=status.HTTP_200_OK)
    
    def put(self, request, *args, **kwargs):
        pass
    def delete(self, request):
        pass
