# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-13 18:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0002_auto_20161213_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='region',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='houses.Region'),
        ),
    ]