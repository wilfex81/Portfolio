# Generated by Django 4.0.5 on 2022-06-02 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('live_server', models.URLField(blank=True)),
                ('github', models.URLField(blank=True)),
                ('image', models.ImageField(upload_to='uploads/% Y/% m/% d/')),
            ],
        ),
        migrations.RenameModel(
            old_name='Services',
            new_name='Service',
        ),
        migrations.DeleteModel(
            name='Projects',
        ),
    ]
