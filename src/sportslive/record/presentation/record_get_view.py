from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.domain import IsAdminUser
from record.containers import RecordContainer
from drf_yasg.utils import swagger_auto_schema

class RecordGetView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._record_get_service = RecordContainer.record_get_service()

    @swagger_auto_schema(responses={"200": ""})
    def get(self, request, record_id: int, record_type: str):
        response = self._record_get_service.get_record_detail(record_id)
        return Response(response, status=status.HTTP_200_OK)