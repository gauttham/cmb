# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-04 03:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmb', '0009_bulkloader'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prepaidincdr',
            name='createdDate',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='prepaidincdr',
            name='updatedDate',
            field=models.DateTimeField(auto_now=True),
        ),
    ]