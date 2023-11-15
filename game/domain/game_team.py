from django.db import models
from team.domain import Team

class GameTeam(models.Model):
    id = models.BigAutoField(primary_key=True)
    game = models.ForeignKey('Game', models.DO_NOTHING)
    team = models.ForeignKey(Team, models.DO_NOTHING)
    cheer_count = models.IntegerField(default=0)
    score = models.IntegerField(default=0)

    class Meta:
        managed = False
        db_table = 'game_teams'