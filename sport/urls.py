from django.urls import path
from sport.presentation import SportView

app_name = 'sport'

urlpatterns = [
    path('', SportView.as_view())
]