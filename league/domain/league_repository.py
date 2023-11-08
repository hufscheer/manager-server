from league.domain import LeagueSport

class LeagueRepository:
    def save_sports(self, league_sport: LeagueSport):
        league_sport.save()