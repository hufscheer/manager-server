import pytest
from accounts.domain.member import Member
from .fixture import load_sql_fixture
from team.containers import TeamContainer
from team.domain import LeagueTeam
import os
from django.core.files.images import ImageFile
from utils.exceptions.team_exceptions import S3UploadError, TeamSaveError, EmptyLogoError
class TestTeam:

    @pytest.fixture
    def dependency_fixture(self):
        self._test_team_register_service = TeamContainer.test_team_register_service()

    @pytest.fixture
    def image_data_fixture(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.img_data1 = ImageFile(open(os.path.join(dir_path, 'resources/첫번째팀.png'), 'rb'))
        self.img_data2 = ImageFile(open(os.path.join(dir_path, 'resources/두번째팀.png'), 'rb'))
        self.img_data3 = ImageFile(open(os.path.join(dir_path, 'resources/세번째팀.png'), 'rb'))

    @pytest.mark.django_db
    def test_register_teams(self, load_sql_fixture, dependency_fixture, image_data_fixture):
        member = Member.objects.get(id=1)
        request_data = {
	        "names": ['첫번째팀', '두번째팀', '세번째팀'],
	        "logos": [self.img_data1, self.img_data2, self.img_data3]
        }
        self._test_team_register_service.register_teams(request_data, 1, member)
        assert LeagueTeam.objects.get(name='첫번째팀').logo_image_url == "https://hufscheer-server.s3.ap-northeast-2.amazonaws.com/외대 월드컵/첫번째팀.png"
        assert LeagueTeam.objects.get(name='두번째팀').logo_image_url == "https://hufscheer-server.s3.ap-northeast-2.amazonaws.com/외대 월드컵/두번째팀.png"

    @pytest.mark.django_db
    def test_fail_register_teams1(self, load_sql_fixture, dependency_fixture, image_data_fixture):
        """
        팀 하나가 로고가 없을 때
        """
        member = Member.objects.get(id=1)
        request_data = {
	        "names": ['첫번째팀', '두번째팀', '세번째팀', '네번째팀'],
	        "logos": [self.img_data1, self.img_data2, self.img_data3]
        }
        with pytest.raises(TeamSaveError):
            self._test_team_register_service.register_teams(request_data, 1, member)

    @pytest.mark.django_db
    def test_fail_register_teams2(self, load_sql_fixture, dependency_fixture, image_data_fixture):
        """
        팀 하나가 로고가 누락됐을 때
        """
        member = Member.objects.get(id=1)
        request_data = {
	        "names": ['첫번째팀', '두번째팀', '세번째팀', '네번째팀'],
	        "logos": [self.img_data1, self.img_data2, self.img_data3, ""]
        }
        with pytest.raises(EmptyLogoError):
            self._test_team_register_service.register_teams(request_data, 1, member)
        
        