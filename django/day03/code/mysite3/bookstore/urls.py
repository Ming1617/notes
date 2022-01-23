#file bookstore/urls.py

from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^add_book',views.add_view),
]