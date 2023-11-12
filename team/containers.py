from dependency_injector import containers, providers
from team.domain import TeamRepository
from team.application import TeamService, TeamGetService

class TeamContainer(containers.DeclarativeContainer):
    team_repository = providers.Factory(TeamRepository)
    team_service = providers.Factory(
        TeamService,
        team_repository=team_repository
    )
    team_get_service = providers.Factory(
        TeamGetService,
        team_repository=team_repository
    )
