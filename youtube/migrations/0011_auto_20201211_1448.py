# Generated by Django 3.1.4 on 2020-12-11 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0010_auto_20201211_1359'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='item',
            new_name='video',
        ),
        migrations.RenameField(
            model_name='like',
            old_name='item',
            new_name='video',
        ),
        migrations.AddField(
            model_name='like',
            name='test',
            field=models.CharField(default='', max_length=2),
            preserve_default=False,
        ),
    ]
