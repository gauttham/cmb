# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-29 08:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cmb', '0030_roles'),
    ]

    operations = [
        migrations.CreateModel(
            name='userRoles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='roles',
            name='users',
        ),
        migrations.AddField(
            model_name='userroles',
            name='roles',
            field=models.ManyToManyField(to='cmb.Roles'),
        ),
        migrations.AddField(
            model_name='userroles',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
