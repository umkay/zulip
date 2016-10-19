# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0003_fillstate'),
    ]

    operations = [
        migrations.AddField(
            model_name='installationcount',
            name='subgroup',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='realmcount',
            name='subgroup',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='streamcount',
            name='subgroup',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='usercount',
            name='subgroup',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='installationcount',
            name='interval',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='installationcount',
            name='property',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='realmcount',
            name='interval',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='realmcount',
            name='property',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='streamcount',
            name='interval',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='streamcount',
            name='property',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='usercount',
            name='interval',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='usercount',
            name='property',
            field=models.CharField(max_length=32),
        ),
    ]
