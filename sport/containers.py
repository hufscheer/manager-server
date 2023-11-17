from dependency_injector import containers, providers
from sport.domain import SportRepository
from sport.application import SportService

class SportContainer(containers.DeclarativeContainer):
    sport_repository = providers.Factory(SportRepository)
    sport_service = providers.Factory(
        SportService,
        sport_repository=sport_repository,
    )

