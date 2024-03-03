import pytest
from accounts.domain.member import Member
from .fixture import load_sql_fixture
from record.containers import RecordContainer
from record.domain import Record, ScoreRecord, ReplacementRecord
from game.domain import GameTeam
from utils.exceptions.record_exception import NotValidRecordTypeError

class TestRecord:

    @pytest.fixture
    def dependency_fixture(self):
        self._record_create_service = RecordContainer.record_create_service()
        self._record_service = RecordContainer.record_service()

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

        assert Record.objects.filter().order_by('-id').first().recorded_quarter_id == 1
        assert Record.objects.filter().order_by('-id').first().recorded_at == 17
        assert ScoreRecord.objects.filter().order_by('-id').first().score == 1
        assert GameTeam.objects.get(id=5).score == 3

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

    @pytest.mark.django_db
    def test_change_score_record1(self, load_sql_fixture, dependency_fixture):
        """
        record 1과 score_record 1의 recored_at과 recorded_quarter_id를 수정한다.
        """
        request_data = {
            "recordedAt": 2,
            "gameTeamId": 5,
            "recordedQuarterId": 2,
            "scoreLineupPlayerId": 9,
            "score": 1
        }
        self._record_service.change_record(1, 1, 'score', request_data)

        assert Record.objects.get(id=1).recorded_at == 2
        assert Record.objects.get(id=1).recorded_quarter_id == 2

    @pytest.mark.django_db
    def test_change_score_record2(self, load_sql_fixture, dependency_fixture):
        """
        record 1과 score_record 2의 score와 score_lineup_player_id를 수정한다.
        축구에 2점은 없지만, 테스트 용으로 2점으로 바꾸었다.
        """
        request_data = {
            "recordedAt": 2,
            "gameTeamId": 5,
            "recordedQuarterId": 2,
            "scoreLineupPlayerId": 10,
            "score": 2
        }
        self._record_service.change_record(1, 2, 'score', request_data)

        assert Record.objects.get(id=1).recorded_at == 2
        assert Record.objects.get(id=1).recorded_quarter_id == 2
        assert ScoreRecord.objects.get(id=2).lineup_player_id == 10
        assert GameTeam.objects.get(id=5).score == 3

    @pytest.mark.django_db
    def test_change_replacement_record(self, load_sql_fixture, dependency_fixture):
        """
        replacement_record 1을 수정한다.
        """
        request_data = {
            "gameTeamId": 6,
            "recordedAt": 3,
            "recordedQuarterId": 2,
            "originLineupPlayerId": 12,
            "recordedQuarterId": 2,
            "replacedLineupPlayerId": 11
        }
        self._record_service.change_record(3, 1, 'replacement', request_data)

        assert ReplacementRecord.objects.get(id=1).origin_lineup_player_id == 12
        assert ReplacementRecord.objects.get(id=1).replaced_lineup_player_id == 11

    @pytest.mark.django_db
    def test_delete_record(self, load_sql_fixture, dependency_fixture):
        """
        score 타임라인 하나를 삭제한다
        """
        self._record_service.delete_record(1, 1, 'score')
        self._record_service.delete_record(2, 2, 'score')

        assert Record.objects.filter(id=1).exists() == False
        assert ScoreRecord.objects.filter(id=1).exists() == False
        assert Record.objects.filter(id=2).exists() == False
        assert ScoreRecord.objects.filter(id=2).exists() == False
        assert GameTeam.objects.get(id=5).score == 0