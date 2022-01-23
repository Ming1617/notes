from . import views
from django.conf.urls import url
urlpatterns=[
    # url(r'datail/<int:user>',views.user_detail)
    url(r'detail/(?P<user_id>[\w]{1,11})$',views.user_detail),
    url(r'update',views.user_update)
]