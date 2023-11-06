from django.db import models
from game.domain import Game, GameTeam, GameTeamPlayer

class Record(models.Model): 
    id = models.BigAutoField(primary_key=True)
    game = models.ForeignKey(Game, models.DO_NOTHING)
    game_team = models.ForeignKey(GameTeam, models.DO_NOTHING)
    game_team_player = models.ForeignKey(GameTeamPlayer, models.DO_NOTHING)
    score = models.IntegerField()
    scored_quarter = models.CharField(max_length=255)
    scored_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'records'