# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-25 23:44
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('bases', '0005_remove_instructor_danza_nombre_bailarin'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='bailarines',
            managers=[
                ('manager', django.db.models.manager.Manager()),
            ],
        ),
    ]
