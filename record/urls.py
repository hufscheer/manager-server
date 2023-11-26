from django.urls import path
from record.presentation import RecordView

app_name = 'record'

urlpatterns = [
    path('<int:game_id>/', RecordView.as_view())
]