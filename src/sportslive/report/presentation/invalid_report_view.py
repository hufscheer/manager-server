from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.domain import IsAdminUser
from report.containers import ReportContainer
from drf_yasg.utils import swagger_auto_schema

class InvalidReportView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._report_service = ReportContainer.report_service()

    @swagger_auto_schema(responses={"200": ""})
    def post(self, request, report_id: int):
        """
        상태가 PENDING 신고 중에서 허위 신고를 Invalid 상태로 변경시키는 api
        """
        response = self._report_service.make_report_invalid(report_id)
        return Response(response, status=status.HTTP_200_OK)