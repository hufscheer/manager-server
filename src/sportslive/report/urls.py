from django.urls import path
from report.presentation import ReportListView, BlockCheerTalkView, InvalidReportView

app_name = 'report'

urlpatterns = [
    path('', ReportListView.as_view()),
    path('cheer-talk/<int:report_id>/', BlockCheerTalkView.as_view()),
    path('invalid/<int:report_id>/', InvalidReportView.as_view()),
]