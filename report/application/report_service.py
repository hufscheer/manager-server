from report.domain import ReportRepository, CommentRepository, Report, Comment
from report.serializers import ReportResponseSerializer
from game.domain import GameRepository, GameTeam
from accounts.domain import Member
from typing import List, Union

class ReportService:
    def __init__(self, report_repository: ReportRepository, comment_repository: CommentRepository, game_repository: GameRepository, *args, **kwargs):
        self._report_repository = report_repository
        self._comment_repository = comment_repository
        self._game_repository = game_repository

    def get_report_info(self, user_data: Member):
        pending_reports: list[Report] = self._report_repository.find_pending_reports_with_comment()
        game_team_ids: list[int] = [report.comment.game_team_id for report in pending_reports]
        pending_report_infos = self._get_report_info_object(game_team_ids, pending_reports, user_data)

        is_blocked_comments: list[Comment] = self._comment_repository.find_is_blocked_comments()
        game_team_ids: list[int] = [comment.game_team_id for comment in is_blocked_comments]
        is_blocked_report_infos = self._get_report_info_object(game_team_ids, is_blocked_comments, user_data)

        response_dto = self._ResponseDto(pending_report_infos, is_blocked_report_infos)
        return ReportResponseSerializer(response_dto).data
    
    def _get_report_info_object(self, game_team_ids: list[int], reports_or_comments: List[Union[Comment, Report]], user_data: Member):
        game_team_objects = self._game_repository.find_game_team_with_game_league_and_sport_by_ids(game_team_ids, user_data)
        game_team_dict = {game_team.id: game_team for game_team in game_team_objects}
        game_team_infos = [game_team_dict.get(game_team_id, None) for game_team_id in game_team_ids]
        return [
                self._ReportInfo(report, game_info)
                for report, game_info in zip(reports_or_comments, game_team_infos)
                if game_info is not None
            ]
    
    class _ResponseDto:
        def __init__(self, pending: list, is_blocked_comments: list):
            self.pending = pending
            self.is_blocked_comments = is_blocked_comments

    class _ReportInfo:
        def __init__(self, report_info, game_info: GameTeam):
            self.report_info = report_info
            self.game_info = game_info
