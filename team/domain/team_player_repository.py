from team.domain import TeamPlayer
from django.shortcuts import get_object_or_404, get_list_or_404

class TeamPlayerRepository:
    def save_team_player(self, team_player: TeamPlayer):
        team_player.save()
    
    def find_team_player_by_id(self, team_player_id: int):
        return get_object_or_404(TeamPlayer, id=team_player_id)
    
    def delete_team_player(self, team_player: TeamPlayer):
        team_player.delete()

    def find_team_player_with_team_by_id(self, team_player_id: int):
        return get_object_or_404(TeamPlayer.objects.select_related('team'), id=team_player_id)
    
    def find_team_player_by_team_id(self, team_id: int):
        return get_list_or_404(TeamPlayer, team_id=team_id)