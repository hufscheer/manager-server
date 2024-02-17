from django.db import models

class LeagueTeamPlayer(models.Model):
    id = models.BigAutoField(primary_key=True)
    league_team = models.ForeignKey('LeagueTeam', models.DO_NOTHING)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    number = models.IntegerField(null=True)
    
    class Meta:
        managed = False
        db_table = 'league_team_players'