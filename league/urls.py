from django.urls import path
from league.presentation import LeagueView, LeagueGetView

app_name = 'league'

urlpatterns = [
    path('', LeagueView.as_view()),
    path('all/', LeagueGetView.as_view()),
]