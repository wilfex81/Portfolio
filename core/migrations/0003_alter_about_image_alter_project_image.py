# Generated by Django 4.0.5 on 2022-11-09 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_project_github_name_project_liver_server_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
