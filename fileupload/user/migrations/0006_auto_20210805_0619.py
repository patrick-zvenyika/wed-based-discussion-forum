# Generated by Django 3.2.2 on 2021-08-05 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='dislikes',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='question',
            name='likes',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='response',
            name='dislikes',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='response',
            name='likes',
            field=models.IntegerField(default='0'),
        ),
    ]