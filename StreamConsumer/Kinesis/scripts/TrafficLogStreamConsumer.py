from KinesisClient import KinesisClient
from datetime import datetime, timedelta
from dateutil.tz import tzoffset
from StreamConsumer import StreamConsumer
import json

class TrafficLogStreamConsumer(StreamConsumer):
	client 	= None

	def __init__(self, config_path):
		super(TrafficLogStreamConsumer, self).__init__()
		self.client = KinesisClient(config_path).connect()
		return

	def __getAvgSpeed(self, results):
		avg_speed 	= 0
		counter 	= 0

		for each_result in results:
			Data 			= json.loads(each_result['Data'])
			travel_time 	= Data['data']['travelTime']
			distance 		= float((Data['data']['distance']))

			if(travel_time > 0 and distance > 0):
				tmp_speed 	= distance / travel_time
				avg_speed 	= (avg_speed*counter + tmp_speed) / (counter +1)
				counter 	+= 1
		return avg_speed

	def consume(self, stream_name, from_time_stamp):
		avg_speed 	= None
		response 	= self.consumeFirstInstance(stream_name, from_time_stamp)
		results		= response['Records']

		# Add demand processing logic here
		while("NextShardIterator" in response and results):
			avg_speed  		= self.__getAvgSpeed(results)
			next_shard_itr 	= response['NextShardIterator']
			response 		= self.client.get_records(ShardIterator=next_shard_itr)
			results 		= response['Records']
		return avg_speed

if __name__ == "__main__":
	import os
	config_path = os.path.join('..','config','config.xml')
	consumer 	= TrafficLogStreamConsumer(config_path)
	print("Consuming stream data at time: {0}".format(str(datetime.now())))

	resp 		= consumer.consume("grab-traffic-log-stream", datetime(2017,10,17,19,51,50, 
									tzinfo=tzoffset("Offset", timedelta(hours=8))))
	print("Stream data consumed at time: {0}".format(str(datetime.now())))
