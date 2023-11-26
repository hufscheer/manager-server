from dependency_injector import containers, providers
from record.domain import RecordRepository
from record.application import RecordService
from game.domain import GameRepository

class RecordContainer(containers.DeclarativeContainer):
    record_repository = providers.Factory(RecordRepository)
    game_repository = providers.Factory(GameRepository)
    record_service = providers.Factory(
        RecordService,
        record_repository=record_repository,
        game_repository=game_repository,
    )

