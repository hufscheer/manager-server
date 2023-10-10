from manage.models.game import Game
from manage.serializers.change_game_score_serializer import GameInfoGetSerializer, GameScoreChangePostSerializer
from manage.serializers.game_team_list_serializer import GameListSerializer

def get_game_info(game_id):
    game = Game.objects.select_related('first_team', 'second_team').get(id=game_id)
    teams_data = {
        'first_team': game.first_team,
        'second_team': game.second_team,
    }
    team_list_serializer = GameListSerializer(teams_data)
    team_list_data = team_list_serializer.data

    game_info_get_serialzier = GameInfoGetSerializer(game)
    game_info_data = game_info_get_serialzier.data
    game_info_data['teamList'] = team_list_data

    return game_info_data


def change_game_score(post_change_game_data, game_id):
    post_change_game_data['game'] = game_id
    post_change_game_data['score'] = 1
    game_score_change_post_serializer = GameScoreChangePostSerializer(data=post_change_game_data)
    game_score_change_post_serializer.is_valid(raise_exception=True)
    record = game_score_change_post_serializer.save()

    game = Game.objects.get(id=game_id)
    update_field = None

    if record.team == game.first_team:
        game.first_team_score += record.score
        update_field = 'first_team_score'

    elif record.team == game.second_team:
        game.second_team_score += record.score
        update_field = 'second_team_score'

    if update_field:
        game.save(update_fields=[update_field])