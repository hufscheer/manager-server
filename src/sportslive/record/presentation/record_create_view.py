from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.domain import IsAdminUser
from record.containers import RecordContainer
from drf_yasg.utils import swagger_auto_schema
from record.serializers import ScoreRecordRequestSerializer, ReplacementRecordRequestSerializer

class RecordCreateView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._record_service = RecordContainer.record_create_service()

    @swagger_auto_schema(responses={"201": ""})
    def post(self, request, game_id: int, record_type: str):
        """
        타임 라인 생성 API
        record type이 "score" 일 경우:
        {
            "gameTeamId": int,
            "recordedQuarterId": int,
            "scoreLineupPlayerId": int,
            "recordedQuarterId": int,
            "score": int,
            "recordedAt": datetime
        }
        record type이 "replacement" 일 경우:
        {
            "gameTeamId": int,
            "recordedQuarterId": int,
            "originLineupPlayerId": int,
            "recordedQuarterId": int,
            "replacedLineupPlayerId": int,
            "recordedAt": datetime
        }
        """
        self._record_service.create_record(game_id, record_type, request.data)
        return Response(status=status.HTTP_201_CREATED)