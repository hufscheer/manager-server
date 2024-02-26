import pytest
from .fixture import load_sql_fixture
from team.containers import TeamContainer
import os
from django.http import Http404

class TestTeamGet:

    @pytest.fixture
    def dependency_fixture(self):
        self._team_player_get_service = TeamContainer.team_player_get_service()
        self._team_get_service = TeamContainer.team_get_service()

    @pytest.mark.django_db
    def test_get_all_teams(self, dependency_fixture, load_sql_fixture):
        response1 = self._team_get_service.get_all_teams(1)
        response2 = self._team_get_service.get_all_teams(2)
        assert len(response1) == 4
        assert len(response2) == 1
        assert response1[0].get('name') == '미컴과'
        assert response2[0].get('name') == '터키어과'

    @pytest.mark.django_db
    def test_get_all_team_player(self, dependency_fixture, load_sql_fixture):
        response1 = self._team_player_get_service.get_all_team_player(1)
        response2 = self._team_player_get_service.get_all_team_player(4)
        assert len(response1) == 4
        assert len(response2) == 2

        with pytest.raises(Http404):
            self._team_player_get_service.get_all_team_player(5)