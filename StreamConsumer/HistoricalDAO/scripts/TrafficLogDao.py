import psycopg2
from HistoricalDbAuth import HistoricalDbAuth

class TrafficLogDao(object):
	table_name 	= "TrafficLog"
	schema 		= "public"
	db_auth 	= None

	def __init__(self, config_path):
		self.db_auth 	= HistoricalDbAuth(config_path)

	def create(self, dict):
		timestamp 	= dict['timestamp']
		distance 	= dict['distance']
		travel_time = dict['traveltime']
		locationid 	= dict['locationid']

		conn 	= self.db_auth.getDbInstance()
		cursor 	= conn.cursor()
		try:
			command = """ INSERT INTO {0}."{1}" (timestamp, distance, traveltime, locationid) 
						VALUES ('{2}',{3},{4},{5}) """.format(self.schema, 
															  self.table_name,
															  timestamp,
															  distance,
															  travel_time,
															  locationid).encode('utf-8')
			print(command)
			cursor.execute(command)
			conn.commit()

		except Exception as ex:
			print(ex)

		cursor.close()
		conn.close()
		return

	def read(self):
		pass

	def delete(self):
		pass

	def update(self):
		pass

if __name__ == "__main__":
	from datetime import datetime
	import os

	config_path 	= os.path.join('..','config','config.xml')
	dao 	= SurgePriceDao(config_path)
	data 	= { "timestamp" 	: datetime.now(),
				"distance" 		: 100,
				"traveltime" 	: 200,
				"locationid" 	: 133,}
	dao.create(data)
