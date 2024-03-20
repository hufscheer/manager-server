from django.db import models
from game.domain import Game, GameTeam, LineupPlayer
from sport.domain import Quarter

class Record(models.Model):
    RECORD_TYPE_CHOICES = (
        ('SCORE', 'score'),
        ('REPLACEMENT', 'replacement')
    )
    id = models.BigAutoField(primary_key=True)
    game = models.ForeignKey(Game, models.CASCADE)
    game_team = models.ForeignKey(GameTeam, models.CASCADE)
    recorded_quarter = models.ForeignKey(Quarter, models.DO_NOTHING)
    recorded_at = models.IntegerField()
    record_type = models.CharField(max_length=255, choices=RECORD_TYPE_CHOICES, null=True)

    class Meta:
        db_table = 'records'

class ScoreRecord(models.Model):
    id = models.BigAutoField(primary_key=True)
    record = models.OneToOneField(Record, models.CASCADE)
    lineup_player = models.ForeignKey(LineupPlayer, models.CASCADE)
    score = models.IntegerField()

    class Meta:
        db_table = 'score_records'

class ReplacementRecord(models.Model):
    id = models.BigAutoField(primary_key=True)
    record = models.OneToOneField(Record, models.CASCADE)
    origin_lineup_player = models.ForeignKey(LineupPlayer, models.CASCADE)
    replaced_lineup_player = models.ForeignKey(LineupPlayer, models.CASCADE)
    
    class Meta:
        db_table = 'replacement_records'