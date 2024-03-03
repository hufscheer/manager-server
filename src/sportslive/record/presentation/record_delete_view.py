from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.domain import IsAdminUser
from record.containers import RecordContainer
from drf_yasg.utils import swagger_auto_schema

class RecordDeleteView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._record_service = RecordContainer.record_service()

    @swagger_auto_schema(responses={"204": ""})
    def put(self, request, record_id: int, extra_record_id: int, record_type: str):
        """
        타임 라인 삭제 API
        """
        self._record_service.delete_record(record_id, extra_record_id, record_type)
        return Response(status=status.HTTP_204_NO_CONTENT)