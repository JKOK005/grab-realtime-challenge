import psycopg2
from HistoricalDbAuth import HistoricalDbAuth

class SurgePriceDao(object):
	table_name 	= "SurgePrice"
	schema 		= "public"
	db_auth 	= None

	def __init__(self, config_path):
		self.db_auth 	= HistoricalDbAuth(config_path)

	def create(self, dict):
		timestamp 	= dict['timestamp']
		demand 		= dict['demand']
		supply 		= dict['supply']
		locationid 	= dict['locationid']

		conn 	= self.db_auth.getDbInstance()
		cursor 	= conn.cursor()
		try:
			command = """ INSERT INTO {0}."{1}" (timestamp, demand, supply, locationid) 
						VALUES ('{2}',{3},{4},{5}) """.format(self.schema, 
															  self.table_name,
															  timestamp,
															  demand,
															  supply,
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
				"demand" 		: 100,
				"supply" 		: 200,
				"locationid" 	: 245,}
	dao.create(data)
