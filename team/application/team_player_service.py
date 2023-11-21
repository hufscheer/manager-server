from team.domain import TeamRepository, Team, TeamPlayer, TeamPlayerRepository
from team.serializers import TeamPlayerRegisterRequestSerializer, TeamPlayerChangeRequestSerializer
from accounts.domain import Member
from django.core.exceptions import PermissionDenied

class TeamPlayerService:
    def __init__(self, team_repository: TeamRepository, team_player_repository: TeamPlayerRepository, *args, **kwargs):
        self._team_repository = team_repository
        self._team_player_repository = team_player_repository

    def register_team_players(self, request_data: dict, team_id: int):
        team: Team = self._team_repository.find_team_by_id(team_id)
        team_player_register_request_serializer = TeamPlayerRegisterRequestSerializer(data=request_data, many=True)
        team_player_register_request_serializer.is_valid(raise_exception=True)
        team_player_datas: list[dict] = team_player_register_request_serializer.validated_data
        
        for team_player_data in team_player_datas:
            team_player = TeamPlayer(
                    team=team,
                    name=team_player_data.get('name'),
                    description=team_player_data.get('description')
                )
            self._team_player_repository.save_team_player(team_player)

    def change_team_player(self, request_data: dict, team_player_id: int):
        team_player: TeamPlayer = self._team_player_repository.find_team_player_by_id(team_player_id)
        team_player_request_serializer = TeamPlayerChangeRequestSerializer(data=request_data)
        team_player_request_serializer.is_valid(raise_exception=True)
        team_player_data = team_player_request_serializer.validated_data

        team_player.name = team_player_data.get('name')
        team_player.description = team_player_data.get('description')
        self._team_player_repository.save_team_player(team_player)

    def delete_team_player(self, team_player_id: int, user_data: Member):
        team_player: TeamPlayer = self._team_player_repository.find_team_player_with_team_by_id(team_player_id)
        if team_player.team.administrator.id != user_data.id:
            raise PermissionDenied
        self._team_player_repository.delete_team_player(team_player)