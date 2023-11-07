from django.db import models
from sport.domain import Sport


class LeagueSport(models.Model):
    id = models.BigAutoField(primary_key=True)
    sport = models.ForeignKey(Sport, models.DO_NOTHING)
    league = models.ForeignKey('League', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'league_sports'