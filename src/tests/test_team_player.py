import pytest
from accounts.domain.member import Member
from .fixture import load_sql_fixture
from team.containers import TeamContainer
from team.domain import LeagueTeamPlayer, LeagueTeam
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from django.http import Http404

class TestLeagueTeamPlayer:

    @pytest.fixture
    def dependency_fixture(self):
        self._team_player_service = TeamContainer.team_player_service()

    @pytest.mark.django_db
    def test_register_team_players(self, load_sql_fixture, dependency_fixture):
        member = Member.objects.get(id=1)
        request_data = [
            {
                "name": "미컴선수3",
                "number": 3
            },
            {
                "name": "미컴선수4",
                "number": 4
            },
            {
                "name": "미컴선수5",
                "number": 5
            },
        ]
        self._team_player_service.register_team_players(request_data, 1)
        assert LeagueTeamPlayer.objects.filter(league_team_id=1).count() == 7

    @pytest.mark.django_db
    def test_change_team_players(self, load_sql_fixture, dependency_fixture):
        member = Member.objects.get(id=1)
        request_data = {
            "name": "바꾼 미컴 선수",
            "description": "추가 설명",
            "number": 999
        }
        self._team_player_service.change_team_player(request_data, 1)
        assert LeagueTeamPlayer.objects.get(id=1).name == "바꾼 미컴 선수"
        assert LeagueTeamPlayer.objects.get(id=1).description == "추가 설명"
        assert LeagueTeamPlayer.objects.get(id=1).number == 999

    @pytest.mark.django_db
    def test_delete_team_players(self, load_sql_fixture, dependency_fixture):
        member = Member.objects.get(id=1)
        self._team_player_service.delete_team_player(1, member)
        with pytest.raises(Http404):
            get_object_or_404(LeagueTeamPlayer, id=1)

    @pytest.mark.django_db
    def test_fail_delete_team_players(self, load_sql_fixture, dependency_fixture):
        member = Member.objects.get(id=3)
        with pytest.raises(PermissionDenied):
            self._team_player_service.delete_team_player(1, member)
    
        
        