from django.db import models
from game.domain import GameTeam

class Comment(models.Model): 
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField()
    content = models.CharField(max_length=255)
    is_blocked = models.BooleanField(default=False)
    game_team = models.ForeignKey(GameTeam, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'comments'