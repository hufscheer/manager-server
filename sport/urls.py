from django.urls import path
from sport.presentation import SportView, SportQuarterView

app_name = 'sport'

urlpatterns = [
    path('', SportView.as_view()),
    path('<int:sport_id>/quarter/', SportQuarterView.as_view())
]