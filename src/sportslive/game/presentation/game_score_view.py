from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.domain import IsAdminUser
from game.containers import GameContainer
from drf_yasg.utils import swagger_auto_schema
from game.serializers import GameScoreChangeSerializer

class GameScoreView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._game_team_serivice = GameContainer.game_team_serivice()
        
    @swagger_auto_schema(request_body=GameScoreChangeSerializer, responses={"200": ''})
    def post(self, request, *args, **kwargs):
        """
        게임의 스코어만 변경할 수 있는 API 입니다.
        """
        self._game_team_serivice.change_score(request.data)
        return Response(status=status.HTTP_200_OK)