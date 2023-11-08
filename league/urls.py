from django.urls import path
from league.presentation import LeagueView

app_name = 'league'

urlpatterns = [
    path('register/', LeagueView.as_view()),
]