
from django.contrib import admin
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from django.http import HttpResponseRedirect

from . import views


urlpatterns = [
    url(r'^address/', views.street_create, name='go_street'),
    url(r'^(?P<pk>\d+)/detail/$', views.street_detail, name='detail_street'),
    url(r'^(?P<pk>\d+)/up-image/$', views.street_image, name='img_street'),
]
