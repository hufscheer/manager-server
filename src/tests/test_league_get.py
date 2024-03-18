import pytest
from accounts.domain.member import Member
from .fixture import load_sql_fixture
from league.containers import LeagueContainer
from league.domain import LeagueSport, League
from django.core.exceptions import PermissionDenied
from freezegun import freeze_time

class TestLeagueGet:

    @pytest.fixture
    def dependency_fixture(self):
        self._league_get_service = LeagueContainer.league_get_service()

    @pytest.mark.django_db
    @freeze_time("2024-03-18")
    def test_get_league_list(self, load_sql_fixture, dependency_fixture):
        member = Member.objects.get(id=1)
        response = self._league_get_service.get_leagues(member)
        assert len(response['scheduled']) == 2

    @pytest.mark.django_db
    @freeze_time("2024-03-21")
    def test_get_main_list(self, load_sql_fixture, dependency_fixture):
        member = Member.objects.get(id=1)
        response = self._league_get_service.get_main(member)
        assert len(response[0].get("playingGameData")) == 1
        
        