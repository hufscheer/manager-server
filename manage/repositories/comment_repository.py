from abc import ABC, abstractmethod
from manage.models import Comment

class CommentRepository(ABC):
    @abstractmethod
    def find_commeny_by_id(self, comment_id: int):
        pass

    @abstractmethod
    def save(self, comment: Comment):
        pass
    
class CommentRepositoryImpl(CommentRepository):
    def find_commeny_by_id(self, comment_id):
        return Comment.objects.get(id=comment_id)

    def save(self, comment: Comment, *args):
        if args:
            comment.save(update_fields=[f'{args[0]}'])
        else:
            comment.save()