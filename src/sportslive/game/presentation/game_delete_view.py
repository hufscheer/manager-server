from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.domain import IsAdminUser
from game.containers import GameContainer
from drf_yasg.utils import swagger_auto_schema

class GameDeleteView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._game_serivce = GameContainer.game_service()

    @swagger_auto_schema(responses={"204": ""})
    def delete(self, request, game_id: int):
        """
        게임 삭제 API
        """
        self._game_serivce.delete_game(game_id, request.user)
        return Response(status=status.HTTP_204_NO_CONTENT)