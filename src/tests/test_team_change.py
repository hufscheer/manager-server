import pytest
from accounts.domain.member import Member
from .fixture import load_sql_fixture
from team.containers import TeamContainer
from team.domain import LeagueTeam
import os
from django.core.files.images import ImageFile
from django.core.exceptions import PermissionDenied, ValidationError
class TestTeam:

    @pytest.fixture
    def dependency_fixture(self):
        self._test_team_service = TeamContainer.test_team_service()

    @pytest.fixture
    def image_data_fixture(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.img_data = ImageFile(open(os.path.join(dir_path, 'resources/두번째팀.png'), 'rb'))

    @pytest.mark.django_db
    def test_change_teams(self, load_sql_fixture, dependency_fixture, image_data_fixture):
        member = Member.objects.get(id=1)
        request_data = {
	        "name": ['바꾼팀'],
	        "logo": [self.img_data]
        }
        self._test_team_service.change_team(request_data, 1, member)
        assert LeagueTeam.objects.get(id=1).logo_image_url == "https://hufscheer-server.s3.ap-northeast-2.amazonaws.com/외대 월드컵/바꾼팀.png"
        assert LeagueTeam.objects.get(id=1).name == "바꾼팀"

    @pytest.mark.django_db
    def test_fail_change_teams1(self, load_sql_fixture, dependency_fixture, image_data_fixture):
        """
        테스트를 만든 사람이 아닐 때
        """
        member = Member.objects.get(id=2)
        request_data = {
	        "name": ['바꾼팀'],
	        "logo": [self.img_data]
        }
        with pytest.raises(PermissionDenied):
            self._test_team_service.change_team(request_data, 1, member)