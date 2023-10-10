from django.db import models

class Comment(models.Model):
    id = models.BigAutoField(primary_key=True)
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    game = models.ForeignKey('Game', models.DO_NOTHING, blank=True, null=True)
    is_blocked = models.BooleanField(default=False)

    class Meta:
        managed = False
        db_table = 'comment'