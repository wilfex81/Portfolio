# Generated by Django 4.0.5 on 2022-11-11 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_rename_social_contacts_footer_linkedin_footer_twiter_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='image',
            field=models.ImageField(upload_to='images_from_admin/'),
        ),
    ]
