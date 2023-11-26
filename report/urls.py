from django.urls import path
from report.presentation import ReportView, BlockCommentView

app_name = 'report'

urlpatterns = [
    path('', ReportView.as_view()),
    path('comment/<int:comment_id>/', BlockCommentView.as_view())
]