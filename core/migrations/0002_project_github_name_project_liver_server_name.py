# Generated by Django 4.0.5 on 2022-10-16 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='github_name',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AddField(
            model_name='project',
            name='liver_server_name',
            field=models.CharField(blank=True, max_length=120),
        ),
    ]
