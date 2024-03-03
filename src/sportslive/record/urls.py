from django.urls import path
from record.presentation import (
    RecordCreateView,
    RecordChangeView,
)

app_name = 'record'

urlpatterns = [
    path('create/<str:record_type>/<int:game_id>/', RecordCreateView.as_view()),
    path('change/<int:record_id>/<int:extra_record_id>/<str:record_type>/', RecordChangeView.as_view()),
]