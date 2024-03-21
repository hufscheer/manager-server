from dependency_injector import containers, providers
from record.domain import RecordRepository
from record.application import RecordCreateService, RecordService, RecordGetService
from game.domain import GameRepository

class RecordContainer(containers.DeclarativeContainer):
    record_repository = providers.Factory(RecordRepository)
    game_repository = providers.Factory(GameRepository)
    record_create_service = providers.Factory(
        RecordCreateService,
        record_repository=record_repository,
        game_repository=game_repository,
    )
    record_service = providers.Factory(
        RecordService,
        record_repository=record_repository,
        game_repository=game_repository,
    )
    record_get_service = providers.Factory(
        RecordGetService,
        record_repository=record_repository,
        game_repository=game_repository,
    )

