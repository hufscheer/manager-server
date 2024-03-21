from django.urls import path
from report.presentation import ReportListView, ManageReportView, InvalidReportView

app_name = 'report'

urlpatterns = [
    path('', ReportListView.as_view()),
    path('<int:report_id>/', ManageReportView.as_view()),
    path('invalid/<int:report_id>/', InvalidReportView.as_view()),
]