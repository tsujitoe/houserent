from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^new/$', views.url_dev, name='get_url'),
	url(r'^(?P<pk>\d+)/new/$', views.get_work, name='url_work'),
	url(r'^(?P<pk>\d+)$', views.url_list, name='url_list'),

	#url(r'^$', views.suite_list, name='suite_list'),
	#url(r'^(?P<pk>\d+)/$', views.suite_detail, name='suite_detail'),
	#url(r'^(?P<pk>\d+)/update/$', views.suite_update, name='suite_update'),url(r'^model_form_upload/$', views.model_form_upload),
]