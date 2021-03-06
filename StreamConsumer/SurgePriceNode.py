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

	def __consumeStream(self, delay):
		result 					= {}
		time_now 				= datetime.now()
		offset 					= timedelta(hours=8, minutes=delay).total_seconds()

		result["timestamp"] 	= time_now
		result["locationid"] 	= 237
		result["demand"] 		= self.dd_consumer.consume("grab-demand-stream", 
												time_now.replace(tzinfo=tzoffset("Offset", offset)))

		result["supply"] 		= self.ss_consumer.consume("grab-supply-stream", 
												time_now.replace(tzinfo=tzoffset("Offset", offset)))
		return result

	def getRealtimeData(self, delay):
		res 	= self.__consumeStream(delay)
		print("(SurgePriceNode) Updating DB")
		self.sp_dao.create(res)
		print("(SurgePriceNode) Finished updates to DB")
		return 

if __name__ == "__main__":
	import os
	import time
	
	while(True):
		delay 			= 10 	#Minutes
		kinesis_config 	= os.path.join(os.getcwd(),'Kinesis','config','config.xml')
		db_config 		= os.path.join(os.getcwd(),'HistoricalDAO','config','config.xml')
		sp 				= SurgePriceNode(kinesis_config, db_config)
		sp.getRealtimeData(delay)
		time.sleep(delay * 60)