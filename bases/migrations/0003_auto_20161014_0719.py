# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-14 07:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bases', '0002_bailarines_instructor_danza'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainer',
            name='bailarin',
        ),
        migrations.AddField(
            model_name='instructor_danza',
            name='bailarin',
            field=models.ManyToManyField(to='bases.Bailarines'),
        ),
    ]
