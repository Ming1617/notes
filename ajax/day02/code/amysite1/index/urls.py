from django.conf.urls import url
from . import views

urlpatterns = [
    #http://127.0.0.1:8000/index/xhr
    url(r'^xhr$', views.xhr_view),
    #http://127.0.0.1:8000/index/xhr_get
    url(r'^xhr_get$', views.xhr_get),
    #http://127.0.0.1:8000/index/xhr_get_server
    url(r'^xhr_get_server$', views.xhr_get_server),
    #http://127.0.0.1:8000/index/check_username
    url(r'^check_username$', views.check_username),
    #http://127.0.0.1:8000/index/register
    url(r'^register$', views.register),
    #http://127.0.0.1:8000/index/xhr_post
    url(r'^xhr_post$', views.xhr_post),
    #http://127.0.0.1:8000/index/xhr_post_server
    url(r'^xhr_post_server$', views.xhr_post_server),
    #http://127.0.0.1:8000/index/get_user
    url(r'^get_user$', views.get_user),
    #http://127.0.0.1:8000/index/get_user_server
    url(r'^get_user_server$', views.get_user_server),
    #http://127.0.0.1:8000/index/test_json
    url(r'^test_json$', views.test_json),
    #http://127.0.0.1:8000/index/json_dumps
    url(r'^json_dumps$', views.json_dumps)
]