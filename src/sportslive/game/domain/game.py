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
    manager = models.ForeignKey(Member, models.DO_NOTHING)
    league = models.ForeignKey(League, models.DO_NOTHING)
    name = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    video_id = models.CharField(max_length=255, blank=True, null=True)
    quarter_changed_at = models.DateTimeField()
    game_quarter = models.CharField(max_length=255, default='시작 전')
    state = models.CharField(max_length=255, choices=GAME_CHOICES, default='SCHEDULED')
    round = models.IntegerField(default=0)
    
    class Meta:
        db_table = 'games'

    @property
    def game_state_korean(self):
        mapping = {
            'PLAYING': '진행중',
            'FINISHED': '종료',
            'SCHEDULED': '예정',
        }
        return mapping.get(self.state)