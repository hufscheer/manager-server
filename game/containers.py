from dependency_injector import containers, providers
from game.domain import GameRepository
from game.application import GameService, GameTeamService, GameTeamGetService, GameTeamPlayerService
from team.domain import TeamRepository
from league.domain import LeagueRepository

class GameContainer(containers.DeclarativeContainer):
    game_repository = providers.Factory(GameRepository)
    team_repository = providers.Factory(TeamRepository)
    league_repository = providers.Factory(LeagueRepository)

    game_service = providers.Factory(
        GameService,
        game_repository=game_repository,
        league_repository=league_repository    
    )
    game_team_serivice = providers.Factory(
        GameTeamService,
        game_repository=game_repository,
        team_repository=team_repository,
    )

    game_team_get_serivice = providers.Factory(
        GameTeamGetService,
        game_repository=game_repository,
    )
    game_team_player_service = providers.Factory(
        GameTeamPlayerService,
        game_repository=game_repository,
    )