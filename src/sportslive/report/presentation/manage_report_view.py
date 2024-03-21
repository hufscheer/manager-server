from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.domain import IsAdminUser
from report.containers import ReportContainer
from drf_yasg.utils import swagger_auto_schema

class ManageReportView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._report_service = ReportContainer.report_service()

    @swagger_auto_schema(responses={"200": ""})
    def post(self, request, report_id: int):
        """
        PENDING 상태인 report를 VALID로 만들고 응원톡을 블럭하거나, VALID인 report를 PENDING으로 만들고 응원톡을 블럭 취소하는 API
        """
        response = self._report_service.manage_report_state_and_cheer_talk_state(report_id)
        return Response(response, status=status.HTTP_200_OK)