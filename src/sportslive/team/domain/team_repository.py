from team.domain import LeagueTeam
from django.shortcuts import get_object_or_404

class TeamRepository:
    def save_team(self, team: LeagueTeam):
        team.save()

    def find_all_teams_by_league_id(self, league_id: int):
        return LeagueTeam.objects.filter(league_id=league_id)
    
    def find_team_by_id(self, team_id: int):
        return get_object_or_404(LeagueTeam, id=team_id)
    
    def find_team_with_league_by_id(self, team_id: int):
        return get_object_or_404(LeagueTeam.objects.select_related('league'), id=team_id)
    
    def delete_team(self, team: LeagueTeam):
        team.delete()