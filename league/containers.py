from dependency_injector import containers, providers
from .application import LeagueService
from .domain import LeagueRepository

class LeagueContainer(containers.DeclarativeContainer):
    league_repository = providers.Factory(LeagueRepository)
    league_service = providers.Factory(
        LeagueService,
        league_repository=league_repository
    )