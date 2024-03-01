from record.domain import RecordRepository, Record, ScoreRecord, ReplacementRecord
from record.serializers import ScoreRecordRequestSerializer, ReplacementRecordRequestSerializer
from game.domain import GameRepository, GameTeam
from datetime import datetime
from utils.exceptions.record_exception import NotValidRecordTypeError

class RecordCreateService:
    def __init__(self, record_repository: RecordRepository, game_repository: GameRepository):
        self._record_repository = record_repository
        self._game_repository = game_repository

    def create_record(self, game_id: int, record_type: str, request_data):
        record_type_serializer_mapping = {
            "score": ScoreRecordRequestSerializer,
            "replacement": ReplacementRecordRequestSerializer
        }
        record_request_serializer = record_type_serializer_mapping.get(record_type, None)
        if not record_request_serializer:
            raise NotValidRecordTypeError

        serializer = record_request_serializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        record_data: dict = serializer.validated_data
        game_team_id: int = record_data.get('game_team_id')
        game_team: GameTeam = self._game_repository.find_game_team_by_id(game_team_id)

        new_record = self._create_and_save_record_object(game_team, record_data, game_id)

        if record_type == "score":
            self._create_and_save_score_record_object(game_team, new_record, record_data)
        elif record_type == "replacement":
            self._create_and_save_replacement_record_object(new_record, record_data)

    def _create_and_save_record_object(self, game_team: GameTeam, record_data, game_id) -> Record:
        recorded_quarter_id=record_data.get('recorded_quarter_id')
        new_record: Record = self._create_new_record_object(game_id, game_team, recorded_quarter_id, 'score')
        self._record_repository.save_record(new_record)
        return new_record
    
    def _create_and_save_score_record_object(self, game_team: GameTeam, new_record: Record, record_data):
        score = record_data.get('score')
        self._change_game_team_score(game_team, score)

        score_lineup_player_id = record_data.get('score_lineup_player_id')
        new_score_record = self._create_score_record_object(new_record, score_lineup_player_id, score)
        self._record_repository.save_record(new_score_record)

    def _create_and_save_replacement_record_object(self, new_record: Record, record_data):
        origin_lineup_player_id = record_data.get('origin_lineup_player_id')
        replaced_lineup_player_id = record_data.get('replaced_lineup_player_id')
        new_replacement_record = self._create_replacement_record_object(new_record, origin_lineup_player_id, replaced_lineup_player_id)
        self._record_repository.save_record(new_replacement_record)
        
    def _change_game_team_score(self, game_team: GameTeam, score):
        game_team.score += score
        self._game_repository.save_game_team(game_team)
    
    def _create_new_record_object(self, game_id: int, game_team: GameTeam, recorded_quarter_id: int, record_type: str) -> Record:
        return Record(
            game_id=game_id,
            game_team=game_team,
            recorded_quarter_id=recorded_quarter_id,
            record_type=record_type,
            recorded_at=datetime.now()
        )
    
    def _create_score_record_object(self, record: Record, lineup_player_id: int, score: int) -> ScoreRecord:
        return ScoreRecord(
            record=record,
            lineup_player_id=lineup_player_id,
            score=score
        )
    
    def _create_replacement_record_object(self, record: Record, origin_lineup_player_id: int, replaced_lineup_player_id: int) -> ReplacementRecord:
        return ReplacementRecord(
            record=record,
            origin_lineup_player_id=origin_lineup_player_id,
            replaced_lineup_player_id=replaced_lineup_player_id
        )