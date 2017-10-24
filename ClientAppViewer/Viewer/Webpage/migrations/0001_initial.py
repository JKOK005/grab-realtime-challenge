# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-24 11:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Geohash',
            fields=[
                ('locationid', models.IntegerField(primary_key=True, serialize=False)),
                ('district', models.TextField(blank=True, null=True)),
                ('city', models.TextField(blank=True, null=True)),
                ('state', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'geohash',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Surgeprice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('demand', models.IntegerField()),
                ('supply', models.IntegerField()),
            ],
            options={
                'db_table': 'surgeprice',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Trafficlog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('avgspeed', models.FloatField()),
            ],
            options={
                'db_table': 'trafficlog',
                'managed': False,
            },
        ),
    ]
