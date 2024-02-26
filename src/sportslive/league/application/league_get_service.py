from league.domain import LeagueRepository
from league.serializers import LeagueGetSerializer

class LeagueGetService:
    def __init__(self, league_repository: LeagueRepository, *args, **kwargs):
        self._league_repository = league_repository

    def get_leagues(self, user_data):
        leagues = self._league_repository.get_all_leagues_by_organization_id(user_data.organization_id)
        league_get_serializer = LeagueGetSerializer(leagues, many=True)
        return league_get_serializer.data