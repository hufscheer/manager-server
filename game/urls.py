from django.urls import path
from game.presentation import GameView

app_name = 'game'

urlpatterns = [
    path('<int:league_id>/', GameView.as_view())
]