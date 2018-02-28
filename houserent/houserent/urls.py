"""houserent URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings

from pages.views import index


urlpatterns = [
    url(r'^$', index, name='index'),

    url(r'^suite/', include('suite.urls')),
    url(r'^home/', include('home.urls')),

    url(r'^devhouse/', include('devhouse.urls')),
    url(r'^devtenant/', include('devtenant.urls')),
    url(r'^devstreet/', include('devstreet.urls')),
    #url(r'^$', lambda x: HttpResponseRedirect('/devstreet/new/')),
    url(r'^gostreet/', include('gostreet.urls')),

    # use app

    #url(r'^capture/',  include('screamshot.urls', namespace='screamshot', app_name='screamshot')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^nested_admin/', include('nested_admin.urls')),
    #path('admin/', admin.site.urls),       # 2.0 和 1.8 差別在url & path
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  
