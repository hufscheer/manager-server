from team.domain import TeamRepository, Team, TeamPlayer
from team.serializers import TeamPlayerRegisterRequestSerializer

class TeamPlayerService:
    def __init__(self, team_repository: TeamRepository, *args, **kwargs):
        self._team_repository = team_repository

    def register_team_players(self, request_data: dict, team_id: int):
        team: Team = self._team_repository.find_team_by_id(team_id)
        team_player_register_request_serializer = TeamPlayerRegisterRequestSerializer(data=request_data, many=True)
        team_player_register_request_serializer.is_valid(raise_exception=True)
        team_player_datas = team_player_register_request_serializer.validated_data
        
        for team_player_data in team_player_datas:
            team_player = TeamPlayer(
                    team=team,
                    name=team_player_data.get('name'),
                    description=team_player_data.get('description')
                )
            self._team_repository.save_team_player(team_player)