from sport.domain import SportRepository
from sport.serializers import SportsNameResponseSerializer

class SportService:
    def __init__(self, sport_repository: SportRepository, *args, **kwargs):
        self._sport_repository = sport_repository

    def get_all_sport_list(self):
        sports = self._sport_repository.find_all_sport()
        sports_name_response_serializer = SportsNameResponseSerializer(sports, many=True)
        return sports_name_response_serializer.data