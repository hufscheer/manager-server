from dependency_injector import containers, providers
from report.domain import ReportRepository, CheerTalkRepository
from game.domain import GameRepository
from report.application import ReportService, ReportGetService

class ReportContainer(containers.DeclarativeContainer):
    report_repository = providers.Factory(ReportRepository)
    cheer_talk_repository = providers.Factory(CheerTalkRepository)
    game_repository = providers.Factory(GameRepository)
    report_service = providers.Factory(
        ReportService,
        report_repository=report_repository,
        cheer_talk_repository=cheer_talk_repository
    )
    report_get_service = providers.Factory(
        ReportGetService,
        report_repository=report_repository,
        cheer_talk_repository=cheer_talk_repository,
        game_repository=game_repository,
    )