from django.shortcuts import get_object_or_404
from game.domain import Game, GameTeam

class GameRepository:
    
    def find_game_by_id(self, game_id):
        return get_object_or_404(Game, id=game_id)

    def save_game_team(self, game_team: GameTeam):
        game_team.save()