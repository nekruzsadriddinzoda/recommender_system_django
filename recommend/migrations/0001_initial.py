# Generated by Django 3.0.6 on 2020-06-08 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('video_url', models.CharField(max_length=500)),
                ('movie_logo', models.FileField(upload_to='')),
            ],
        ),
    ]
