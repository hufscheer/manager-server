from manage.models.game import Game
from manage.serializers.game_team_list_serializer import GameListSerializer

def get_team_list(game_id):
    game = Game.objects.select_related('first_team', 'second_team').get(id=game_id)
    game_team_list_serializer = GameListSerializer(game)
    return game_team_list_serializer.data
    