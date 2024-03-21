from django.shortcuts import get_object_or_404
from record.domain import Record, ReplacementRecord, ScoreRecord
from typing import Union

class RecordRepository:
    def save_record(self, record: Union[Record, ReplacementRecord, ScoreRecord]):
        record.save()

    def find_record_by_id(self, record_id: int):
        return get_object_or_404(Record, id=record_id)

    def find_record_by_id_with_game_team(self, record_id: int):
        return get_object_or_404(Record.objects.select_related('game_team'), id=record_id)

    def find_score_record_by_record_id(self, record_id: int):
        return get_object_or_404(ScoreRecord, record_id=record_id)
    
    def find_replacement_record_by_record_id(self, record_id: int):
        return get_object_or_404(ReplacementRecord, record_id=record_id)
    
    def delete_record(self, record: Union[Record, ReplacementRecord, ScoreRecord]):
        return record.delete()
    
    def find_score_record_by_record_id_with_record_quarter_and_league_team(self, record_id: int):
        return get_object_or_404(
            ScoreRecord.objects.select_related('record', 'record__recorded_quarter', 'record__game_team__league_team'),
            record_id=record_id
        )
    
    def find_replacement_record_by_record_id_with_record_quarter_and_league_team(self, record_id: int):
        return get_object_or_404(
            ReplacementRecord.objects.select_related('record', 'record__recorded_quarter', 'record__game_team__league_team'),
            record_id=record_id
        )