# Generated by Django 4.2.4 on 2025-01-18 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0004_team_team_rank'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentee',
            name='Mentee_rank',
            field=models.IntegerField(default=0),
        ),
    ]
