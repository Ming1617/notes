"""mysite2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^sum',views.sum_view),
    url(r'^login$',views.login_view),
    url(r'^login2',views.login2_view),
    url(r'^test$',views.test_view),
    url(r'^test2',views.mytemp_view),
    url(r'^mycal$',views.mycal_view),
    url(r'test_for$',views.for_view),


    url(r'^$',views.index_view),
    url(r'^sport',views.sport_view),
    url(r'^news',views.news_view)
]
