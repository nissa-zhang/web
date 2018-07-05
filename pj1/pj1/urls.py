"""pj1 URL Configuration

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
from django.urls import path

from django.conf.urls import url, include
from item import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^wel$', views.welcome, name='abc'),
    url(r'^doget/(.*)$',views.doget_execute, name='doget_e'),
    url(r'^doget/(?P<param1>.*)$',views.doget_execute, name='doget_p'),
    url(r'^showtemp1$', views.showtemp1, name='showtemp1'),

    url(r'^item/', include('item.urls')),

    url(r'show/$', views.welcome, name='wel'),
]
