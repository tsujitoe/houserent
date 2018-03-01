from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.suite_list, name='suite_list'),
	url(r'^(?P<pk>\d+)/$', views.suite_detail, name='suite_detail'),
	url(r'^new/$', views.suite_create, name='suite_create'),
	url(r'^(?P<pk>\d+)/update/$', views.suite_update, name='suite_update'),
	url(r'^(?P<pk>\d+)/update_room/$', views.rooms_update, name='rooms_update'),
	url(r'^(?P<pk>\d+)/update_photo/$', views.photo_update, name='update_photo'),
	#url(r'^model_form_upload/$', views.model_form_upload),
]