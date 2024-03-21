from record.domain import RecordRepository, Record, ScoreRecord, ReplacementRecord
from record.serializers import ScoreRecordResponseSerializer, ReplacementRecordResponseSerializer
from game.domain import GameRepository
from utils.exceptions.record_exception import NotValidRecordTypeError

class RecordGetService:
    def __init__(self, record_repository: RecordRepository, game_repository: GameRepository):
        self._record_repository = record_repository
        self._game_repository = game_repository

    def get_record_detail(self, record_id: int):
        record: Record = self._record_repository.find_record_by_id(record_id)
        if record.record_type == 'SCORE':
            score_record: ScoreRecord = self._record_repository.find_score_record_by_record_id_with_fetch_join(record_id)
            return ScoreRecordResponseSerializer(score_record).data
        elif record.record_type == 'REPLACEMENT':
            replacement_record: ReplacementRecord = self._record_repository.find_replacement_record_by_record_id_with_fetch_join(record_id)
            return ReplacementRecordResponseSerializer(replacement_record).data
        else:
            raise NotValidRecordTypeError