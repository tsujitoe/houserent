from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^address/', views.street_create, name='go_street'),
    url(r'^(?P<pk>\d+)/detail/$', views.street_detail, name='detail_street'),
    url(r'^(?P<pk>\d+)/up-detail/$', views.street_update, name='update_street'),
    url(r'^(?P<pk>\d+)/up-mul-image/$', views.street_mul_image, name='img_mul_street'),
    url(r'^(?P<pk>\d+)/up-image/$', views.street_image, name='img_street'),
]
