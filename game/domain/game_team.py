from django.db import models
from team.domain import LeagueTeam

class GameTeam(models.Model):
    id = models.BigAutoField(primary_key=True)
    game = models.ForeignKey('Game', models.DO_NOTHING)
    league_team = models.ForeignKey(LeagueTeam, models.DO_NOTHING)
    cheer_count = models.IntegerField(default=0)
    score = models.IntegerField(default=0)

    class Meta:
        managed = False
        db_table = 'game_teams'