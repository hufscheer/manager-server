from django.db import models

class Organization(models.Model): 
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'organizations'