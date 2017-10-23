from Kinesis.scripts.TrafficLogStreamConsumer import TrafficLogStreamConsumer
from HistoricalDAO.scripts.TrafficLogDao import TrafficLogDao
from datetime import datetime, timedelta
from dateutil.tz import tzoffset

class TrafficLogNode(object):
	tl_consumer 	= None
	tl_dao 			= None

	def __init__(self, kinesis_config, db_config):
		self.tl_consumer 	= TrafficLogStreamConsumer(kinesis_config)
		self.tl_dao 		= TrafficLogDao(db_config)

	def __consumeStream(self, delay):
		result 					= {}
		time_now 				= datetime.now()
		resp 					= self.tl_consumer.consume("grab-traffic-log-stream", 
												time_now.replace(tzinfo=tzoffset("Offset", timedelta(hours=8, minutes=delay))))

		result["timestamp"] 	= time_now
		result["avgspeed"] 		= resp
		result["locationid"] 	= 237
		return result

	def getRealtimeData(self, delay):
		res 	= self.__consumeStream(delay)
		print("(TrafficLogNode) Updating DB")
		self.tl_dao.create(res)
		print("(TrafficLogNode) Finished updates to DB")
		return 

if __name__ == "__main__":
	import os
	import time

	while(True):
		delay 			= 10 	#Minutes
		kinesis_config 	= os.path.join(os.getcwd(),'Kinesis','config','config.xml')
		db_config 		= os.path.join(os.getcwd(),'HistoricalDAO','config','config.xml')
		tl 				= TrafficLogNode(kinesis_config, db_config)
		tl.getRealtimeData(delay)
		time.sleep(10)