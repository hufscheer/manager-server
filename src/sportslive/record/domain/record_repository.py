from django.shortcuts import get_object_or_404
from record.domain import Record, ReplacementRecord, ScoreRecord

class RecordRepository:
    def save_record(self, record: Record):
        record.save()

    def find_record_by_id(self, record_id: int):
        return get_object_or_404(Record, id=record_id)

    def find_record_by_id_with_game_team(self, record_id: int):
        return get_object_or_404(Record.objects.select_related('game_team'), id=record_id)

    def find_score_record_by_id(self, score_record_id: int):
        return get_object_or_404(ScoreRecord, id=score_record_id)
    
    def find_replacement_record_by_id(self, replaement_record_id: int):
        return get_object_or_404(ReplacementRecord, id=replaement_record_id)