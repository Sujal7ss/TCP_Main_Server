# Generated by Django 4.2.9 on 2024-01-28 19:25

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mentee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mentor_id', models.IntegerField(blank=True, default=0, null=True)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(max_length=200, unique=True)),
                ('password', models.CharField(max_length=200)),
                ('branch', models.CharField(max_length=10)),
                ('semester', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(8)])),
                ('phone_number', models.CharField(max_length=10, unique=True)),
                ('image', models.URLField(blank=True, default='https://avatars.githubusercontent.com/u/5783068?v=4', max_length=300, null=True)),
                ('codechefID', models.URLField(max_length=100)),
                ('codeforcesID', models.URLField(max_length=100)),
                ('leetcodeID', models.URLField(max_length=100)),
                ('gfgID', models.URLField(max_length=100)),
                ('hackerrankID', models.URLField(max_length=100, null=True)),
                ('linkedinID', models.URLField(max_length=100)),
                ('score', models.BigIntegerField(default=0)),
                ('topic_count', models.JSONField(blank=True, default=dict, null=True)),
                ('total_q', models.BigIntegerField(default=0)),
                ('solvedQ', models.BigIntegerField(default=0)),
                ('Qlevel_count', models.JSONField(blank=True, default=dict, null=True)),
                ('cumHour_diff', models.BigIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=200)),
                ('branch', models.CharField(choices=[('1', 'CSE'), ('2', 'IT'), ('3', 'ECE'), ('4', 'ELEC'), ('5', 'MECH'), ('6', 'CHEM'), ('7', 'CIVIL'), ('8', 'META'), ('9', 'MIN'), ('10', 'BIOMED'), ('11', 'BIOTECH'), ('12', 'MCA')], max_length=10)),
                ('semester', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(8)])),
                ('phone_number', models.CharField(max_length=10, unique=True)),
                ('image', models.URLField(blank=True, default='https://avatars.githubusercontent.com/u/5783068?v=4', max_length=300, null=True)),
                ('codechefID', models.URLField(blank=True, max_length=100, null=True)),
                ('codeforcesID', models.URLField(blank=True, max_length=100, null=True)),
                ('leetcodeID', models.URLField(blank=True, max_length=100, null=True)),
                ('gfgID', models.URLField(blank=True, max_length=100, null=True)),
                ('hackerrankID', models.URLField(blank=True, max_length=100, null=True)),
                ('linkedinID', models.URLField(max_length=100)),
                ('score', models.BigIntegerField(default=0)),
                ('total_q', models.BigIntegerField(default=0)),
                ('topic_count', models.JSONField(blank=True, default=dict, null=True)),
                ('Qlevel_count', models.JSONField(blank=True, default=dict, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=50)),
                ('team_score', models.IntegerField(default=0)),
                ('cumHour_diff', models.BigIntegerField(default=0)),
                ('alloted_mentor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='clients.mentor')),
                ('team_members', models.ManyToManyField(to='clients.mentee')),
            ],
        ),
        migrations.AddField(
            model_name='mentee',
            name='Menteeteam',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='clients.team'),
        ),
    ]
