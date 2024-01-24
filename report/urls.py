from django.urls import path
from report.presentation import ReportView, BlockCheerTalkView

app_name = 'report'

urlpatterns = [
    path('', ReportView.as_view()),
    path('comment/<int:comment_id>/', BlockCheerTalkView.as_view())
]