from django.urls import path
from report.presentation import ReportView, BlockCheerTalkView, InvalidReportView

app_name = 'report'

urlpatterns = [
    path('', ReportView.as_view()),
    path('cheer-talk/<int:report_id>/', BlockCheerTalkView.as_view()),
    path('invalid/<int:report_id>/', InvalidReportView.as_view()),
]