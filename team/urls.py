from django.urls import path
from team.presentation import TeamView, TeamGetView, TeamPlayerView

app_name = 'team'

urlpatterns = [
    path('register/<int:league_id>/', TeamView.as_view()),
    path('change/', TeamView.as_view()),
    path('<int:league_id>/', TeamGetView.as_view()),
    path('<int:team_id>/player/', TeamPlayerView.as_view()),
    path('player/<int:team_player_id>/', TeamPlayerView.as_view())
]