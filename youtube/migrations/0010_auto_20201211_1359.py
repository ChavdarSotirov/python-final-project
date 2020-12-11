# Generated by Django 3.1.4 on 2020-12-11 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0009_auto_20201211_1347'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='video_url',
        ),
        migrations.AddField(
            model_name='video',
            name='video_file',
            field=models.FileField(default='upload video file', upload_to='videos/'),
            preserve_default=False,
        ),
    ]
