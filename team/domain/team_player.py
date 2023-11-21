from django.db import models

class TeamPlayer(models.Model):
    id = models.BigAutoField(primary_key=True)
    team = models.ForeignKey('Team', models.DO_NOTHING)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'team_players'