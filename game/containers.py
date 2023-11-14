from dependency_injector import containers, providers
from game.domain import GameRepository
from game.application import GameService

class GameContainer(containers.DeclarativeContainer):
    game_repository = providers.Factory(GameRepository)
    game_service = providers.Factory(
        GameService,
        game_repository=game_repository        
    )

