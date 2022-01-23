#file bookstore/urls.py

from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^add',views.add_view),
    url(r'^all',views.show_all),
    url(r'^mod/(\d+)',views.mod_view),
    url(r'^del/(\d+)',views.del_view),
    url(r'^set_cookie',views.set_cookies_view),
    url(r'^get_cookie',views.get_cookies_view)
]