from django.conf.urls import url, include
from Webpage.views import *

urlpatterns = [
    url(r'^$', MainPage.as_view(), name="main-page"),
]
