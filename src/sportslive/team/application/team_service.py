from team.domain import TeamRepository
from accounts.domain import Member
from django.core.exceptions import PermissionDenied
from team.serializers import TeamChangeRequestSerializer, TeamSaveSerializer
from utils.s3 import AbstractS3Connect
from utils.sqs import AbstractSqsConnect
from team.domain import LeagueTeam

class TeamService:
    def __init__(self, team_repository: TeamRepository, s3_conn: AbstractS3Connect, sqs_conn: AbstractSqsConnect):
        self._team_repository = team_repository
        self._s3_conn = s3_conn
        self._sqs_conn = sqs_conn

    def change_team(self, request_data, team_id: int, user_data: Member):
        team: LeagueTeam = self._team_repository.find_team_with_league_by_id(team_id)
        if team.organization != user_data.organization:
            raise PermissionDenied
        team_change_request_serializer = TeamChangeRequestSerializer(data=request_data)
        team_change_request_serializer.is_valid(raise_exception=True)
        team_change_data = team_change_request_serializer.validated_data
    
        team_name = team_change_data.get('name')[0]
        team_logo = team_change_data.get('logo')[0]

        s3_key = self._s3_conn.make_s3_key(image_data=team_logo, team_name=team_name, league_name=team.league.name)
        logo_url = self._s3_conn.upload_to_s3(image_data=team_logo, team_name=team_name, league_name=team.league.name)

        team.name = team_name
        team.logo_image_url = logo_url
        self._team_repository.save_team(team)
        self._sqs_conn.send_message_to_sqs(s3_key)

    def _send_sqs_message(self, s3_key):
        sqs_conn = self._sqs_conn
        sqs_conn.send_message_to_sqs(s3_key)

    class _TeamDto:
        def __init__(self, name: str, logo_image_url: str):
            self.name = name
            self.logo_image_url = logo_image_url
