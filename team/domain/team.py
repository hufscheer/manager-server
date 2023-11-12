from django.db import models
from accounts.domain import Member, Organization
from league.domain import League

class Team(models.Model): #team
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    logo_image_url = models.CharField(max_length=255)
    league = models.ForeignKey(League, models.DO_NOTHING)
    administrator = models.ForeignKey(Member, models.DO_NOTHING)
    organization = models.ForeignKey(Organization, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'teams'