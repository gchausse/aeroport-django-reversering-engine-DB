# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Airport(models.Model):
    id_airport = models.BigAutoField(primary_key=True)
    name_airport = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'airport'


class Baggage(models.Model):
    id_baggage = models.BigAutoField(primary_key=True)
    weight_baggage = models.BigIntegerField(blank=True, null=True)
    id_passagers = models.ForeignKey('Passengers', models.DO_NOTHING, db_column='id_passagers', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'baggage'


class Compagny(models.Model):
    id_compagny = models.BigAutoField(primary_key=True)
    name_compagny = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'compagny'


class Crew(models.Model):
    id_crew = models.BigAutoField(primary_key=True)
    driver_crew = models.CharField(max_length=255, blank=True, null=True)
    copilot_crew = models.CharField(max_length=255, blank=True, null=True)
    id_compagny = models.ForeignKey(Compagny, models.DO_NOTHING, db_column='id_compagny', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crew'


class Flight(models.Model):
    id_flight = models.BigAutoField(primary_key=True)
    time_flight = models.CharField(max_length=255, blank=True, null=True)
    id_compagny = models.ForeignKey(Compagny, models.DO_NOTHING, db_column='id_compagny', blank=True, null=True)
    id_airport = models.ForeignKey(Airport, models.DO_NOTHING, db_column='id_airport', blank=True, null=True)
    id_airport_begining = models.ForeignKey(Airport, models.DO_NOTHING, db_column='id_airport_begining', blank=True, null=True, related_name='airoport_depart')

    class Meta:
        managed = False
        db_table = 'flight'


class Passengers(models.Model):
    id_passagers = models.BigAutoField(primary_key=True)
    first_name_passengers = models.CharField(max_length=255, blank=True, null=True)
    last_name_passengers = models.CharField(max_length=255, blank=True, null=True)
    id_flight = models.ForeignKey(Flight, models.DO_NOTHING, db_column='id_flight', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'passengers'


class Plane(models.Model):
    id_avion = models.BigAutoField(primary_key=True)
    mark_plane = models.CharField(max_length=255, blank=True, null=True)
    model_plane = models.CharField(max_length=255, blank=True, null=True)
    id_compagny = models.ForeignKey(Compagny, models.DO_NOTHING, db_column='id_compagny', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plane'
