# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-08-05 14:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0004_auto_20190731_1140'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='upvotes',
            options={'verbose_name_plural': 'Up votes'},
        ),
    ]
