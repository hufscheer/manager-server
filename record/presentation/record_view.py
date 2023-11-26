from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.domain import IsAdminUser
from record.containers import RecordContainer

class RecordView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._record_service = RecordContainer.record_service()

    def post(self, request, game_id: int):
        self._record_service.create_record(game_id, request.data)
        return Response(status=status.HTTP_201_CREATED)