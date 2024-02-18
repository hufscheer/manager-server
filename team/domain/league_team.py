from django.db import models
from accounts.domain import Member, Organization
from league.domain import League

class LeagueTeam(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    logo_image_url = models.CharField(max_length=255)
    league = models.ForeignKey(League, models.DO_NOTHING)
    manager = models.ForeignKey(Member, models.DO_NOTHING)
    organization = models.ForeignKey(Organization, models.DO_NOTHING)

    class Meta:
        db_table = 'league_teams'