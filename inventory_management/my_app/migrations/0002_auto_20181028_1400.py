# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-28 14:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invetoryrecord',
            name='Batch_Num',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='invetoryrecord',
            name='MRP',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='invetoryrecord',
            name='Quatity',
            field=models.IntegerField(null=True),
        ),
    ]
