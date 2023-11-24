from dependency_injector import containers, providers
from report.domain import ReportRepository, CommentRepository
from game.domain import GameRepository
from report.application import ReportService

class ReportContainer(containers.DeclarativeContainer):
    report_repository = providers.Factory(ReportRepository)
    comment_repository = providers.Factory(CommentRepository)
    game_repository = providers.Factory(GameRepository)
    report_service = providers.Factory(
        ReportService,
        report_repository=report_repository,
        comment_repository=comment_repository,
        game_repository=game_repository,
    )