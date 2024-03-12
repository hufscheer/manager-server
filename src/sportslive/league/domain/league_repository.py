from league.domain import LeagueSport, League
from django.shortcuts import get_object_or_404, get_list_or_404

class LeagueRepository:
    def save_sports(self, league_sport: LeagueSport):
        league_sport.save()

    def find_league_by_id(self, id: int):
        return get_object_or_404(League, id=id)
    
    def delete_league_sports_by_league_id(self, league_id: int):
        LeagueSport.objects.filter(league_id=league_id).delete()

    def save_league(self,league: League, *args):
        if args:
            league.save(update_fields=[f'{args[0]}'])
        else:
            league.save()
            
    def get_all_leagues_by_organization_id(self, organization_id: int):
        return League.objects.filter(organization_id=organization_id, is_deleted=False).order_by('-start_at')