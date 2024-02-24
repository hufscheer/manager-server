from django.db import models

class CheerTalk(models.Model): 
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField()
    content = models.CharField(max_length=255)
    is_blocked = models.BooleanField(default=False)
    game_team_id = models.BigIntegerField()

    @property
    def is_bool_blocked(self):
        return self.is_blocked == b'\x01'

    class Meta:
        db_table = 'cheer_talks'