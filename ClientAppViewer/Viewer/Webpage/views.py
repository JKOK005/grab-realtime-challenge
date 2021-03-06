import json
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView, View
from Webpage.RealtimeDataDAO import RealtimeDataDAOFactory
from Webpage.SurgePriceCalculatorMixin import *	
from dateutil import parser

class MainPage(TemplateView):
	template_name 	= "charts.html"

class SurgePriceCalculator(SurgePriceCalculatorMixin, View):
	def __init__(self, *args, **kwargs):
		super(SurgePriceCalculator, self).__init__(*args, **kwargs)

	def post(self, request, *args, **kwargs):
		data_dao 	= RealtimeDataDAOFactory.getDAO("surgeprice")
		model_obj 	= data_dao.getLatestData()
		sp 			= self.getSurgePrice(model_obj)
		timestamp 	= model_obj.timestamp
		resp_dict 	= { 'surgeprice' 	: sp,
						'timestamp' 	: timestamp,}
		return JsonResponse({"results" : resp_dict})

class TrafficStatus(View):
	def post(self, request, *args, **kwargs):
		data_dao 	= RealtimeDataDAOFactory.getDAO("traffic")
		model_obj 	= data_dao.getLatestData()
		avg_speed 	= model_obj.avgspeed
		timestamp 	= model_obj.timestamp
		resp_dict 	= { 'avgspeed' 		: avg_speed,
						'timestamp' 	: timestamp,}
		return JsonResponse({"results" : resp_dict})

class DemandSupplyDistribution(View):
	def post(self, request, *args, **kwargs):
		resp_dict 	= { 'demand' 	: [],
						'supply' 	: [],
						'timestamp' : [],}
		try:
			start 		= parser.parse(request.POST['start'])
			end 		= parser.parse(request.POST['end'])
			data_dao 	= RealtimeDataDAOFactory.getDAO("surgeprice")
			model_obj 	= data_dao.getTimestampRange(start, end)

			for each_model in model_obj:
				resp_dict['demand'].append(each_model.demand)
				resp_dict['supply'].append(each_model.supply)
				resp_dict['timestamp'].append(each_model.timestamp)
		except Exception as ex:
			pass 
		return JsonResponse({"results" : resp_dict})

class TrafficDistribution(View):
	def post(self, request, *args, **kwargs):
		resp_dict 	= { 'avgspeed' 	: [],
						'timestamp' : [],}
		try:
			start 		= parser.parse(request.POST['start'])
			end 		= parser.parse(request.POST['end'])
			data_dao 	= RealtimeDataDAOFactory.getDAO("traffic")
			model_obj 	= data_dao.getTimestampRange(start, end)

			for each_model in model_obj:
				resp_dict['avgspeed'].append(each_model.avgspeed)
				resp_dict['timestamp'].append(each_model.timestamp)
		except Exception as ex:
			pass

		return JsonResponse({"results" : resp_dict})