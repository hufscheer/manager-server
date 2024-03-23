from league.domain import LeagueRepository
from league.serializers import (
                    LeagueSportRegistrationSerializer,
                    LeagueSportChangeSerializer,
                    LeagueDeleteSerializer,
                    LeagueRegisterResponseSerializer,
                )
from accounts.domain import Member
from league.domain import LeagueSport, League
from django.core.exceptions import PermissionDenied
from utils.exceptions.league_exception import CantEndAtFasterThanStartAt

class LeagueService:
    def __init__(self, league_repository: LeagueRepository, *args, **kwargs):
        self._league_repository = league_repository
    
    def register_league(self, request_data , user_data: Member):
        league_sport_serializer = LeagueSportRegistrationSerializer(data=request_data)
        league_sport_serializer.is_valid(raise_exception=True)
        league_sport_data = league_sport_serializer.validated_data
        league_data = league_sport_data.get('league_data')
        self._check_start_and_end_time(league_data)
        league: League = self._create_league_object(league_data, user_data)
        self._league_repository.save_league(league)

        sport_ids: list[int] = league_sport_data.get('sport_data')
        self._register_league_sports(sport_ids=sport_ids, league=league)
        return LeagueRegisterResponseSerializer(self._ResponseLeagueIdDto(league_id=league.id)).data

    def change_league(self, request_data , user_data: Member):
        league_sport_serializer = LeagueSportChangeSerializer(data=request_data)
        league_sport_serializer.is_valid(raise_exception=True)
        league_sport_data = league_sport_serializer.validated_data
        league_id = league_sport_data.get('league_id')
        target_league: League = self._league_repository.find_league_by_id(league_id)
        league_data: dict = league_sport_data.get('league_data')

        if target_league.organization != user_data.organization:
            raise PermissionDenied
        
        self._change_league_object(league_data, target_league)

        sport_ids: list[int] = league_sport_data.get('sport_data')
        self._league_repository.delete_league_sports_by_league_id(target_league.id)
        self._register_league_sports(sport_ids=sport_ids, league=target_league)
    
    def delete_league(self, request_data , user_data: Member):
        league_delete_serializer = LeagueDeleteSerializer(data=request_data)
        league_delete_serializer.is_valid(raise_exception=True)
        league_delete_data = league_delete_serializer.validated_data
        league_id = league_delete_data.get('league_id')
        target_league = self._league_repository.find_league_by_id(id=league_id)

        if target_league.organization != user_data.organization:
            raise PermissionDenied
        
        self._make_leage_is_deleted_true(target_league)

    def _make_leage_is_deleted_true(self, target_league: League):
        target_league.is_deleted = True
        self._league_repository.save_league(target_league, 'is_deleted')

    def _change_league_object(self, league_data: dict, target_league: League):
        target_league.name = league_data.get('name')
        target_league.start_at = league_data.get('start_at')
        target_league.end_at = league_data.get('end_at')
        target_league.max_round = league_data.get('max_round')
        target_league.in_progress_round = league_data.get('in_progress_round')
        self._league_repository.save_league(target_league)

    def _create_league_object(self, league_data: dict, user_data: Member):
        return League(
            manager=user_data,
            organization=user_data.organization,
            name=league_data.get('name'),
            start_at=league_data.get('start_at'),
            end_at=league_data.get('end_at'),
            max_round=league_data.get('max_round'),
            in_progress_round=league_data.get('max_round')
        )
    def _check_start_and_end_time(self, league_data: dict):
        start_at = league_data.get('start_at')
        end_at = league_data.get('end_at')
        if end_at < start_at:
            raise CantEndAtFasterThanStartAt 

    def _register_league_sports(self, sport_ids: list[int], league: League):
        for sport_id in sport_ids:
            leage_sport = LeagueSport(sport_id=sport_id, league_id=league.id)
            self._league_repository.save_sports(leage_sport)

    class _ResponseLeagueIdDto:
        def __init__(self, league_id: int):
            self.league_id = league_id