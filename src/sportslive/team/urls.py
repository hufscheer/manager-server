from django.urls import path
from team.presentation import (
    TeamView,
    TeamGetView,
    TeamPlayerCreateView,
    TeamPlayerGetView,
    TeamRegisterView,
    TeamPlayerUpdateDeleteView,
    TeamPlayerGetByGameTeamView,
)

app_name = 'team'

urlpatterns = [
    path('register/<int:league_id>/', TeamRegisterView.as_view()),
    path('<int:team_id>/change/', TeamView.as_view()),
    path('<int:league_id>/', TeamGetView.as_view()),
    path('<int:team_id>/player/', TeamPlayerCreateView.as_view()),
    path('player/<int:team_player_id>/', TeamPlayerUpdateDeleteView.as_view()),
    path('<int:team_id>/player/all/', TeamPlayerGetView.as_view()),
    path('player/game-team/<int:game_team_id>/', TeamPlayerGetByGameTeamView.as_view()),
]