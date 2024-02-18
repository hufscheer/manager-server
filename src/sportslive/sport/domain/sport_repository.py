from sport.domain import Sport, Quarter
from django.shortcuts import get_list_or_404

class SportRepository:
    def find_all_sport(sport_id: int):
        return Sport.objects.all()
    
    def find_all_quarter_by_sport_id(self, sport_id: int):
        return get_list_or_404(Quarter, sports=sport_id)