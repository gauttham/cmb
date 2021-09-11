# Generated by Django 2.0.3 on 2018-03-27 11:33

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cmb', '0003_auto_20180327_0634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beepcdr',
            name='createdDate',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='beepcdr',
            name='updatedDate',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='daincdrmap',
            name='PrepaidInCdr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dedicatedAccounts', to='cmb.PrepaidInCdr'),
        ),
        migrations.AlterField(
            model_name='daincdrmap',
            name='createdDate',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='daincdrmap',
            name='updatedDate',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='dedicatedaccount',
            name='createdDate',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='dedicatedaccount',
            name='updatedDate',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='exceptionlist',
            name='createdDate',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='exceptionlist',
            name='updatedDate',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='freebies',
            name='createdDate',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='freebies',
            name='updatedDate',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='freebiestype',
            name='createdDate',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='freebiestype',
            name='updatedDate',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='prepaidincdr',
            name='createdDate',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='prepaidincdr',
            name='updatedDate',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='revenueconfig',
            name='createdDate',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='revenueconfig',
            name='updatedDate',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='serviceclass',
            name='createdDate',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='serviceclass',
            name='updatedDate',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
