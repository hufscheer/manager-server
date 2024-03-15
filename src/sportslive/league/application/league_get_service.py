from league.domain import LeagueRepository
from league.serializers import LeagueGetSerializer
from league.domain import League, LeagueSport

class LeagueGetService:
    def __init__(self, league_repository: LeagueRepository, *args, **kwargs):
        self._league_repository = league_repository

    def get_leagues(self, user_data):
        organization_id: int = user_data.organization_id
        leagues: list[League] = self._league_repository.find_all_leagues_with_sport_by_organization_id(organization_id)
        for league in leagues:
            league.sport_datas = [
                self._SportWrapping(league_sport)
                for league_sport in league.league_sports.all()
            ]
        league_get_serializer = LeagueGetSerializer(leagues, many=True)
        return league_get_serializer.data
    
    class _SportWrapping:
        def __init__(self, league_sport: LeagueSport):
            self.id = league_sport.sport.id
            self.name = league_sport.sport.name