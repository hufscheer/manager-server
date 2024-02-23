from django.urls import path
from game.presentation import (
                                GameView,
                                GameChangeView,
                                GameScoreView,
                                GameGetView,
                                GameTeamView,
                                LineupPlayerView,
                                LineupPlayerGetView,
                                GameTeamGetView,
                            )
app_name = 'game'

urlpatterns = [
    path('<int:league_id>/', GameView.as_view()),
    path('<int:game_id>/change/', GameChangeView.as_view()),
    path('score/', GameScoreView.as_view()),
    path('<int:game_id>/info/', GameGetView.as_view()),
    #path('team/<int:game_id>/', GameTeamView.as_view()),
    path('<int:game_id>/team/', GameTeamGetView.as_view()),
    path('team/<int:game_team_id>/lineup-player/', LineupPlayerView.as_view()),
    path('team/<int:game_team_id>/lineup-player/all/', LineupPlayerGetView.as_view()),
]