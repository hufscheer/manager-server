from dependency_injector import containers, providers
from team.domain import TeamRepository, TeamPlayerRepository
from team.application import (
                        TeamService,
                        TeamGetService,
                        TeamPlayerService,
                        TeamPlayerGetService,
                        TeamRegisterService,
                        )
from league.domain import LeagueRepository
from utils.s3 import S3Connect, FakeS3Connect
from utils.sqs import SqsConnect, FakeSqsConnect
from team.dto import TeamRequestDTO, FakeTeamRequestDTO

class TeamContainer(containers.DeclarativeContainer):
    team_repository = providers.Factory(TeamRepository)
    league_repository = providers.Factory(LeagueRepository)
    team_player_repository = providers.Factory(TeamPlayerRepository)

    team_service = providers.Factory(
        TeamService,
        team_repository=team_repository,
        s3_conn=S3Connect(),
        sqs_conn=SqsConnect(),
    )
    team_register_service = providers.Factory(
        TeamRegisterService,
        team_repository=team_repository,
        league_repository=league_repository,
        s3_conn=S3Connect(),
        sqs_conn=SqsConnect(),
        team_request_dto=TeamRequestDTO
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
    team_player_get_service = providers.Factory(
        TeamPlayerGetService,
        team_repository=team_repository,
        team_player_repository=team_player_repository
    )
    test_team_service = providers.Factory(
        TeamService,
        team_repository=team_repository,
        s3_conn=FakeS3Connect(),
        sqs_conn=FakeSqsConnect(),
    )
    test_team_register_service = providers.Factory(
        TeamRegisterService,
        team_repository=team_repository,
        league_repository=league_repository,
        s3_conn=FakeS3Connect(),
        sqs_conn=FakeSqsConnect(),
        team_request_dto=FakeTeamRequestDTO
    )