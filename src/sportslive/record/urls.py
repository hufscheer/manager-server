from django.urls import path
from record.presentation import (
    RecordCreateView,
    RecordChangeView,
    RecordDeleteView,
    RecordGetView
)

app_name = 'record'

urlpatterns = [
    path('<int:record_id>/', RecordGetView.as_view()),
    path('create/<str:record_type>/<int:game_id>/', RecordCreateView.as_view()),
    path('change/<int:record_id>/<str:record_type>/', RecordChangeView.as_view()),
    path('delete/<int:record_id>/<str:record_type>/', RecordDeleteView.as_view()),
]