from django.urls import path
from report.presentation import ReportView

app_name = 'report'

urlpatterns = [
    path('', ReportView.as_view())
]