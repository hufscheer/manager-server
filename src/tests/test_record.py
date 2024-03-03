import pytest
from accounts.domain.member import Member
from .fixture import load_sql_fixture
from record.containers import RecordContainer
from record.domain import Record, ScoreRecord, ReplacementRecord
from utils.exceptions.record_exception import NotValidRecordTypeError

class TestRecord:

    @pytest.fixture
    def dependency_fixture(self):
        self._record_create_service = RecordContainer.record_create_service()

    @pytest.mark.django_db
    def test_create_score_record(self, load_sql_fixture, dependency_fixture):
        request_data = {
            "recordedAt": '2024-03-22 14:07:24',
            "gameTeamId": 5,
            "scoreLineupPlayerId": 9,
            "recordedQuarterId": 1,
            "score": 1
        }
        self._record_create_service.create_record(3, 'score', request_data)
        print(Record.objects.get(id=1).recorded_at)
        assert Record.objects.filter().order_by('-id').first().recorded_quarter_id == 1
        assert Record.objects.filter().order_by('-id').first().recorded_at == 17
        assert ScoreRecord.objects.filter().order_by('-id').first().score == 1

    @pytest.mark.django_db
    def test_create_replacement_record(self, load_sql_fixture, dependency_fixture):
        request_data = {
            "recordedAt": '2024-03-22 14:50:24',
            "gameTeamId": 5,
            "recordedQuarterId": 2,
            "originLineupPlayerId": 9,
            "replacedLineupPlayerId": 10
        }
        self._record_create_service.create_record(3, 'replacement', request_data)

        assert Record.objects.filter().order_by('-id').first().recorded_quarter_id == 2
        assert ReplacementRecord.objects.filter().order_by('-id').first().origin_lineup_player_id == 9
        assert ReplacementRecord.objects.filter().order_by('-id').first().replaced_lineup_player_id == 10

    @pytest.mark.django_db
    def test_invalid_record_type(self, load_sql_fixture, dependency_fixture):
        request_data = {
        }
        with pytest.raises(NotValidRecordTypeError):
            assert self._record_create_service.create_record(3, 'unknown', request_data)