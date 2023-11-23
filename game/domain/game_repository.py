from django.shortcuts import get_object_or_404, get_list_or_404
from game.domain import Game, GameTeam, GameTeamPlayer

class GameRepository:
    
    def find_game_by_id(self, game_id):
        return get_object_or_404(Game, id=game_id)
    
    def find_game_with_sport_by_id(self, game_id):
        return get_object_or_404(Game.objects.select_related('sport'), id=game_id)

    def save_game_team(self, game_team: GameTeam):
        game_team.save()
    
    def find_game_team_by_id(self, game_team_id: int):
        return get_object_or_404(GameTeam, id=game_team_id)
    
    def save_game_team_player(self, game_team_player: GameTeamPlayer):
        game_team_player.save()

    def find_game_team_players_by_game_team_id(self, game_team_id: int):
        return get_list_or_404(GameTeamPlayer, game_team_id=game_team_id)
    
    def find_game_team_player_by_id(self, game_team_player_id: int):
        return get_object_or_404(GameTeamPlayer, id=game_team_player_id)
    
    def delete_game_team_players_by_ids(self, ids: set):
        GameTeamPlayer.objects.filter(id__in=ids).delete()

    def save_game(self, game: Game):
        game.save()