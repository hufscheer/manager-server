from django.urls import path
from game.presentation import GameView, GameTeamView, GameChangeView

app_name = 'game'

urlpatterns = [
    path('<int:league_id>/', GameView.as_view()),
    path('team/<int:game_id>/', GameTeamView.as_view()),
    path('change/<int:game_id>/', GameChangeView.as_view())
]