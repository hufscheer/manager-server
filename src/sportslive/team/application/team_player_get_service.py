from team.domain import TeamPlayerRepository, TeamRepository, LeagueTeamPlayer
from team.serializers import TeamPlayersResponseSerialier
from game.domain import GameRepository, GameTeam

class TeamPlayerGetService:
    def __init__(
            self,
            team_repository: TeamRepository,
            team_player_repository: TeamPlayerRepository,
            game_repository: GameRepository
        ):
        self._team_player_repository = team_player_repository
        self._team_repository = team_repository
        self._game_repository = game_repository

    def get_all_team_player(self, team_id: int):
        team_players: list[LeagueTeamPlayer] = self._team_player_repository.find_team_player_by_team_id(team_id)
        team_player_data = TeamPlayersResponseSerialier(team_players, many=True)
        return team_player_data.data
    
    def get_all_team_player_by_game_team(self, game_team_id: int):
        game_team: GameTeam = self._game_repository.find_game_team_by_id(game_team_id)
        team_players: list[LeagueTeamPlayer] = self._team_player_repository.find_team_player_by_team_id(game_team.league_team_id)

        team_player_data = TeamPlayersResponseSerialier(team_players, many=True)
        return team_player_data.data
