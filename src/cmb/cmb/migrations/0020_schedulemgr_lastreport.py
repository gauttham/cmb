# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-15 07:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmb', '0019_schedulemgr'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedulemgr',
            name='lastReport',
            field=models.FileField(blank=True, null=True, upload_to=b'../reports/'),
        ),
    ]
