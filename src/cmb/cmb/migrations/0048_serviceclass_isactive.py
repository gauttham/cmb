# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-06-14 10:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmb', '0047_serviceclass_privateflagcost'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceclass',
            name='isActive',
            field=models.BooleanField(default=True),
        ),
    ]
