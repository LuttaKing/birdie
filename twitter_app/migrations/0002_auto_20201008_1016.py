# Generated by Django 3.1 on 2020-10-08 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lasttweetid',
            name='tweetId',
            field=models.IntegerField(),
        ),
    ]