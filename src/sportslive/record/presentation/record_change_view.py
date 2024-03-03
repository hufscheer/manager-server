from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.domain import IsAdminUser
from record.containers import RecordContainer
from drf_yasg.utils import swagger_auto_schema

class RecordChangeView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._record_service = RecordContainer.record_service()

    @swagger_auto_schema(responses={"200": ""})
    def put(self, request, record_id: int, extra_record_id: int, record_type: str):
        """
        타임 라인 수정 API
        record type이 "score" 일 경우:
        {
            "gameTeamId": int,
            "recordedAt": int,
            "recordedQuarterId": int,
            "scoreLineupPlayerId": int,
            "recordedQuarterId": int,
            "score": int
        }
        record type이 "replacement" 일 경우:
        {
            "gameTeamId": int,
            "recordedAt": int,
            "recordedQuarterId": int,
            "originLineupPlayerId": int,
            "recordedQuarterId": int,
            "replacedLineupPlayerId": int
        }
        """
        self._record_service.change_record(record_id, extra_record_id, record_type, request.data)
        return Response(status=status.HTTP_201_CREATED)