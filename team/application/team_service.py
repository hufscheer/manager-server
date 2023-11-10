from team.domain import TeamRepository
from accounts.domain import Member
from team.serializers import TeamRegisterRequestSerializer
from utils.upload_to_s3 import upload_to_s3
from team.domain import Team
from league.domain import League

class TeamService:
    def __init__(self, team_repository: TeamRepository, *args, **kwargs):
        self._team_repository = team_repository

    def register_teams(self, request_data, league: League, user_data: Member):
        teams_data_serializer = TeamRegisterRequestSerializer(data=request_data)
        teams_data_serializer.is_valid(raise_exception=True)
        team_data = teams_data_serializer.validated_data
        teams_names = team_data.get('names')
        teams_logos = team_data.get('logos')
        error_team = []

        for i, team_name in enumerate(teams_names):
            team_logo = teams_logos[i]
            try:
                logo_url = upload_to_s3(image_data=team_logo, team_name=team_name, league_name=league.name)
                new_team = Team(name=team_name, logo_image_url=logo_url, league=league, administrator=user_data, organization=user_data.organization)
                self._team_repository.save_team(new_team)
            except:
                error_team.append(team_name)
        if error_team:
            return {"errorTeams": error_team}