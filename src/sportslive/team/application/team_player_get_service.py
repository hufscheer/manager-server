from team.domain import TeamPlayerRepository, TeamRepository, LeagueTeamPlayer
from team.serializers import TeamPlayersResponseSerialier
from game.domain import GameRepository, GameTeam, LineupPlayer

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
        current_lineup_players: list[LineupPlayer] = self._game_repository.find_lineup_players_by_game_team_id(game_team.id)
        current_lineup_players_ids = [current_lineup_player.league_team_player_id for current_lineup_player in current_lineup_players]
        team_players: list[LeagueTeamPlayer] = self._team_player_repository.find_team_player_by_team_id_exclude_lineup_player(game_team.league_team_id, current_lineup_players_ids)

        team_player_data = TeamPlayersResponseSerialier(team_players, many=True)
        return team_player_data.data
