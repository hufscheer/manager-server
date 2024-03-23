import pytest
from accounts.domain.member import Member
from .fixture import load_sql_fixture
from league.containers import LeagueContainer
from league.domain import LeagueSport, League
from django.core.exceptions import PermissionDenied
from utils.exceptions.league_exception import CantEndAtFasterThanStartAt

class TestLeague:

    @pytest.fixture
    def dependency_fixture(self):
        self._league_service = LeagueContainer.league_service()

    @pytest.mark.django_db
    def test_create_league(self, load_sql_fixture, dependency_fixture):
        member = Member.objects.get(id=1)
        request_data = {
            "leagueData": {
                "name": "푸드파이터대회",
                "startAt": "2019-08-24T14:15:22Z",
                "endAt": "2019-08-24T14:15:22Z",
                "maxRound": 16,
                "inProgressRound": 16
            },
            "sportData": [
                1
            ]
        }
        response = self._league_service.register_league(request_data, member)
        assert response.get('leagueId') == 3
        assert LeagueSport.objects.get(league_id=3).sport_id == 1

    @pytest.mark.django_db
    def test_create_fail_league(self, load_sql_fixture, dependency_fixture):
        member = Member.objects.get(id=1)
        request_data = {
            "leagueData": {
                "name": "푸드파이터대회",
                "startAt": "2019-08-24T14:15:22Z",
                "endAt": "2019-08-24T14:13:22Z",
                "maxRound": 16,
                "inProgressRound": 16
            },
            "sportData": [
                1
            ]
        }
        with pytest.raises(CantEndAtFasterThanStartAt):
            self._league_service.register_league(request_data, member)

    @pytest.mark.django_db
    def test_change_league(self, load_sql_fixture, dependency_fixture):
        member = Member.objects.get(id=1)
        request_data = {
            "leagueData": {
                "name": "푸파대회",
                "startAt": "2024-03-20 00:00:00",
                "endAt": "2024-03-25 00:00:00",
                "maxRound": 32,
                "inProgressRound": 4
            },
            "sportData": [
                2
            ],
            "leagueId": 1
            }
    
        self._league_service.change_league(request_data, member)
        assert League.objects.get(id=1).name == "푸파대회"
        assert League.objects.get(id=1).max_round == 32
        assert League.objects.get(id=1).in_progress_round == 4
        assert LeagueSport.objects.get(league_id=1).sport_id == 2

    @pytest.mark.django_db
    def test_change_fail_league(self, load_sql_fixture, dependency_fixture):
        member = Member.objects.get(id=3)
        request_data = {
            "leagueData": {
                "name": "푸파대회",
                "startAt": "2024-03-20 00:00:00",
                "endAt": "2024-03-25 00:00:00",
                "maxRound": 32,
                "inProgressRound": 4
            },
            "sportData": [
                2
            ],
            "leagueId": 1
            }
        with pytest.raises(PermissionDenied):
            self._league_service.change_league(request_data, member)

    @pytest.mark.django_db
    def test_delete_league(self, load_sql_fixture, dependency_fixture):
        member = Member.objects.get(id=1)
        request_data = {
            "leagueId": 1
        }
        self._league_service.delete_league(request_data, member)
        assert League.objects.get(id=1).is_deleted == True

    @pytest.mark.django_db
    def test_cant_delete_league(self, load_sql_fixture, dependency_fixture):
        member = Member.objects.get(id=3)
        request_data = {
            "leagueId": 1
        }
        with pytest.raises(PermissionDenied):
            self._league_service.delete_league(request_data, member)
        
