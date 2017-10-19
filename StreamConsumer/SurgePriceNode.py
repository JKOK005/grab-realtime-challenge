from Kinesis.scripts.DemandStreamConsumer import DemandStreamConsumer
from Kinesis.scripts.SupplyStreamConsumer import SupplyStreamConsumer
from HistoricalDAO.scripts.SurgePriceDao import SurgePriceDao
from datetime import datetime, timedelta
from dateutil.tz import tzoffset

class SurgePriceNode(object):
	dd_consumer  	= None
	ss_consumer 	= None
	sp_dao 			= None

	def __init__(self, kinesis_config, db_config):
		self.dd_consumer 	= DemandStreamConsumer(kinesis_config)
		self.ss_consumer 	= SupplyStreamConsumer(kinesis_config)
		self.sp_dao 		= SurgePriceDao(db_config)

	def __consumeStream(self):
		result 					= {}
		time_now 				= datetime.now()

		result["timestamp"] 	= time_now
		result["locationid"] 	= 357 
		result["demand"] 		= self.dd_consumer.consume("grab-demand-stream", 
												time_now.replace(tzinfo=tzoffset("Offset", timedelta(hours=8))))

		result["supply"] 		= self.ss_consumer.consume("grab-supply-stream", 
												time_now.replace(tzinfo=tzoffset("Offset", timedelta(hours=8))))
		return result

	def getRealtimeDate(self):
		res 	= self.__consumeStream()
		print(res)
		self.sp_dao.create(res)
		return 

if __name__ == "__main__":
	import os
	kinesis_config 	= os.path.join(os.getcwd(),'Kinesis','config','config.xml')
	db_config 		= os.path.join(os.getcwd(),'HistoricalDAO','config','config.xml')
	sp 		= SurgePriceNode(kinesis_config, db_config)
	sp.getRealtimeDate()
	sp.getRealtimeDate()
	sp.getRealtimeDate()
