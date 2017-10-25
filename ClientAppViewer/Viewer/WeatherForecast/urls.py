from django.conf.urls import url
from WeatherForecast.views import *

urlpatterns = [
    url(r'range', WeatherDistribution.as_view(), name="weather-range"),
]

