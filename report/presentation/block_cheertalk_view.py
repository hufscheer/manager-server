from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.domain import IsAdminUser
from report.containers import ReportContainer

class BlockCheerTalkView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._report_service = ReportContainer.report_service()

    def post(self, request, cheer_talk_id: int):
        response = self._report_service.block_cheer_talk(cheer_talk_id)
        return Response(response, status=status.HTTP_200_OK)