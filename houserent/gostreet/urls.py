from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^address/', views.street_create, name='go_street'),
    url(r'^(?P<pk>\d+)/detail/$', views.street_detail, name='detail_street'),
    url(r'^(?P<pk>\d+)/up-detail/$', views.street_update, name='update_street'),
    url(r'^(?P<pk>\d+)/up-mul-image/$', views.street_mul_image, name='img_mul_street'),
    url(r'^(?P<pk>\d+)/up-image/$', views.street_image, name='img_street'),

    # for fake tenant
    url(r'^new/591/$', views.url_dev, name='get_url_fake'),
	url(r'^(?P<pk>\d+)/new/591/$', views.get_work, name='url_work_fake'),
	url(r'^(?P<pk>\d+)/591/$', views.url_list, name='url_list_fake'),
]
