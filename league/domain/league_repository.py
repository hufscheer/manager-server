from league.domain import LeagueSport, League

class LeagueRepository:
    def save_sports(self, league_sport: LeagueSport):
        league_sport.save()

    def find_league_by_id(self, id: int):
        return League.objects.get(id=id)
    
    def delete_league_sports_by_league_id(self, league_id: int):
        LeagueSport.objects.filter(league_id=league_id).delete()

    def save_league(self,league: League, **args):
        if args:
            league.save(update_fields=[f'{args[0]}'])
        else:
            league.save()
