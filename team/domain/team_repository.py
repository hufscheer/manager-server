from team.domain import Team
from django.shortcuts import get_object_or_404, get_list_or_404

class TeamRepository:
    def save_team(self, team: Team):
        team.save()

    def find_all_teams_by_league_id(self, league_id: int):
        return get_list_or_404(Team, league_id=league_id)
    
    def find_team_by_id(self, team_id: int):
        return get_object_or_404(Team, id=team_id)
    
    def find_team_with_league_by_id(self, team_id: int):
        return get_object_or_404(Team.objects.select_related('league'), id=team_id)