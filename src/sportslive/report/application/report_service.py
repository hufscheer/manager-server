from report.domain import ReportRepository, CheerTalkRepository, Report, CheerTalk

class ReportService:
    def __init__(self, report_repository: ReportRepository, cheer_talk_repository: CheerTalkRepository):
        self._report_repository = report_repository
        self._cheer_talk_repository = cheer_talk_repository
    
    def manage_report_state_and_cheer_talk_state(self, report_id: int):
        report: Report = self._report_repository.find_report_by_id(report_id)
        cheer_talk: CheerTalk = self._cheer_talk_repository.find_cheer_talk_by_id(report.cheer_talk_id)

        if report.state == "PENDING":
            cheer_talk.is_blocked = True
            report.state = "VALID"
        elif report.state == "VALID":
            cheer_talk.is_blocked = False
            report.state = "PENDING"

        self._report_repository.save_report(report)
        self._cheer_talk_repository.save_cheer_talk(cheer_talk)
    
    def block_cheer_talk(self, cheer_talk_id: int):
        cheer_talk: CheerTalk = self._cheer_talk_repository.find_cheer_talk_by_id(cheer_talk_id)
        if cheer_talk.is_bool_blocked:
            cheer_talk.is_blocked = False
        else:
            cheer_talk.is_blocked = True
        self._cheer_talk_repository.save_cheer_talk(cheer_talk)

    def make_report_invalid(self, report_id: int):
        report: Report = self._report_repository.find_report_by_id(report_id)
        report.state = 'INVALID'
        self._report_repository.save_report(report)
