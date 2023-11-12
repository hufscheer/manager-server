from team.domain import Team

class TeamRepository:
    def save_team(self, team: Team):
        team.save()
    
    def find_all_teams_by_league_id(self, league_id: int):
        return Team.objects.filter(league_id=league_id)
    
    def find_team_by_id(self, team_id: int):
        return Team.objects.get(id=team_id)