import pytest
from accounts.domain.member import Member
from .fixture import load_sql_fixture
from league.containers import LeagueContainer
from league.domain import LeagueSport, League
from django.core.exceptions import PermissionDenied

class TestLeagueGet:

    @pytest.fixture
    def dependency_fixture(self):
        self._league_get_service = LeagueContainer.league_get_service()

    @pytest.mark.django_db
    def test_get_league_list(self, load_sql_fixture, dependency_fixture):
        member = Member.objects.get(id=1)
        response = self._league_get_service.get_leagues(member)
        assert response[0].get('name') == '외대 월드컵'
        assert response[1].get('name') == '아대 월드컵'
        
        