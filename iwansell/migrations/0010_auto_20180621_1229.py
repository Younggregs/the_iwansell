# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-06-21 12:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwansell', '0009_auto_20180621_1229'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subcategory',
            options={'ordering': ['id']},
        ),
    ]