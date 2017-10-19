import psycopg2
import xmltodict

class HistoricalDbAuth(object):
	config_ref 		= None
	config_path 	= None
	conn 			= None

	def __init__(self, config_path):
		self.config_path 	= config_path

		with open(config_path) as config_file:
			self.config_ref 	= xmltodict.parse(config_file.read())
		return

	def __getConfig(self, config_str):
		name 	= self.config_ref['aws-rds']['configuration'][config_str]
		return name.encode('ascii')

	def getDbInstance(self):
		if(self.conn is not None):
			return self.conn

		host 		= self.__getConfig("url")
		port 		= self.__getConfig("port")
		user_name 	= self.__getConfig("username")
		password 	= self.__getConfig("password")
		dbname 		= self.__getConfig("dbname")

		try:
			conn 	= psycopg2.connect(	dbname=dbname,
										user=user_name,
										password=password,
										host=host,
										port=port
									)	
		except Exception as ex:
			print(ex)

		self.conn = conn
		return self.conn

if __name__ == "__main__":
	import os
	config_path 	= os.path.join('..','config','config.xml')
	dao 	= HistoricalDbAuth(config_path)
	cursor 	= dao.getDbInstance()
	import IPython
	IPython.embed()