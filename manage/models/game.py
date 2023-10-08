from django.db import models
from accounts.models import Member

class Game(models.Model):
    GAME_STATUS = (
        ('BEFORE', '경기전'),
        ('FIRST_HALF', '전반전'),
        ('BREAK_TIME', '쉬는시간'),
        ('SECOND_HALF', '후반전'),
        ('END', '종료')
    )
    id = models.BigAutoField(primary_key=True)
    first_team_score = models.IntegerField(default=0)
    name = models.CharField(max_length=255)
    second_team_score = models.IntegerField(default=0)
    sports_name = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    first_team = models.ForeignKey('Team', models.DO_NOTHING, related_name='game_first_team_set')
    member = models.ForeignKey(Member, models.DO_NOTHING)
    second_team = models.ForeignKey('Team', models.DO_NOTHING, related_name='game_second_team_set')
    game_status = models.CharField(max_length=11, choices=GAME_STATUS, default='BEFORE')
    status_changed_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'game'