# Generated by Django 4.2 on 2023-05-05 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0016_rename_email_adress_userprofile_email_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='nickname',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
