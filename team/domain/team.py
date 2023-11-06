from django.db import models
from accounts.domain import Member, Organization

class Team(models.Model): #team
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    logo_image_url = models.CharField(max_length=255)
    administrator = models.ForeignKey(Member, models.DO_NOTHING, blank=True, null=True)
    organization = models.ForeignKey(Organization, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teams'