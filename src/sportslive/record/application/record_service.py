from record.domain import RecordRepository, Record, ScoreRecord, ReplacementRecord
from record.serializers import ScoreRecordChangeRequestSerializer, ReplacementRecordChangeRequestSerializer
from game.domain import GameRepository, GameTeam
from utils.exceptions.record_exception import NotValidRecordTypeError

class RecordService:
    def __init__(self, record_repository: RecordRepository, game_repository: GameRepository):
        self._record_repository = record_repository
        self._game_repository = game_repository

    def change_record(self, record_id: int, extra_record_id: int, record_type: str, request_data):
        record_type_serializer_mapping = {
            "score": ScoreRecordChangeRequestSerializer,
            "replacement": ReplacementRecordChangeRequestSerializer
        }
        record_request_serializer = record_type_serializer_mapping.get(record_type, None)
        if not record_request_serializer:
            raise NotValidRecordTypeError

        serializer = record_request_serializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        record_data: dict = serializer.validated_data
        game_team_id: int = record_data.get('game_team_id')
        game_team: GameTeam = self._game_repository.find_game_team_by_id(game_team_id)

        target_record: Record = self._record_repository.find_record_by_id(record_id)
        self._change_and_save_record_object(record_data, target_record)

        if record_type == "score":
            self._change_and_save_score_record_object(game_team, extra_record_id, record_data)
        elif record_type == "replacement":
            self._change_and_save_replacement_record_object(extra_record_id, record_data)

    def _change_and_save_record_object(self, record_data: dict, target_record: Record):
        target_record.game_team_id = record_data.get('game_team_id')
        target_record.recorded_at = record_data.get('recorded_at')
        target_record.recorded_quarter_id = record_data.get('recorded_quarter_id')
        self._record_repository.save_record(target_record)

    def _change_and_save_score_record_object(self, game_team: GameTeam, extra_record_id: int, record_data: dict):
        target_score_record: ScoreRecord = self._record_repository.find_score_record_by_id(extra_record_id)
        target_score_record.lineup_player_id = record_data.get('score_lineup_player_id')

        score = record_data.get('score')
        self._change_game_team_score(game_team, target_score_record, score)
        target_score_record.score = score
        self._record_repository.save_record(target_score_record)

    def _change_and_save_replacement_record_object(self, extra_record_id: int, record_data: dict):
        target_replacement_record: ReplacementRecord = self._record_repository.find_replacement_record_by_id(extra_record_id)
        target_replacement_record.origin_lineup_player_id = record_data.get('origin_lineup_player_id')
        target_replacement_record.replaced_lineup_player_id = record_data.get('replaced_lineup_player_id')
        self._record_repository.save_record(target_replacement_record)

    def _change_game_team_score(self, game_team: GameTeam, target_score_record: ScoreRecord, score: int):
        game_team.score -= target_score_record.score
        game_team.score += score
        self._game_repository.save_game_team(game_team)