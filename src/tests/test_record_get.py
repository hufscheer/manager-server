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
        self._record_get_service = RecordContainer.record_get_service()

    @pytest.mark.django_db
    def test_get_record(self, load_sql_fixture, dependency_fixture):
        result = self._record_get_service.get_record_detail(3)

        assert result["recordInfo"]["game"] == 3
        assert result["recordInfo"]["gameTeam"]["gameTeamId"] == 6
        assert result["recordInfo"]["gameTeam"]["gameTeamName"] == "인도어과"
        assert result["recordInfo"]["recordedQuarter"]["id"] == 2
        assert result["recordInfo"]["recordedQuarter"]["name"] == "후반전"
        assert result["recordInfo"]["recordedAt"] == 3
        assert result["recordInfo"]["recordType"] == "REPLACEMENT"

        assert result["originLineupPlayer"]["id"] == 11
        assert result["originLineupPlayer"]["name"] == "인도선수1"
        assert result["originLineupPlayer"]["number"] == 22

        assert result["replacedLineupPlayer"]["id"] == 12
        assert result["replacedLineupPlayer"]["name"] == "인도선수2"
        assert result["replacedLineupPlayer"]["number"] == 44
       