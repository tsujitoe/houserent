from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.get_tenant, name='tenant_get'),
	url(r'^(?P<pk>\d+)$', views.list_tenant, name='tenant_list'),
	#url(r'^(?P<pk>\d+)/new/$', views.get_work, name='url_work'),
	#url(r'^(?P<pk>\d+)$', views.url_list, name='url_list'),
]