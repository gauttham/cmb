# Generated by Django 2.0.3 on 2018-03-23 23:22

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='beepCDR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calledNumber', models.IntegerField()),
                ('callerNumber', models.IntegerField()),
                ('callStartTime', models.DateTimeField()),
                ('createdDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('updatedDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('createdBy', models.CharField(default='Khal Drogo', max_length=100)),
                ('updatedBy', models.CharField(default='Khal Drogo', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DaInCdrMap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valueBeforeCall', models.FloatField()),
                ('valueAfterCall', models.FloatField()),
                ('createdDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('updatedDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('createdBy', models.CharField(default='Khal Drogo', max_length=100)),
                ('updatedBy', models.CharField(default='Khal Drogo', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DedicatedAccount',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('product', models.CharField(max_length=100)),
                ('createdDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('updatedDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('createdBy', models.CharField(default='Khal Drogo', max_length=100)),
                ('updatedBy', models.CharField(default='Khal Drogo', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ExceptionList',
            fields=[
                ('msisdn', models.IntegerField(primary_key=True, serialize=False)),
                ('createdDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('updatedDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('createdBy', models.CharField(default='Khal Drogo', max_length=100)),
                ('updatedBy', models.CharField(default='Khal Drogo', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Freebies',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('createdDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('updatedDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('createdBy', models.CharField(default='Khal Drogo', max_length=100)),
                ('updatedBy', models.CharField(default='Khal Drogo', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FreebiesType',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('createdDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('updatedDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('createdBy', models.CharField(default='Khal Drogo', max_length=100)),
                ('updatedBy', models.CharField(default='Khal Drogo', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='msisdnType',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PrepaidInCdr',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('accountValueBeforeCall', models.FloatField()),
                ('accountValueAfterCall', models.FloatField()),
                ('callCharge', models.FloatField()),
                ('chargedDuration', models.IntegerField()),
                ('callStartTime', models.DateTimeField()),
                ('callerNumber', models.IntegerField()),
                ('calledNumber', models.IntegerField()),
                ('redirectingNumber', models.IntegerField(null=True)),
                ('GsmCallRefNumber', models.CharField(max_length=100)),
                ('presentationIndicator', models.IntegerField()),
                ('revenueShared', models.FloatField(null=True)),
                ('reason', models.CharField(blank=True, max_length=100)),
                ('createdDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('updatedDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('createdBy', models.CharField(default='Khal Drogo', max_length=100)),
                ('updatedBy', models.CharField(default='Khal Drogo', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RevenueConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BeepToCallGap', models.IntegerField(default=60)),
                ('isActive', models.BooleanField(default=False)),
                ('createdDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('updatedDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('createdBy', models.CharField(default='Khal Drogo', max_length=100)),
                ('updatedBy', models.CharField(default='Khal Drogo', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceClass',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=50)),
                ('isRevenueShare', models.BooleanField(default=False)),
                ('inMobilesPercentage', models.IntegerField(default=50, null=True)),
                ('otherOperatorPercentage', models.IntegerField(default=50, null=True)),
                ('createdDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('updatedDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('createdBy', models.CharField(default='Khal Drogo', max_length=100)),
                ('updatedBy', models.CharField(default='Khal Drogo', max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='prepaidincdr',
            name='serviceClass',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmb.ServiceClass'),
        ),
        migrations.AddField(
            model_name='exceptionlist',
            name='msisdnType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmb.msisdnType'),
        ),
        migrations.AddField(
            model_name='dedicatedaccount',
            name='sub_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmb.FreebiesType'),
        ),
        migrations.AddField(
            model_name='dedicatedaccount',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmb.Freebies'),
        ),
        migrations.AddField(
            model_name='daincdrmap',
            name='DedicatedAccount',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmb.DedicatedAccount'),
        ),
        migrations.AddField(
            model_name='daincdrmap',
            name='PrepaidInCdr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmb.PrepaidInCdr'),
        ),
    ]
