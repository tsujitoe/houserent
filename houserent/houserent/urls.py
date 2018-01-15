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
from django.http import HttpResponseRedirect

from pages.views import home


urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^suite/', include('suite.urls')),

    url(r'^devhouse/', include('devhouse.urls')),
    url(r'^devtenant/', include('devtenant.urls')),

    url(r'^devstreet/', include('devstreet.urls')),
    #url(r'^$', lambda x: HttpResponseRedirect('/devstreet/new/')),

    # 2.0 和 1.8 差別在url & path
    url(r'^admin/', include(admin.site.urls)),
    #path('admin/', admin.site.urls),
    #url(r'^capture/',  include('screamshot.urls', namespace='screamshot', app_name='screamshot')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  