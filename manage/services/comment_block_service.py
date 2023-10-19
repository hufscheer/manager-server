

class CommentBlockService:
    def __init__(self, *args, **kwargs):
        from manage.app_config import ManageContainer
        self.comment_repository = ManageContainer.comment_repository()
    
    def block_comment(self, comment_id):
        comment = self.comment_repository.find_commeny_by_id(comment_id)
        comment.is_blocked = True
        self.comment_repository.save(comment, 'is_blocked')