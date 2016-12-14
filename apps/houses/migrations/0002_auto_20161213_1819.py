# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-13 18:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('trade_goods', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='house',
            name='region',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='houses.Region'),
        ),
    ]