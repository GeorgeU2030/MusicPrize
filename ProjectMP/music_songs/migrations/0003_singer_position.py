# Generated by Django 4.1.7 on 2023-03-20 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_songs', '0002_singer'),
    ]

    operations = [
        migrations.AddField(
            model_name='singer',
            name='position',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
