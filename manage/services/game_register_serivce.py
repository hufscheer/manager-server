from manage.serializers import GameRegisterRequestSerializer
from django.utils import timezone

def post_game(post_game_data, admin_user):
    post_game_data['member'] = admin_user.id
    post_game_data['status_changed_at'] = timezone.now()
    game_register_request_serialzier = GameRegisterRequestSerializer(data=post_game_data)
    game_register_request_serialzier.is_valid(raise_exception=True)
    game_register_request_serialzier.save()
