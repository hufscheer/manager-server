from sport.domain import Sport, Quarter


class SportRepository:
    def find_all_sport(sport_id: int):
        return Sport.objects.all()
    
    def find_all_quarter_by_sport_id(self, sport_id: int):
        return Quarter.objects.filter(sports=sport_id)