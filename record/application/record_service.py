from record.domain import RecordRepository, Record
from record.serializers import RecordRequestSerializer
from game.domain import GameRepository, GameTeam

class RecordService:
    def __init__(self, record_repository: RecordRepository, game_repository: GameRepository):
        self._record_repository = record_repository
        self._game_repository = game_repository

    def create_record(self, game_id: int, request_data):
        record_request_serializer = RecordRequestSerializer(data=request_data)
        record_request_serializer.is_valid(raise_exception=True)
        record_data: dict = record_request_serializer.validated_data

        game_team_id: int = record_data.get('game_team_id')
        game_team: GameTeam = self._game_repository.find_game_team_by_id(game_team_id)
        game_team.score += record_data.get('score')
        self._game_repository.save_game_team(game_team)

        new_record = Record(
            game_id=game_id,
            game_team_id=record_data.get('game_team_id'),
            game_team_player_id=record_data.get('game_team_player_id'),
            score=record_data.get('score'),
            scored_quarter_id=record_data.get('quarter_id')
        )
        self._record_repository.save_record(new_record)
        