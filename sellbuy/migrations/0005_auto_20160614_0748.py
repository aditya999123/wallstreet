# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-14 07:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellbuy', '0004_auto_20160614_0410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sharedetail',
            name='id',
            field=models.PositiveSmallIntegerField(primary_key='True', serialize=False),
        ),
    ]
