from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from WeatherForecast.WeatherForecastMixin import *

class WeatherDistribution(WeatherUndergroundMixin, View):
	def __init__(self, *args, **kwargs):
		super(WeatherDistribution, self).__init__(*args, **kwargs)

	def post(self, request, *args, **kwargs):
		date 		= request.POST['date']
		resp 		= self.setUrlState("ny").setUrlDistrict("upper_east_side").setUrlQueryDate(date).call()
		contents 	= self.getContent(resp)
		resp_dict 	= self.getResponseDict(contents)
		return JsonResponse({"results" : resp_dict})	