import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, View
from Webpage.RealtimeDataDAO import RealtimeDataDAOFactory

class MainPage(TemplateView):
	template_name 	= "charts.html"

class ReturnRealTimeData(View):
	def get(self, request, *args, **kwargs):
		req 		= request.GET['data']
		data_dao 	= RealtimeDataDAOFactory.getDAO(req)
		print(data_dao)
		return HttpResponse("Get real time data")