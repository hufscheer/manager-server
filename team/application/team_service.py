from team.domain import TeamRepository
from accounts.domain import Member
from django.core.exceptions import PermissionDenied
from team.serializers import TeamChangeRequestSerializer, TeamSaveSerializer
from utils import S3Connect
from team.domain import Team

class TeamService:
    def __init__(self, team_repository: TeamRepository, *args, **kwargs):
        self._team_repository = team_repository
        self._s3_conn = S3Connect()

    def change_team(self, request_data, team_id: int, user_data: Member):
        team: Team = self._team_repository.find_team_with_league_by_id(team_id)
        if team.administrator.id != user_data.id:
            raise PermissionDenied
        team_change_request_serializer = TeamChangeRequestSerializer(data=request_data)
        team_change_request_serializer.is_valid(raise_exception=True)
        team_change_data = team_change_request_serializer.validated_data
        team_name = team_change_data.get('names')[0]
        team_logo = team_change_data.get('logos')[0]

        logo_url = self._s3_conn.upload_to_s3(image_data=team_logo, team_name=team_name, league_name=team.league.name)
    
        team_save_serialzier = TeamSaveSerializer(team, data=self._TeamDto(team_name, logo_url), partial=True)
        team_save_serialzier.is_valid(raise_exception=True)
        team_save_serialzier.save()

    class _TeamDto:
        def __init__(self, name: str, logo_image_url: str):
            self.name = name
            self.logo_image_url = logo_image_url
