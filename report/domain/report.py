from django.db import models
from report.domain import Comment

class Report(models.Model):
    REPORT_STATE_CHOICES = (
        ('UNCHECKED', 'unchecked'),
        ('VALID','valid'),
        ('INVALID', 'invalid'),
        ('PENDING', 'pending')
    )
    id = models.BigAutoField(primary_key=True)
    comment = models.ForeignKey(Comment, models.DO_NOTHING)
    reported_at = models.DateTimeField()
    state = models.CharField(max_length=255, choices=REPORT_STATE_CHOICES)

    class Meta:
        managed = False
        db_table = 'reports'
