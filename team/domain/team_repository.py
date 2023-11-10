from team.domain import Team

class TeamRepository:
    def save_team(self, team: Team):
        team.save()