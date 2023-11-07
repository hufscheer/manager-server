from django.db import models
from sport.domain import Sport
from accounts.domain import Member
from league.domain import League

class Game(models.Model):
    GAME_CHOICES = (
        ('PLAYING', 'playing'),
        ('FINISHED','finished'),
        ('SCHEDULED', 'scheduled'),
    )
    id = models.BigAutoField(primary_key=True)
    sport = models.ForeignKey(Sport, models.DO_NOTHING)
    member = models.ForeignKey(Member, models.DO_NOTHING)
    league = models.ForeignKey(League, models.DO_NOTHING)
    name = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    video_id = models.CharField(max_length=255, blank=True, null=True)
    quarter_changed_at = models.DateTimeField()
    game_quarter = models.CharField(max_length=255)
    state = models.CharField(max_length=255, choices=GAME_CHOICES)

    class Meta:
        managed = False
        db_table = 'games'