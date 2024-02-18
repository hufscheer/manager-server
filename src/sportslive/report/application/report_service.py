from report.domain import ReportRepository, CheerTalkRepository, Report, CheerTalk
from report.serializers import ReportResponseSerializer
from game.domain import GameRepository, GameTeam
from accounts.domain import Member
from typing import List, Union

class ReportService:
    def __init__(self, report_repository: ReportRepository, cheer_talk_repository: CheerTalkRepository, game_repository: GameRepository):
        self._report_repository = report_repository
        self._cheer_talk_repository = cheer_talk_repository
        self._game_repository = game_repository

    def get_report_info(self, user_data: Member):
        pending_reports: list[Report] = self._report_repository.find_pending_reports_with_cheer_talk()
        game_team_ids: list[int] = [report.cheer_talk.game_team_id for report in pending_reports]
        pending_report_infos = self._get_report_info_object(game_team_ids, pending_reports, user_data)

        blocked_cheer_talks: list[CheerTalk] = self._cheer_talk_repository.find_is_blocked_cheer_talks()
        game_team_ids: list[int] = [cheer_talk.game_team_id for cheer_talk in blocked_cheer_talks]
        blocked_cheer_talks_infos = self._get_report_info_object(game_team_ids, blocked_cheer_talks, user_data)

        response_dto = self._ResponseDto(pending_report_infos, blocked_cheer_talks_infos)
        return ReportResponseSerializer(response_dto).data
    
    def block_cheer_talk(self, cheer_talk_id: int):
        cheer_talk: CheerTalk = self._cheer_talk_repository.find_cheer_talk_by_id(cheer_talk_id)

        if cheer_talk.is_blocked == b'\x00':
            cheer_talk.is_blocked = True
        elif cheer_talk.is_blocked == b'\x01':
            cheer_talk.is_blocked = False
        self._cheer_talk_repository.save_cheer_talk(cheer_talk)

    def _get_report_info_object(self, game_team_ids: list[int], reports_or_cheer_talks: List[Union[CheerTalk, Report]], user_data: Member):
        game_team_objects = self._game_repository.find_game_team_with_game_league_and_sport_by_ids(game_team_ids, user_data)
        game_team_dict = {game_team.id: game_team for game_team in game_team_objects}
        game_team_infos = [game_team_dict.get(game_team_id, None) for game_team_id in game_team_ids]
        return [
                self._ReportOrCheerTalkInfo(report_or_cheer_talk, game_info)
                for report_or_cheer_talk, game_info in zip(reports_or_cheer_talks, game_team_infos)
                if game_info is not None
            ]
    
    class _ResponseDto:
        def __init__(self, pending: list, blocked_cheer_talks_infos: list):
            self.pending = pending
            self.blocked_cheer_talks_infos = blocked_cheer_talks_infos

    class _ReportOrCheerTalkInfo:
        def __init__(self, report_or_cheer_talk, game_info: GameTeam):
            self.report_or_cheer_talk = report_or_cheer_talk
            self.game_info = game_info
