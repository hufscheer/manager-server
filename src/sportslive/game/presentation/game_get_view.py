from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.domain import IsAdminUser
from game.containers import GameContainer
from drf_yasg.utils import swagger_auto_schema
from game.serializers import GameInfoResponseSerializer

class GameGetView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._game_service = GameContainer.game_service()

    @swagger_auto_schema(responses={"200": GameInfoResponseSerializer})
    def get(self, request, game_id: int):
        """
        게임 수정 정보 조회 API
        """
        response = self._game_service.get_game_info(game_id)
        return Response(response, status=status.HTTP_200_OK)