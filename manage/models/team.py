from django.db import models

class Team(models.Model):
    id = models.BigAutoField(primary_key=True)
    logo_image_url = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'team'