from django.db import models
from game.domain import Game, GameTeam, LineupPlayer
from sport.domain import Quarter

class Record(models.Model): 
    id = models.BigAutoField(primary_key=True)
    game = models.ForeignKey(Game, models.DO_NOTHING)
    game_team = models.ForeignKey(GameTeam, models.DO_NOTHING)
    lineup_player = models.ForeignKey(LineupPlayer, models.DO_NOTHING)
    score = models.IntegerField()
    scored_quarter = models.ForeignKey(Quarter, models.DO_NOTHING)
    scored_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'records'