# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

class Geohash(models.Model):
    locationid = models.IntegerField(primary_key=True)
    district = models.TextField(blank=True, null=True)  # This field type is a guess.
    city = models.TextField(blank=True, null=True)  # This field type is a guess.
    state = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'geohash'

class Surgeprice(models.Model):
    timestamp = models.DateTimeField()
    demand = models.IntegerField()
    supply = models.IntegerField()
    locationid = models.ForeignKey(Geohash, models.DO_NOTHING, db_column='locationid')

    class Meta:
        managed = False
        db_table = 'surgeprice'

class Trafficlog(models.Model):
    timestamp = models.DateTimeField()
    locationid = models.ForeignKey(Geohash, models.DO_NOTHING, db_column='locationid')
    avgspeed = models.FloatField()

    class Meta:
        managed = False
        db_table = 'trafficlog'
