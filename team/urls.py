from django.urls import path
from team.presentation import TeamView

app_name = 'team'

urlpatterns = [
    path('register/<int:league_id>/', TeamView.as_view())
]