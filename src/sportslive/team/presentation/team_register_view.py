from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.core.exceptions import PermissionDenied
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.domain import IsAdminUser
from team.containers import TeamContainer
from drf_yasg.utils import swagger_auto_schema
from team.serializers import TeamRegisterResponseSerializer

class TeamRegisterView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._team_register_service = TeamContainer.team_register_service()
    
    @swagger_auto_schema(responses={"201": TeamRegisterResponseSerializer})
    def post(self, request, league_id: int):
        """
        리그팀 등록 API 입니다.
        {
	        "names": ['팬돌이', '피카츄', '최강팀'],
	        "logos": ['팬돌이.png', '피카츄.png', '최강.png']
        }
        순서에 맞게 보내져야 합니다. 해당 API는 자세한 설명이 필요합니다.
        """
        response = self._team_register_service.register_teams(request_data=request.data, league_id=league_id, user_data=request.user)
        return Response(response, status=status.HTTP_201_CREATED)
