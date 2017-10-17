from KinesisClient import KinesisClient
from datetime import datetime

class DemandStreamConsumer(object):
	client 	= None

	def __init__(self, config_path):
		self.client = KinesisClient(config_path).connect()
		return

	def consume(self, stream_name, shard_itr_type):
		stream_desc = self.client.describe_stream(StreamName=stream_name)
		shard_id 	= stream_desc['StreamDescription']['Shards'][0]['ShardId']
		print(stream_desc	)
		shard_itr 	= self.client.get_shard_iterator(StreamName=stream_name, 
													 ShardId="shardId-000000000001", 
													 ShardIteratorType=shard_itr_type)['ShardIterator']

		response 	= self.client.get_records(ShardIterator=shard_itr)
		return response

if __name__ == "__main__":
	import os
	config_path = os.path.join('..','config','config.xml')
	consumer 	= DemandStreamConsumer(config_path)
	resp 		= consumer.consume("grab-demand-stream", "TRIM_HORIZON")
	print(resp)