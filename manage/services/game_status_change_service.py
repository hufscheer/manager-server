from manage.models import Game
from django.utils import timezone

def get_status_type(game_id):
    game = Game.objects.get(id=game_id)
    return dict(game.GAME_STATUS)

def change_status(status_data, game_id):
    game = Game.objects.get(id=game_id)
    new_status = status_data.get('gameStatus')

    if new_status not in dict(Game.GAME_STATUS):
        raise ValueError("경기 상태에 존재하지 않는 상태입니다.")
    
    game.game_status = new_status
    game.status_changed_at = timezone.now()
    game.save(update_fields=['game_status', 'status_changed_at'])