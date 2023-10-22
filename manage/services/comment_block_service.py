from manage.repositories import CommentRepository

class CommentBlockService:
    def __init__(self,comment_repository: CommentRepository, *args, **kwargs):
        self._comment_repository = comment_repository
    
    def block_comment(self, comment_id: int):
        comment = self._comment_repository.find_commeny_by_id(comment_id)
        comment.is_blocked = True
        self._comment_repository.save(comment, 'is_blocked')