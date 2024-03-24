from django.shortcuts import get_object_or_404, get_list_or_404
from game.domain import Game, GameTeam, LineupPlayer
from accounts.domain import Member

class GameRepository:
    
    def find_game_by_id(self, game_id):
        return get_object_or_404(Game, id=game_id)
    
    def find_game_with_manger_by_id(self, game_id: int):
        return get_object_or_404(Game.objects.select_related('manager'), id=game_id)

    def delete_game(self, game: Game):
        game.delete()
    
    def find_game_with_sport_by_id(self, game_id):
        return get_object_or_404(Game.objects.select_related('sport'), id=game_id)

    def save_game_team(self, game_team: GameTeam):
        game_team.save()
    
    def find_game_team_by_id(self, game_team_id: int):
        return get_object_or_404(GameTeam, id=game_team_id)
    
    def find_game_team_with_game_league_and_sport_by_ids(self, game_team_ids: list, user: Member):
        return GameTeam.objects.select_related('game__league', 'game__sport').filter(id__in=game_team_ids, game__league__organization=user.organization)
                    
    def find_game_teams_with_team_by_game_id(self, game_id: int):
        return get_list_or_404(
            GameTeam.objects.select_related('league_team').filter(game_id=game_id)
        )

    def save_lineup_player(self, lineup_player: LineupPlayer):
        lineup_player.save()

    def find_lineup_players_by_game_team_id(self, game_team_id: int):
        return get_list_or_404(LineupPlayer, game_team_id=game_team_id)
    
    def find_lineup_player_by_id(self, lineup_player_id: int):
        return get_object_or_404(LineupPlayer, id=lineup_player_id)
    
    def delete_lineup_players_by_ids(self, ids: set):
        LineupPlayer.objects.filter(id__in=ids).delete()

    def save_game(self, game: Game):
        game.save()