from team.domain import TeamRepository
from team.serializers import TeamGetSerializer

class TeamGetService:
    def __init__(self, team_repository: TeamRepository, *args, **kwargs):
        self._team_repository = team_repository

    def get_all_teams(self, league_id: int):
        leagues = self._team_repository.find_all_teams_by_league_id(league_id=league_id)
        team_serailzier = TeamGetSerializer(leagues, many=True)
        return team_serailzier.data