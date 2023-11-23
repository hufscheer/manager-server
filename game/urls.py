from django.urls import path
from game.presentation import (
                                GameView,
                                GameTeamView,
                                GameChangeView,
                                GameTeamPlayerView,
                                GameTeamPlayerGetView,
                                GameExtraView
                            )

app_name = 'game'

urlpatterns = [
    path('<int:league_id>/', GameView.as_view()),
    path('team/<int:game_id>/', GameTeamView.as_view()),
    path('change/<int:game_id>/', GameChangeView.as_view()),
    path('<int:game_id>/extra/', GameExtraView.as_view()),
    path('team/<int:game_team_id>/player/', GameTeamPlayerView.as_view()),
    path('team/<int:game_team_id>/player/all/', GameTeamPlayerGetView.as_view()),
]