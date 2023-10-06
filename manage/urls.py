from django.urls import path, include
from .views.game_register_view import GameRegisterView
app_name = 'manage'

urlpatterns = [
    path('game/register/', GameRegisterView.as_view(), name='GameRegisterView'),
]