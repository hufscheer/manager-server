from django.db import models
from report.domain import Comment

class Report(models.Model): 
    id = models.BigAutoField(primary_key=True)
    comment = models.ForeignKey(Comment, models.DO_NOTHING)
    reported_at = models.DateTimeField()
    is_valid = models.BooleanField(default=False)

    class Meta:
        managed = False
        db_table = 'reports'
