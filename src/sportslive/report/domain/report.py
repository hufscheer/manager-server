from django.db import models
from report.domain import CheerTalk

class Report(models.Model):
    REPORT_STATE_CHOICES = (
        ('UNCHECKED', 'unchecked'),
        ('VALID','valid'),
        ('INVALID', 'invalid'),
        ('PENDING', 'pending')
    )
    id = models.BigAutoField(primary_key=True)
    cheer_talk = models.ForeignKey(CheerTalk, models.DO_NOTHING, unique=True)
    reported_at = models.DateTimeField()
    state = models.CharField(max_length=255, choices=REPORT_STATE_CHOICES)

    class Meta:
        db_table = 'reports'
