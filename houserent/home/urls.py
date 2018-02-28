from django.conf.urls import url
from . import views


urlpatterns = [
    #url(r'^$', views.home_info_list, name='home_info_list'),
    url(r'^$', views.home_info_create, name='home'),
    url(r'^(?P<pk>\d+)/detail/$', views.home_info_detail, name='home_info_detail'),
    url(r'home_info_update/^$', views.home_info_update, name='home_info_update'),
    url(r'photo_create/^$', views.photo_create, name='photo_create'),

    #url(r'^upload$', views.post_upload_images_test_database, name='post'),
    
]
