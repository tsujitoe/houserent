from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.post_upload_images_test_database, name='home'),
    #url(r'^upload$', views.post_upload_images_test_database, name='post'),
    
]
