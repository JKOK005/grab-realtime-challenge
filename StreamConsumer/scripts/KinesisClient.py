import xmltodict
import boto3

class KinesisClient(object):
	config_path 	= None
	config_ref 		= None

	def __init__(self, config_path):
		self.config_path 	= config_path

		with open(config_path) as config_file:
			self.config_ref 	= xmltodict.parse(config_file.read())
		return

	def __getConfig(self, config_str):
		name 	= self.config_ref['aws-kinesis']['configuration'][config_str]
		return name.encode('ascii')

	def connect(self):
		access_key 	= self.__getConfig("access-key")
		secret_key 	= self.__getConfig("secret-key")
		region 		= self.__getConfig("region")
		client 		= boto3.client('kinesis', aws_access_key_id=access_key, 
									aws_secret_access_key=secret_key, 
									region_name=region)
		return client

if __name__ == "__main__":
	import os
	config_path 	= os.path.join('..','config','config.xml')
	client 	= KinesisClient(config_path).connect()
	stream 	= client.describe_stream(StreamName="grab-demand-stream")
	print(stream)	
