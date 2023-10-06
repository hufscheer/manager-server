from django.db import models
from .game import Game

class Record(models.Model):
    id = models.BigAutoField(primary_key=True)
    player_name = models.CharField(max_length=255)
    score = models.IntegerField()
    game = models.ForeignKey('Game', models.DO_NOTHING, blank=True, null=True)
    team = models.ForeignKey('Team', models.DO_NOTHING, blank=True, null=True)
    scored_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'record'