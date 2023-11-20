from dependency_injector import containers, providers
from team.domain import TeamRepository, TeamPlayerRepository
from team.application import (
                        TeamService,
                        TeamGetService,
                        TeamPlayerService,
                        )
from league.domain import LeagueRepository

class TeamContainer(containers.DeclarativeContainer):
    team_repository = providers.Factory(TeamRepository)
    league_repository = providers.Factory(LeagueRepository)
    team_player_repository = providers.Factory(TeamPlayerRepository)

    team_service = providers.Factory(
        TeamService,
        team_repository=team_repository,
        league_repository=league_repository
    )
    team_get_service = providers.Factory(
        TeamGetService,
        team_repository=team_repository
    )
    team_player_service = providers.Factory(
        TeamPlayerService,
        team_repository=team_repository,
        team_player_repository=team_player_repository
    )