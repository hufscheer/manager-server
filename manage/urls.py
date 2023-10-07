from django.urls import path, include
from .views.game_register_view import GameRegisterView
from .views.game_score_change_view import GameScoreChangeView
from .views.game_team_list_view import GameTeamListView
app_name = 'manage'

urlpatterns = [
    path('game/register/', GameRegisterView.as_view(), name='GameRegisterView'),
    path('game/score/<int:game_id>/', GameScoreChangeView.as_view(), name='GameScoreChangeView'),
    path('game/teamlist/<int:game_id>/', GameTeamListView.as_view(), name='GameTeamListView'),
]