from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.domain import IsAdminUser
from report.containers import ReportContainer
from drf_yasg.utils import swagger_auto_schema

class BlockCheerTalkView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._report_service = ReportContainer.report_service()

    @swagger_auto_schema(responses={"200": ""})
    def post(self, request, cheer_talk_id: int):
        """
        응원톡 블럭 API
        """
        response = self._report_service.block_cheer_talk(cheer_talk_id)
        return Response(response, status=status.HTTP_200_OK)