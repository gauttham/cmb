# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-15 05:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmb', '0016_prepaidincdr_micrevenue'),
    ]

    operations = [
        migrations.AddField(
            model_name='beepcdr',
            name='MCID',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='prepaidincdr',
            name='NCR',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
