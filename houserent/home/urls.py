from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home_info_list, name='home_list'),
    url(r'^update_home/$', views.home_info_create, name='update_home'),
    url(r'^(?P<pk>\d+)/$', views.home_info_detail, name='home_info_detail'),
    url(r'^(?P<pk>\d+)/home_info_update/$', views.home_info_update, name='home_info_update'),
    url(r'^(?P<pk>\d+)/photo_create/$', views.photo_create, name='photo_create'),

    #url(r'^upload$', views.post_upload_images_test_database, name='post'),
    
]
