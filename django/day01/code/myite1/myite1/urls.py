"""myite1 URL Configuration

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
    url(r'^page1',views.page1_view),
    url(r'^$',views.index_view),
    url(r'^page2',views.page2_view),
    #配置/page3..../page3...
    url(r'^page(\d+)',views.pagen_view),
    url(r'(\d+)/(\w{3})/(\d+)',views.math_view),
    url(r'^person/(?P<name>\w+)/(?P<age>\d{1,2})',
        views.person_view),
    url(r'^birthday/(?P<y>\d{4})/(?P<m>\d{1,2})/(?P<d>\d{1,2})',
        views.birthday_view),
    url(r'^birthday/(?P<m>\d{1,2})/(?P<d>\d{1,2})/(?P<y>\d{4})/',
        views.birthday_view),
    url(r'^mypage',views.mypage_view)
]
