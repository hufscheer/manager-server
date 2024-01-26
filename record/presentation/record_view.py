from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.domain import IsAdminUser
from record.containers import RecordContainer
from drf_yasg.utils import swagger_auto_schema
from record.serializers import RecordRequestSerializer

class RecordView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._record_service = RecordContainer.record_service()

    @swagger_auto_schema(request_body=RecordRequestSerializer, responses={"201": ""})
    def post(self, request, game_id: int):
        """
        타임 라인 생성 API
        """
        self._record_service.create_record(game_id, request.data)
        return Response(status=status.HTTP_201_CREATED)