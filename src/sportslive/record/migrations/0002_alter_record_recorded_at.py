# Generated by Django 4.2.5 on 2024-03-03 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='recorded_at',
            field=models.IntegerField(),
        ),
    ]
