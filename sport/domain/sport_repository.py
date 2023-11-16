from sport.domain import Sport
from django.shortcuts import get_list_or_404

class SportRepository:
    def find_all_sport(sport_id: int):
        return Sport.objects.all()