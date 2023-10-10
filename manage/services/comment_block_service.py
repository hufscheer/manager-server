from manage.models import Comment

def block_comment(comment_id):
    comment = Comment.objects.get(id=comment_id)
    comment.is_blocked = True
    comment.save(update_fields=['is_blocked'])