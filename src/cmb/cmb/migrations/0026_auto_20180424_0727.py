# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-24 07:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmb', '0025_auto_20180423_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bulkloadhistory',
            name='end',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bulkloadhistory',
            name='errorCount',
            field=models.IntegerField(null=True),
        ),
    ]
