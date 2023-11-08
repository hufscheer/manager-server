from dependency_injector import containers, providers
from .application import LeagueService, LeagueGetService
from .domain import LeagueRepository

class LeagueContainer(containers.DeclarativeContainer):
    league_repository = providers.Factory(LeagueRepository)
    league_service = providers.Factory(
        LeagueService,
        league_repository=league_repository
    )
    league_get_service = providers.Factory(
        LeagueGetService,
        league_repository=league_repository
    )