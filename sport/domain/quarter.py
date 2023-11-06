from django.db import models

class Quarter(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    sports = models.ForeignKey('Sport', models.CASCADE)

    class Meta:
        managed = False
        db_table = 'quarters'