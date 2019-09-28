# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-09-28 16:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_remove_order_county'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='country',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='order',
            name='postcode',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='street_address2',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='order',
            name='town_or_city',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]
