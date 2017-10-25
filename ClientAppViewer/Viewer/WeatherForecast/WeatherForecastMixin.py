import os
import requests
import json

class WeatherUndergroundMixin(object):
	__url_template 	= "http://api.wunderground.com/api/{0}/history_{1}/q/{2}/{3}.json"
	__api_key 		= os.environ.get("weather_apikey")
	__state 		= None
	__district 		= None
	__query_date 	= None

	def __init__(self, *args, **kwargs):
		super(WeatherUndergroundMixin, self).__init__(*args, **kwargs)

	def setUrlState(self, state):
		self.__state 	= state
		return self

	def setUrlDistrict(self, district):
		self.__district = district
		return self

	def setUrlQueryDate(self, date):
		self.__query_date = date
		return self

	def getUrl(self):
		return self.__url_template.format(self.__api_key, self.__query_date, self.__state, self.__district)

	def call(self):
		resp 	= requests.get(self.getUrl())
		if(resp.status_code == 200):
			decode_str = resp.content.decode('utf-8')
			return json.loads(decode_str)
		return None

	def getContent(self, resp):
		return resp['history']

	def getResponseDict(self, contents):
		def parseDateString(hh, mm):
			return str(hh) + ":" + str(mm)

		def parse(val):
			value  	= float(val)
			if value < 0:
				return 0
			return value

		resp_dict 	= {	'windspeed' 	: [],
						'temp' 			: [],
						'humidity' 		: [],
						'timestamp' 	: [],
		}

		for each_observe in contents['observations']:
			resp_dict['windspeed'].append(parse(each_observe['wspdm']))
			resp_dict['temp'].append(parse(each_observe['tempm']))
			resp_dict['humidity'].append(parse(each_observe['hum']))
			resp_dict['timestamp'].append(parseDateString(each_observe['utcdate']['hour'], 
														  each_observe['utcdate']['min']))
		return resp_dict