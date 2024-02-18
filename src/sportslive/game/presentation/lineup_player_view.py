from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.domain import IsAdminUser
from game.containers import GameContainer
from drf_yasg.utils import swagger_auto_schema
from game.serializers import LineupPlayerRequestSerialzier, LineupPlayerChangeSerialzier

class LineupPlayerView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._game_team_player_service = GameContainer.lineup_player_service()

    @swagger_auto_schema(request_body=LineupPlayerRequestSerialzier(many=True), responses={"201": ''})
    def post(self, request, game_team_id: int):
        self._game_team_player_service.register_lineup_player(game_team_id, request.data)
        return Response(status=status.HTTP_201_CREATED)
    
    @swagger_auto_schema(request_body=LineupPlayerChangeSerialzier(many=True), responses={"200": ''})
    def put(self, request, game_team_id: int):
        """
        전체 조회로 선수들을 모두 불러온 뒤 수정하는 페이지
        '-' 를 누르면 팀원을 라인업에서 제외 시킨다.
        '+' 를 누르면 팀원 중에서 라인업을 추가할 수 있다.
        이때 새로운 팀원은 id가 있지 않기 때문에 id 를 제외하고 PUT 한다
        """
        self._game_team_player_service.change_lineup_player(game_team_id, request.data)
        return Response(status=status.HTTP_200_OK)