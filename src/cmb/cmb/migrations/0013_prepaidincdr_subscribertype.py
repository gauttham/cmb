# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-04 04:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmb', '0012_auto_20180404_0355'),
    ]

    operations = [
        migrations.AddField(
            model_name='prepaidincdr',
            name='subscriberType',
            field=models.IntegerField(default=1),
        ),
    ]
