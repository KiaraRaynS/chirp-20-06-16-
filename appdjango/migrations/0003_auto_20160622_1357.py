# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-22 13:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appdjango', '0002_auto_20160622_1354'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='StopWork',
            new_name='StopWord',
        ),
    ]