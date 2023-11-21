from team.domain import TeamPlayerRepository, TeamRepository, TeamPlayer
from team.serializers import TeamPlayersResponseSerialier

class TeamPlayerGetService:
    def __init__(self, team_repository: TeamRepository, team_player_repository: TeamPlayerRepository, *args, **kwargs):
        self._team_player_repository = team_player_repository
        self._team_repository = team_repository

    def get_all_team_player(self, team_id: int):
        team_players: list[TeamPlayer] = self._team_player_repository.find_team_player_by_team_id(team_id)
        team_player_data = TeamPlayersResponseSerialier(team_players, many=True)
        return team_player_data.data