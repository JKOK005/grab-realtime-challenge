from django.conf.urls import url, include
from Webpage.views import *

urlpatterns = [
    url(r'^$', MainPage.as_view(), name="main-page"),
    url(r'^get-surgeprice/latest', SurgePriceCalculator.as_view(), name="surgeprice-latest"),
    url(r'^get-demandsupply/range', DemandSupplyDistribution.as_view(), name="demand-supply-latest"),
    url(r'^get-traffic/latest', TrafficStatus.as_view(), name="traffic-latest"),
    url(r'^get-traffic/range', TrafficDistribution.as_view(), name="traffic-range"),
]
