from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.store_info_list, name='store_list'),
    url(r'^update_store/$', views.store_info_create, name='update_store'),
    url(r'^(?P<pk>\d+)/$', views.store_info_detail, name='store_info_detail'),
    url(r'^(?P<pk>\d+)/store_info_update/$', views.store_info_update, name='store_info_update'),
    url(r'^(?P<pk>\d+)/photo_create/$', views.photo_create, name='photo_create'),

    #url(r'^upload$', views.post_upload_images_test_database, name='post'),
    
]
