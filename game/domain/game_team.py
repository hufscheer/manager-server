from django.db import models
from team.domain import Team

class GameTeam(models.Model):
    id = models.BigAutoField(primary_key=True)
    game = models.ForeignKey('Game', models.DO_NOTHING)
    team = models.ForeignKey(Team, models.DO_NOTHING)
    cheer_count = models.IntegerField()
    score = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'game_teams'