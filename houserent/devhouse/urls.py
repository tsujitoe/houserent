from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^new/591/$', views.url_dev, name='get_url'),
	url(r'^(?P<pk>\d+)/new/591/$', views.get_work, name='url_work'),
	url(r'^(?P<pk>\d+)/591/$', views.url_list, name='url_list'),

	url(r'^new/good/$', views.url_dev_good, name='get_url_good'),
	url(r'^(?P<pk>\d+)/new/good/$', views.get_work_good, name='url_work_good'),
	url(r'^(?P<pk>\d+)/good/$', views.url_list_good, name='url_list_good'),

	#url(r'^$', views.suite_list, name='suite_list'),
	#url(r'^(?P<pk>\d+)/$', views.suite_detail, name='suite_detail'),
	#url(r'^(?P<pk>\d+)/update/$', views.suite_update, name='suite_update'),url(r'^model_form_upload/$', views.model_form_upload),
]