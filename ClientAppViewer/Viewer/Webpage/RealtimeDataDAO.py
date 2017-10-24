from Webpage.models import *

class SurgePricingDAO(object):
	def getLatestData(self):
		return Surgeprice.objects.all().order_by('-timestamp').first()

	def getTimestampRange(self, start, end):
		return Surgeprice.objects.filter(timestamp__range=(start, end))

class TrafficLogsDAO(object):
	def getLatestData(self):
		return Trafficlog.objects.all().order_by('-timestamp').first()

	def getTimestampRange(self, start, end):
		return Trafficlog.objects.filter(timestamp__range=(start, end))

class GeohashDAO(object):
	def getLocation(id):
		return Geohash.objects.filter(locationid=id).first()

class RealtimeDataDAOFactory(object):
	mapping 	= { 'surgeprice' 	: SurgePricingDAO(),
					'traffic' 		: TrafficLogsDAO(),
					'geohash' 		: GeohashDAO(),
				}

	@classmethod
	def getDAO(cls, dao_string):
		return cls.mapping[dao_string]