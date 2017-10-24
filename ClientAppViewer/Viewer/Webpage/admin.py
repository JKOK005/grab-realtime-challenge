from django.contrib import admin
from Webpage.models import *

@admin.register(Geohash)
class GeohashAdmin(admin.ModelAdmin):
	pass

@admin.register(Surgeprice)
class SurgepriceAdmin(admin.ModelAdmin):
	pass

@admin.register(Trafficlog)
class TrafficlogAdmin(admin.ModelAdmin):
	pass