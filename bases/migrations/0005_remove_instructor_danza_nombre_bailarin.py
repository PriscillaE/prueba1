# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-14 07:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bases', '0004_instructor_danza_nombre_bailarin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instructor_danza',
            name='nombre_bailarin',
        ),
    ]