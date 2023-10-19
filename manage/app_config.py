from dependency_injector import containers, providers
from .repositories import CommentRepositoryImpl
from .services import CommentBlockService

class ManageContainer(containers.DeclarativeContainer):
    
    comment_repository = providers.Factory(CommentRepositoryImpl)
    comment_block_service = providers.Factory(
        CommentBlockService,
        comment_repository=comment_repository.provider,
    )

