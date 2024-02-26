import pytest
from accounts.domain.member import Member
from .fixture import load_sql_fixture
from game.containers import GameContainer
from game.domain import Game, GameTeam
from django.core.exceptions import PermissionDenied

class TestGame:

    @pytest.fixture
    def dependency_fixture(self):
        self._game_service = GameContainer.game_service()
        self._game_team_get_serivice = GameContainer.game_team_get_serivice()

    @pytest.mark.django_db
    def test_get_game_info(self, load_sql_fixture, dependency_fixture):
        response = self._game_service.get_game_info(1)
        assert response.get('gameName') == '준결승'

    @pytest.mark.django_db
    def test_get_game_teams_info(self, load_sql_fixture, dependency_fixture):
        response = self._game_team_get_serivice.get_game_teams_info(1)
        assert len(response) == 2

    @pytest.mark.django_db
    def test_create_game(self, load_sql_fixture, dependency_fixture):
        member = Member.objects.get(id=1)
        request_data = {
            "sportsId": 1,
            "startTime": "2024-03-22 14:00:00",
            "name": "3위결정전",
            "teamIds": [
                2, 3
            ]
        }
        self._game_service.create_game(1, request_data, member)
        assert Game.objects.get(id=4).name == "3위결정전"
        assert Game.objects.get(id=4).video_id == None
        assert Game.objects.get(id=4).game_quarter == "시작 전"
        assert Game.objects.get(id=4).state == "SCHEDULED"
        assert GameTeam.objects.filter(id=7).exists()
        assert GameTeam.objects.filter(id=8).exists()

    @pytest.mark.django_db
    def test_change_game(self, load_sql_fixture, dependency_fixture):
        """
        결승전 바꿔보기
        """
        member = Member.objects.get(id=1)
        request_data = {
            "sportsId": 1,
            "startTime": "2024-03-22 14:00:00",
            "gameName": "결승",
            "videoId": "video.com",
            "gameQuarter": "전반전",
            "state": "PLAYING"
        }
        self._game_service.change_game(3, request_data, member)
        assert Game.objects.get(id=3).name == "결승"
        assert Game.objects.get(id=3).game_quarter == "전반전"
        assert Game.objects.get(id=3).state == "PLAYING"

    @pytest.mark.django_db
    def test_fail_change_game(self, load_sql_fixture, dependency_fixture):
        """
        결승전 바꾸기 실패
        """
        member = Member.objects.get(id=2)
        request_data = {
            "sportsId": 1,
            "startTime": "2024-03-22 14:00:00",
            "gameName": "결승",
            "videoId": "video.com",
            "gameQuarter": "전반전",
            "state": "PLAYING"
        }
        with pytest.raises(PermissionDenied):
            self._game_service.change_game(3, request_data, member)