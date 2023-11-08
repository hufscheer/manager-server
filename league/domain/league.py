from django.db import models
from accounts.domain import Member, Organization

class League(models.Model): 
    id = models.BigAutoField(primary_key=True)
    administrator = models.ForeignKey(Member, models.DO_NOTHING)
    organization = models.ForeignKey(Organization, models.DO_NOTHING)
    name = models.CharField(max_length=255)
    is_deleted = models.BooleanField(default=False)
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'leagues'