from report.domain import Comment
from django.shortcuts import get_list_or_404

class CommentRepository:
    def find_is_blocked_comments(self):
        return get_list_or_404(Comment.objects.order_by('-created_at'), is_blocked=True)