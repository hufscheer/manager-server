import pytest
from accounts.domain.member import Member
from .fixture import load_sql_fixture
from game.containers import GameContainer
from game.domain import Game, GameTeam
from utils.exceptions.game_exceptions import CantDeleteGameError, CantParsingYoutubeUrl
from django.core.exceptions import PermissionDenied
class TestGame:

    @pytest.fixture
    def dependency_fixture(self):
        self._game_service = GameContainer.game_service()

    @pytest.mark.django_db
    def test_create_game1(self, load_sql_fixture, dependency_fixture):
        member = Member.objects.get(id=1)
        request_data = {
            "sportsId": 1,
            "startTime": "2024-03-22 14:00:00",
            "gameName": "1경기",
            "teamIds": [
                2, 3
            ],
            "round": 16
        }
        self._game_service.create_game(1, request_data, member)
        assert Game.objects.get(id=5).name == "1경기"
        assert Game.objects.get(id=5).video_id == None
        assert Game.objects.get(id=5).game_quarter == "시작 전"
        assert Game.objects.get(id=5).state == "SCHEDULED"
        assert Game.objects.get(id=5).round == 16
        assert GameTeam.objects.filter(id=7).exists()
        assert GameTeam.objects.filter(id=8).exists()
    
    @pytest.mark.django_db
    def test_create_game2(self, load_sql_fixture, dependency_fixture):
        member = Member.objects.get(id=1)
        request_data = {
            "sportsId": 1,
            "startTime": "2024-03-22 14:00:00",
            "gameName": "1경기",
            "videoId": "https://youtu.be/yE0MWJN6KCU?si=Z_EQc0VbbQwSdmVk",
            "teamIds": [
                2, 3
            ],
            "round": 16
        }
        self._game_service.create_game(1, request_data, member)
        assert Game.objects.get(id=5).name == "1경기"
        assert Game.objects.get(id=5).game_quarter == "시작 전"
        assert Game.objects.get(id=5).state == "SCHEDULED"
        assert Game.objects.get(id=5).video_id == "yE0MWJN6KCU"
        assert Game.objects.get(id=5).round == 16
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
            "videoId": "https://www.youtube.com/watch?v=ZTcCqJU_9qs",
            "gameQuarter": "후반전",
            "state": "FINISHED",
            "round": 2
        }
        self._game_service.change_game(3, request_data, member)
        assert Game.objects.get(id=3).name == "결승"
        assert Game.objects.get(id=3).game_quarter == "후반전"
        assert Game.objects.get(id=3).state == "FINISHED"
        assert Game.objects.get(id=3).video_id == "ZTcCqJU_9qs"

    @pytest.mark.django_db
    def test_fail_change_game1(self, load_sql_fixture, dependency_fixture):
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

    @pytest.mark.django_db
    def test_fail_change_game2(self, load_sql_fixture, dependency_fixture):
        """
        결승전 바꾸기 실패2 (유튜브 url)
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
        with pytest.raises(CantParsingYoutubeUrl):
            self._game_service.change_game(3, request_data, member)

    @pytest.mark.django_db
    def test_delete_game(self, load_sql_fixture, dependency_fixture):
        """
        게임 삭제
        """
        member = Member.objects.get(id=1)
        self._game_service.delete_game(4, member)
        assert Game.objects.filter(id=4).exists() == False
        assert GameTeam.objects.filter(game_id=4).exists() == False
    
    @pytest.mark.django_db
    def test_fail_delete_game(self, load_sql_fixture, dependency_fixture):
        """
        게임 삭제
        """
        member = Member.objects.get(id=1)
        with pytest.raises(CantDeleteGameError):
            self._game_service.delete_game(1, member)
        