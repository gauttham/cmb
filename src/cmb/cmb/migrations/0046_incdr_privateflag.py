# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-06-14 06:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmb', '0045_auto_20180613_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='incdr',
            name='privateFlag',
            field=models.BooleanField(default=False),
        ),
    ]
