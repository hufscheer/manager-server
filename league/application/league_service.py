from league.domain import LeagueRepository
from league.serializers import LeagueSerializer, LeagueSportRegistrationSerializer, LeagueSportChangeSerializer
from accounts.domain import Member
from league.domain import LeagueSport, League
from django.core.exceptions import PermissionDenied

class LeagueService:
    def __init__(self, league_repository: LeagueRepository, *args, **kwargs):
        self._league_repository = league_repository
    
    def register_league(self, request_data , user_data: Member):
        league_sport_serializer = LeagueSportRegistrationSerializer(data=request_data)
        league_sport_serializer.is_valid(raise_exception=True)
        league_sport_data = league_sport_serializer.validated_data
        league_data = league_sport_data.get('league_data')
        league_data['organization'] = user_data.organization_id
        league_data['administrator'] = user_data.id
        league_serializer = LeagueSerializer(data=league_data)
        league_serializer.is_valid(raise_exception=True)
        league: League = league_serializer.save()

        sport_ids: list[int] = league_sport_data.get('sport_data')
        self._register_league_sports(sport_ids=sport_ids, league=league)

    def change_league(self, request_data , user_data: Member):
        league_sport_serializer = LeagueSportChangeSerializer(data=request_data)
        league_sport_serializer.is_valid(raise_exception=True)
        league_sport_data = league_sport_serializer.validated_data
        league_id = league_sport_data.get('league_id')
        league_data: dict = league_sport_data.get('league_data')

        target_league : League = self._league_repository.find_league_by_id(league_id)
        if target_league.administrator != user_data:
            raise PermissionDenied
        
        league_data['organization'] = user_data.organization_id
        league_data['administrator'] = user_data.id
        league_serializer = LeagueSerializer(target_league, data=league_data)
        league_serializer.is_valid(raise_exception=True)
        league: League = league_serializer.save()

        sport_ids: list[int] = league_sport_data.get('sport_data')
        self._league_repository.delete_league_sports_by_league_id(league.id)
        self._register_league_sports(sport_ids=sport_ids, league=league)

    def _register_league_sports(self, sport_ids: list[int], league: League):
        for sport_id in sport_ids:
            leage_sport = LeagueSport(sport_id=sport_id, league_id=league.id)
            self._league_repository.save_sports(leage_sport)