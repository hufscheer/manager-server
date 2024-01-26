from django.urls import path
from team.presentation import TeamView, TeamGetView, TeamPlayerView, TeamPlayerGetView, TeamRegisterView

app_name = 'team'

urlpatterns = [
    path('register/<int:league_id>/', TeamRegisterView.as_view()),
    path('<int:team_id>/change/', TeamView.as_view()),
    path('<int:league_id>/', TeamGetView.as_view()),
    path('<int:team_id>/player/', TeamPlayerView.as_view()),
    path('<int:team_id>/player/all/', TeamPlayerGetView.as_view()),
]