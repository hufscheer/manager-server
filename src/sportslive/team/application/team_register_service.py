from team.domain import TeamRepository
from accounts.domain import Member
from team.serializers import TeamRegisterRequestSerializer
from utils import S3Connect, SqsConnect
from team.domain import LeagueTeam
from league.domain import LeagueRepository
from django.db import transaction
from utils.exceptions.team_exceptions import S3UploadError, TeamSaveError, EmptyLogoError
from team.dto import TeamRequestDTO, TeamMakeDTO
from league.domain import League

class TeamRegisterService:
    def __init__(self, team_repository: TeamRepository, league_repository: LeagueRepository):
        self._team_repository = team_repository
        self._league_repository = league_repository
        self._s3_conn = S3Connect()
        self._uploaded_logo_urls = []
        self._logo_uploaded_teams_keys = []

    def register_teams(self, request_data, league_id: int, user_data: Member):
        league = self._league_repository.find_league_by_id(league_id)
        team_data = TeamRequestDTO(request_data)
        teams_names = team_data.names
        teams_logos = team_data.logos
        self._check_logo_str(teams_logos)

        self._upload_logo_on_s3(teams_logos, teams_names, league)               
        self._make_and_save_team_in_transaction(teams_names, league, user_data)
        self._send_sqs_message()

    def _upload_logo_on_s3(self, teams_logos, teams_names, league: League):
         # 로고들을 S3에 업로드 하는 로직
        s3_upload_error_teams = []
        for i, team_logo in enumerate(teams_logos):
            team_name = teams_names[i]
            try:
                team_dto = TeamMakeDTO(team_name, team_logo)
                team_data_serializer = TeamRegisterRequestSerializer(data=team_dto.__dict__)
                team_data_serializer.is_valid(raise_exception=True)
                logo_url = self._s3_conn.upload_to_s3(image_data=team_logo, team_name=team_name, league_name=league.name)
                s3_key = self._s3_conn.make_s3_key(image_data=team_logo, team_name=team_name, league_name=league.name)
                self._uploaded_logo_urls.append(logo_url)
                self._logo_uploaded_teams_keys.append(s3_key)
            except:
                s3_upload_error_teams.append(team_name)

        if s3_upload_error_teams:
            self._delete_s3_object(self._logo_uploaded_teams_keys)
            raise S3UploadError(s3_upload_error_teams)
        
    def _make_and_save_team_in_transaction(self, teams_names, league: League, user_data: dict):
        save_error_teams = []
        try:
            with transaction.atomic():
                for i, team_name in enumerate(teams_names):
                    logo_url = self._uploaded_logo_urls[i]
                    new_team = LeagueTeam(name=team_name, logo_image_url=logo_url, league=league, manager=user_data, organization=user_data.organization)
                    self._team_repository.save_team(new_team)
        except:
            save_error_teams.append(team_name)
        if save_error_teams:
            self._delete_s3_object(self._logo_uploaded_teams_keys)
            raise TeamSaveError(save_error_teams)

    def _send_sqs_message(self):
        sqs_conn = SqsConnect()
        for logo_uploaded_teams_key in self._logo_uploaded_teams_keys:
            sqs_conn.send_message_to_sqs(logo_uploaded_teams_key)

    def _delete_s3_object(self, s3_keys: list[str]):
        for s3_key in s3_keys:
            self._s3_conn.delete_object(s3_key)
    
    def _check_logo_str(self, teams_logos):
        for logo in teams_logos:
            if isinstance(logo, str):
                raise EmptyLogoError

    class _TeamDto:
        def __init__(self, name: str, logo_image_url: str):
            self.name = name
            self.logo_image_url = logo_image_url
