from django.urls import path
from .views import index



from django.conf.urls import include, url
from django.contrib import admin
from .views import rainfall, ph_rain, rain_cond

urlpatterns = [
    # url('admin/', include(admin.site.urls)),
    url('^$', index),
    url('ph_rain/', ph_rain),
    url('rain_cond/', rain_cond),
    url('rainfall/', rainfall),

]