from KinesisClient import KinesisClient
from datetime import datetime, timedelta
from dateutil.tz import tzoffset

class StreamConsumer(object):
	client 	= None

	def __init__(self):
		return

	def consumeFirstInstance(self, stream_name, time_stamp):
		stream_desc = self.client.describe_stream(StreamName=stream_name)
		shard_id 	= stream_desc['StreamDescription']['Shards'][0]['ShardId']
		shard_itr 	= self.client.get_shard_iterator(StreamName=stream_name, 
													 ShardId="shardId-000000000000", 
													 ShardIteratorType="AT_TIMESTAMP",
													 Timestamp=time_stamp)['ShardIterator']

		response 	= self.client.get_records(ShardIterator=shard_itr)
		return response