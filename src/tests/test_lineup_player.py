import pytest
from accounts.domain.member import Member
from .fixture import load_sql_fixture
from game.containers import GameContainer
from game.domain import LineupPlayer
from django.core.exceptions import PermissionDenied

class TestLineupPlayer:

    @pytest.fixture
    def dependency_fixture(self):
        self._lineup_player_service = GameContainer.lineup_player_service()

    @pytest.mark.django_db
    def test_register_lineup_player(self, load_sql_fixture, dependency_fixture):
        """
        미컴과에 결승전 라인업을 추가해본다.
        """
        member = Member.objects.get(id=1)
        request_data = [
            {
                "name": "미컴선수3",
                "number": 55,
                "isCaptain": 0,
                "leagueTeamPlayerId": 9
            },
            {
                "name": "미컴선수4",
                "number": 55,
                "description": "부상",
                "isCaptain": 0,
                "leagueTeamPlayerId": 10
            }
        ]
        self._lineup_player_service.register_lineup_player(5, request_data)
        assert LineupPlayer.objects.get(id=13).name == "미컴선수3"
        assert LineupPlayer.objects.get(id=14).name == "미컴선수4"
        assert LineupPlayer.objects.get(id=13).description == None
        assert LineupPlayer.objects.get(id=14).description == "부상"
        assert LineupPlayer.objects.get(id=13).league_team_player_id == 9
        assert LineupPlayer.objects.get(id=14).league_team_player_id == 10

    @pytest.mark.django_db
    def test_change_lineup_player(self, load_sql_fixture, dependency_fixture):
        """
        미컴과에 결승전 라인업을 변경해본다.
        미컴선수 3, 4를 라인업에 추가하고, 미컴선수2를 라인업에서 삭제하고 is_caption을 0으로 수정
        미컴선수1의 is_catain을 1로 수정한다.
        """
        member = Member.objects.get(id=1)
        request_data = [
            {
                "name": "미컴선수4",
                "number": 66,
                "isCaptain": 0,
                "leagueTeamPlayerId": 9
            },
            {
                "name": "미컴선수3",
                "number": 55,
                "isCaptain": 0,
                "leagueTeamPlayerId": 10
            },
            {
                "id": 9,
                "name": "미컴선수1",
                "number": 11,
                "isCaptain": 1,
                "leagueTeamPlayerId": 1
            }
        ]
        self._lineup_player_service.change_lineup_player(5, request_data)
        assert LineupPlayer.objects.filter(game_team_id=5).count() == 3
        assert LineupPlayer.objects.get(id=9).is_captain == 1