from KinesisClient import KinesisClient
from datetime import datetime, timedelta
from dateutil.tz import tzoffset
from StreamConsumer import StreamConsumer

class SupplyStreamConsumer(StreamConsumer):
	client 	= None

	def __init__(self, config_path):
		super(SupplyStreamConsumer, self).__init__()
		self.client = KinesisClient(config_path).connect()
		return

	def consume(self, stream_name, from_time_stamp):
		ss_count 	= 0
		response 	= self.consumeFirstInstance(stream_name, from_time_stamp)
		result 		= response['Records']

		# Add supply processing logic here
		while("NextShardIterator" in response and result):
			ss_count 		+= len(result)
			next_shard_itr 	= response['NextShardIterator']
			response 		= self.client.get_records(ShardIterator=next_shard_itr)
			result 			= response['Records']
		return ss_count

if __name__ == "__main__":
	import os
	config_path = os.path.join('..','config','config.xml')
	consumer 	= SupplyStreamConsumer(config_path)
	print("Consuming stream data at time: {0}".format(str(datetime.now())))

	resp 		= consumer.consume("grab-supply-stream", datetime(2017,10,17,19,51,50, 
									tzinfo=tzoffset("Offset", timedelta(hours=8))))
	print("Stream data consumed at time: {0}".format(str(datetime.now())))