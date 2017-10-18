from KinesisClient import KinesisClient
from datetime import datetime, timedelta
from dateutil.tz import tzoffset

class DemandStreamConsumer(object):
	client 	= None

	def __init__(self, config_path):
		self.client = KinesisClient(config_path).connect()
		return

	def consume(self, stream_name, time_stamp):
		stream_desc = self.client.describe_stream(StreamName=stream_name)
		shard_id 	= stream_desc['StreamDescription']['Shards'][0]['ShardId']
		shard_itr 	= self.client.get_shard_iterator(StreamName=stream_name, 
													 ShardId="shardId-000000000001", 
													 ShardIteratorType="AT_TIMESTAMP",
													 Timestamp=time_stamp)['ShardIterator']

		response 	= self.client.get_records(ShardIterator=shard_itr)
		return response

if __name__ == "__main__":
	import os
	config_path = os.path.join('..','config','config.xml')
	consumer 	= DemandStreamConsumer(config_path)
	resp 		= consumer.consume("grab-demand-stream", datetime(2017,10,17,19,51,50, 
									tzinfo=tzoffset("Offset by -8h", timedelta(hours=8))))
	print(resp['Records'])
