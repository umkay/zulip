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

        migrations.AlterUniqueTogether(
            name='installationcount',
            unique_together=set([('property', 'end_time', 'interval', 'subgroup')]),
        ),
        migrations.AlterUniqueTogether(
            name='realmcount',
            unique_together=set([('realm', 'property', 'end_time', 'interval', 'subgroup')]),
        ),
        migrations.AlterUniqueTogether(
            name='streamcount',
            unique_together=set([('stream', 'property', 'end_time', 'interval', 'subgroup')]),
        ),
        migrations.AlterUniqueTogether(
            name='usercount',
            unique_together=set([('user', 'property', 'end_time', 'interval', 'subgroup')]),
        ),
    ]
