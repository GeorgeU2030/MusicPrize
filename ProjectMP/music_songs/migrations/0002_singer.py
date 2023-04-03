# Generated by Django 4.1.7 on 2023-03-19 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_songs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Singer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
                ('country', models.TextField(max_length=10)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='imagebd/')),
                ('flag', models.ImageField(blank=True, null=True, upload_to='imagebd/')),
                ('points', models.IntegerField(max_length=10000000)),
                ('awards', models.IntegerField(max_length=10000000)),
            ],
        ),
    ]