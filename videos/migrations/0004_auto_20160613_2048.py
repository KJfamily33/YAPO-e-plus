# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-13 17:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0003_auto_20160613_2043'),
    ]

    operations = [
        migrations.AddField(
            model_name='actortag',
            name='date_fav',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='actortag',
            name='date_runner_up',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='scenetag',
            name='date_fav',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='scenetag',
            name='date_runner_up',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='actor',
            name='date_fav',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='actor',
            name='date_runner_up',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]