from django.urls import path
from record.presentation import RecordCreateView

app_name = 'record'

urlpatterns = [
    path('<int:game_id>/<str:record_type>/create/', RecordCreateView.as_view())
]