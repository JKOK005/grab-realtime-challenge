class RealtimeDataDAOFactory(object):
	mapping 	= { 'traffic' 		: "traffic",
					'surgeprice' 	: "surge_price"
				}

	@classmethod
	def getDAO(cls, dao_string):
		return cls.mapping[dao_string]

class SurgePricingDAO(object):
	def __init__(self):
		pass

class TrafficLogsDAO(object):
	def __init__(self):
		pass