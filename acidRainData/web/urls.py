from django.urls import path
from django.conf.urls import include, url
from django.contrib import admin
from .views import index, rainfall, ph_rain, rain_cond

urlpatterns = [
    url(r'^$', index),
    url(r'ph_rain/', ph_rain),
    url(r'rain_cond/', rain_cond),
    url(r'rainfall/', rainfall),
]