# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-31 03:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bases', '0006_auto_20161025_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bailarines',
            name='edad_bailarin',
            field=models.IntegerField(),
        ),
    ]