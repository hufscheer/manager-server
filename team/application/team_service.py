from team.domain import TeamRepository
from accounts.domain import Member
from django.core.exceptions import PermissionDenied
from team.serializers import TeamRegisterRequestSerializer, TeamChangeRequestSerializer, TeamSaveSerializer
from utils.upload_to_s3 import upload_to_s3
from team.domain import Team
from league.domain import League, LeagueRepository

class TeamService:
    def __init__(self, team_repository: TeamRepository, league_repository: LeagueRepository, *args, **kwargs):
        self._team_repository = team_repository
        self._league_repository = league_repository

    def register_teams(self, request_data, league_id: int, user_data: Member):
        league: League = self._league_repository.find_league_by_id(league_id)
        teams_data_serializer = TeamRegisterRequestSerializer(data=request_data)
        teams_data_serializer.is_valid(raise_exception=True)
        team_data = teams_data_serializer.validated_data
        team_name = team_data.get('name')[0]
        team_logo = team_data.get('logo')[0]
        logo_url = upload_to_s3(image_data=team_logo, team_name=team_name, league_name=league.name)
        new_team = Team(name=team_name, logo_image_url=logo_url, league=league, administrator=user_data, organization=user_data.organization)
        self._team_repository.save_team(new_team)
        
    def change_team(self, request_data, team_id: int, user_data: Member):
        team: Team = self._team_repository.find_team_with_league_by_id(team_id)
        if team.administrator.id != user_data.id:
            raise PermissionDenied
        team_change_request_serializer = TeamChangeRequestSerializer(data=request_data)
        team_change_request_serializer.is_valid(raise_exception=True)
        team_change_data = team_change_request_serializer.validated_data
        team_name = team_change_data.get('names')[0]
        team_logo = team_change_data.get('logos')[0]
        logo_url = upload_to_s3(image_data=team_logo, team_name=team_name, league_name=team.league.name)
    
        team_save_serialzier = TeamSaveSerializer(team, data={'name': team_name, 'logo_image_url': logo_url, 'administrator': user_data.id}, partial=True)
        team_save_serialzier.is_valid(raise_exception=True)
        team_save_serialzier.save()