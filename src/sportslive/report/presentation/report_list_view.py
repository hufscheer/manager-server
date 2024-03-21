from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.domain import IsAdminUser
from report.containers import ReportContainer
from drf_yasg.utils import swagger_auto_schema
from report.serializers import ReportResponseSerializer

class ReportListView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._report_get_service = ReportContainer.report_get_service()

    @swagger_auto_schema(responses={"200": ReportResponseSerializer})
    def get(self, request):
        """
        신고 조회 API
        """
        response = self._report_get_service.get_report_info(request.user)
        return Response(response, status=status.HTTP_200_OK)