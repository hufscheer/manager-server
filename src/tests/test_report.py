import pytest
from accounts.domain.member import Member
from .fixture import load_sql_fixture
from report.containers import ReportContainer
from report.domain import Report, CheerTalk
from django.core.exceptions import PermissionDenied
import json

class TestReport:

    @pytest.fixture
    def dependency_fixture(self):
        self._report_service = ReportContainer.report_service()

    @pytest.mark.django_db
    def test_get_report_info(self, load_sql_fixture, dependency_fixture):
        member = Member.objects.get(id=1)
        response = self._report_service.get_report_info(member)
        
        assert 'pending' in response
        assert 'isBlocked' in response
        assert response['pending'][0]['gameInfo']['leagueName'] == '외대 월드컵'
        assert response['pending'][0]['reportInfo']['cheerTalkId'] == 4
        assert response['pending'][0]['reportInfo']['reportId'] == 2
        
        assert response['isBlocked'][0]['gameInfo']['leagueName'] == '외대 월드컵'
        assert response['isBlocked'][0]['reportInfo']['cheerTalkId'] == 2

    @pytest.mark.django_db
    def test_block_cheer_talk(self, load_sql_fixture, dependency_fixture):
        member = Member.objects.get(id=1)
        self._report_service.block_cheer_talk(1)
        self._report_service.block_cheer_talk(2)
        assert CheerTalk.objects.get(id=1).is_blocked == True

    @pytest.mark.django_db
    def test_invalid_report(self, load_sql_fixture, dependency_fixture):
        self._report_service.make_report_invalid(2)
        assert Report.objects.get(id=2).state == 'INVALID'