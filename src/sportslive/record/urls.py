from django.urls import path
from record.presentation import (
    RecordCreateView,
    RecordChangeView,
    RecordDeleteView,
)

app_name = 'record'

urlpatterns = [
    path('create/<str:record_type>/<int:game_id>/', RecordCreateView.as_view()),
    path('change/<int:record_id>/<int:extra_record_id>/<str:record_type>/', RecordChangeView.as_view()),
    path('delete/<str:record_type>/<int:extra_record_id>/<int:game_id>/', RecordDeleteView.as_view()),
]